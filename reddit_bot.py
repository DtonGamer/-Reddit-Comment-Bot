# Importing necessary libraries
from __future__ import print_function
import praw
import prawcore
import time
import os
import logging
import random
import json
from datetime import datetime
from config import (
    REDDIT_USERNAME,
    REDDIT_PASSWORD,
    REDDIT_CLIENT_ID,
    REDDIT_CLIENT_SECRET,
    REDDIT_USER_AGENT,
    TARGET_SUBREDDITS,
    TARGET_STRINGS,
    REPLY_TEMPLATES,
    SLEEP_DURATION,
    MIN_KARMA_THRESHOLD,
    MAX_COMMENTS_PER_SESSION,
    MAX_REPLY_PER_POST,
)
from response_templates import get_destination_specific_response, GENERIC_RESPONSES, load_context_from_file
from advanced_config import ENGAGEMENT_STRATEGY, RESPONSE_SETTINGS, CONTENT_MODERATION, ACTIVITY_SCHEDULE, TRACKING_SETTINGS

# Configuring logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Global variables to track session activity
session_comments_count = 0
posts_replied_to = {}

# Function to handle rate limit with exponential backoff
def handle_rate_limit(api_exception, retry_attempts=3):
    for attempt in range(retry_attempts):
        retry_after = api_exception.response.headers.get('retry-after')
        if retry_after:
            logger.warning(f"Rate limited. Retrying after {retry_after} seconds. Attempt {attempt + 1}/{retry_attempts}")
            time.sleep(int(retry_after) + 1)
        else:
            logger.error(f"API Exception: {api_exception}")
            break
    else:
        logger.error("Exceeded retry attempts. Aborting.")
        raise

# Function to log in to Reddit
def bot_login():
    logger.info("Logging in...")

    try:
        reddit_instance = praw.Reddit(
            username=REDDIT_USERNAME,
            password=REDDIT_PASSWORD,
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent=REDDIT_USER_AGENT
        )
        logger.info("Logged in!")
        return reddit_instance
    except prawcore.exceptions.ResponseException as e:
        logger.error(f"Login failed: {e}")
        raise
    except Exception as e:
        logger.exception(f"Unexpected error during login: {e}")
        raise

# Function to run the bot
def run_bot(reddit_instance, comments_replied_to):
    global session_comments_count, posts_replied_to

    logger.info(f"Starting bot session. Current session comments count: {session_comments_count}")

    # Reset session tracking if session limit reached
    if session_comments_count >= MAX_COMMENTS_PER_SESSION:
        logger.info("Max comments per session reached. Resetting session counters.")
        session_comments_count = 0
        posts_replied_to = {}

    # Process comments from each target subreddit
    for subreddit_name in TARGET_SUBREDDITS:
        logger.info(f"Searching last 1,000 comments in subreddit {subreddit_name}")
        try:
            process_comments(reddit_instance, comments_replied_to, subreddit_name)
        except praw.exceptions.APIException as api_exception:
            # Handle rate limits
            handle_rate_limit(api_exception)
        except Exception as e:
            # Log other exceptions
            logger.exception(f"An error occurred while processing {subreddit_name}: {e}")

    logger.info(f"Session completed. Comments replied in this session: {session_comments_count}. Sleeping for {SLEEP_DURATION} seconds...")
    time.sleep(int(SLEEP_DURATION))

# Function to process comments
def process_comments(reddit_instance, comments_replied_to, subreddit_name):
    global session_comments_count

    try:
        subreddit = reddit_instance.subreddit(subreddit_name)
        # Limit to fewer comments to be more targeted
        for comment in subreddit.comments(limit=ENGAGEMENT_STRATEGY['POSTS_PER_SUBREDDIT']):
            if session_comments_count >= MAX_COMMENTS_PER_SESSION:
                break
            try:
                process_single_comment(comment, comments_replied_to, subreddit_name)
            except prawcore.exceptions.Forbidden as forbidden_error:
                logger.warning(f"Permission error for comment {comment.id}: {forbidden_error}. Skipping.")
            except Exception as error:
                logger.exception(f"Error processing comment {comment.id}: {error}")

            # Add delay between processing comments to avoid rate limits
            time.sleep(ENGAGEMENT_STRATEGY['SUBREDDIT_SWITCH_DELAY'])
    except Exception as e:
        logger.exception(f"Error accessing subreddit {subreddit_name}: {e}")

    # Log when the search is completed
    logger.info(f"Completed processing {subreddit_name}.")

# Function to check if comment contains target keywords
def contains_target_keywords(comment_body):
    comment_lower = comment_body.lower()
    for target_string in TARGET_STRINGS:
        if target_string.lower() in comment_lower:
            return True
    return False

def get_context_for_subreddit(subreddit_name):
    """
    Get specific context based on the subreddit.
    """
    context_map = {
        'JapanTravel': 'context/japan_context.md',
        'Tokyo': 'context/japan_context.md',
        'japan': 'context/japan_context.md',
        'EuropeTravelTips': 'context/europe_context.md',
        'europe': 'context/europe_context.md',
        'Paris': 'context/europe_context.md',
        'travel': 'context/travel_journal_context.md',
        'solotravel': 'context/travel_journal_context.md',
        'travel_tips': 'context/travel_journal_context.md',
        'TravelHacks': 'context/travel_journal_context.md',
        'backpacking': 'context/travel_journal_context.md',
        'digitalnomad': 'context/travel_journal_context.md',
        'ThailandTourism': 'context/travel_journal_context.md',
        'bali': 'context/travel_journal_context.md',
        'VisitingIceland': 'context/travel_journal_context.md',
        'italianlearning': 'context/europe_context.md'
    }

    context_file = context_map.get(subreddit_name.lower())
    if context_file:
        context = load_context_from_file(context_file)
        if context:
            return context

    # Default context if no specific context found
    default_context = load_context_from_file('context/travel_journal_context.md')
    return default_context if default_context else ""


# Function to generate a contextually appropriate response
def generate_response(comment, target_string_found):
    # Get context specific to the subreddit
    subreddit_context = get_context_for_subreddit(comment.subreddit.display_name)

    # Use the Hugging Face model to generate a contextual response with additional context
    return generate_contextual_response(comment.body, comment.subreddit.display_name, subreddit_context)

# Function to process a single comment
def process_single_comment(comment, comments_replied_to, subreddit_name):
    import datetime as dt

    global session_comments_count, posts_replied_to

    # Check if we've hit the session limit
    if session_comments_count >= MAX_COMMENTS_PER_SESSION:
        return

    # Check current time to see if we should be active
    current_hour = dt.datetime.now().hour
    current_day = dt.datetime.now().weekday()  # 0=Monday, 6=Sunday

    if current_hour not in ACTIVITY_SCHEDULE['ACTIVE_HOURS'] or \
       current_day not in ACTIVITY_SCHEDULE['ACTIVE_DAYS']:
        return  # Not in active hours/days

    # Check if we've already replied too many times to this post
    post_id = comment.submission.id
    if post_id in posts_replied_to and posts_replied_to[post_id] >= MAX_REPLY_PER_POST:
        return

    # Check if comment contains target keywords
    if (
        contains_target_keywords(comment.body)
        and comment.id not in comments_replied_to
        and comment.author != reddit_instance.user.me()
        and len(comment.body) >= CONTENT_MODERATION['MIN_COMMENT_LENGTH']
        and not any(avoid_word in comment.body.lower() for avoid_word in CONTENT_MODERATION['AVOID_KEYWORDS'])
    ):
        # Log when the target string is found in a comment
        logger.info(f"Target keyword found in comment {comment.id} in r/{subreddit_name}")

        # Randomly decide whether to respond based on response rate
        if random.random() > ENGAGEMENT_STRATEGY['RESPONSE_RATE']:
            return  # Skip this response based on probability

        # Generate a contextual response
        response = generate_response(comment, True)

        # Add visual journal mention based on probability
        if RESPONSE_SETTINGS['INCLUDE_VISUAL_JOURNAL_MENTION'] and \
           random.random() < RESPONSE_SETTINGS['JOURNAL_MENTION_PROBABILITY']:
            journal_mention = (
                "\n\nP.S. I create these fun, crayon-style travel journals that make planning more enjoyable. "
                "Would love to create one for your trip if you'd find it helpful!"
            )
            response += journal_mention

        # Make sure response is not too long
        if len(response) > CONTENT_MODERATION['MAX_RESPONSE_LENGTH']:
            response = response[:CONTENT_MODERATION['MAX_RESPONSE_LENGTH']-3] + "..."

        # Reply to the comment
        try:
            comment.reply(response)
            # Log that the bot has replied to the comment
            logger.info(f"Replied to comment {comment.id}")

            # Update session counters
            session_comments_count += 1
            if post_id not in posts_replied_to:
                posts_replied_to[post_id] = 0
            posts_replied_to[post_id] += 1

            # Add the comment ID to the list of comments replied to
            comments_replied_to.append(comment.id)

            # Save the comment ID to the file with timestamp
            with open("comments_replied_to.txt", "a") as f:
                f.write(f"{dt.datetime.now().isoformat()}|{comment.id}|{subreddit_name}|{comment.body[:50]}...\n")

            # Add a small delay between responses to seem more natural
            time.sleep(random.randint(ACTIVITY_SCHEDULE['MIN_RESPONSE_DELAY'],
                                     ACTIVITY_SCHEDULE['MAX_RESPONSE_DELAY']))
        except prawcore.exceptions.Forbidden as forbidden_error:
            logger.warning(f"Permission error for comment {comment.id}: {forbidden_error}. Skipping.")
        except Exception as reply_error:
            logger.exception(f"Error while replying to comment {comment.id}: {reply_error}")

# Function to get saved comments
def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        # If the file doesn't exist, initialize an empty list
        comments_replied_to = []
    else:
        # Read the file and create a list of comments (excluding empty lines)
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = [line.split('|')[1] for line in f.readlines() if line.strip() and '|' in line]  # Extract just the comment ID

    return comments_replied_to

# Main block to execute the bot
if __name__ == "__main__":
    # Log in to Reddit
    reddit_instance = bot_login()
    # Get the list of comments the bot has replied to from the file
    comments_replied_to = get_saved_comments()
    # Log the number of comments replied to
    logger.info(f"Number of comments replied to: {len(comments_replied_to)}")

    # Run the bot in an infinite loop
    while True:
        try:
            # Attempt to run the bot
            run_bot(reddit_instance, comments_replied_to)
        except Exception as e:
            # Log any general exceptions and sleep for the specified duration
            logger.exception(f"An error occurred: {e}")
            time.sleep(int(SLEEP_DURATION))  # Add a sleep after catching general exceptions
        except KeyboardInterrupt:
            logger.info("Bot terminated by user.")
            break
