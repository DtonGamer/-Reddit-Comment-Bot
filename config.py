import os
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# Reddit account credentials (from environment variables)
REDDIT_USERNAME = os.getenv('REDDIT_USERNAME', 'crayontravel_helper')
REDDIT_PASSWORD = os.getenv('REDDIT_PASSWORD', 'YOUR_REDDIT_PASSWORD_HERE')

# Reddit API credentials
REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID', 'YourClientID')
REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET', 'YourClientSecret')

# Bot configuration
REDDIT_USER_AGENT = os.getenv('REDDIT_USER_AGENT', 'TravelBot v1.0 by crayontravel_helper')
TARGET_SUBREDDITS = [
    "travel",
    "solotravel",
    "TravelHacks",
    "travel_tips",
    "backpacking",
    "digitalnomad",
    "JapanTravel",
    "Tokyo",
    "Paris",
    "ThailandTourism",
    "bali",
    "VisitingIceland",
    "italianlearning",  # travel context
    "EuropeTravelTips"
]  # List of subreddits to monitor
TARGET_STRINGS = [
    "planning",
    "recommend",
    "help with",
    "where should I",
    "best places",
    "tips for",
    "itinerary",
    "visiting",
    "trip advice",
    "travel advice",
    "suggestions",
    "options",
    "overwhelmed",
    "food spots",
    "day trip",
    "must visit",
    "solo travel",
    "first time",
    "beginner"
]  # Keywords to trigger responses
REPLY_TEMPLATES = [
    "That's a great question! Based on my experience, here are some thoughts...",
    "Hey there! I've been to that destination and can definitely help. Here's what I recommend...",
    "I had a similar question recently and learned a lot about this. Here's what helped me...",
    "Great topic! Here are some tips that might be helpful for your situation...",
    "Based on what you're looking for, I'd suggest..."
]  # Generic starter templates

# Bot behavior configuration
SLEEP_DURATION = int(os.getenv('SLEEP_DURATION', '60'))  # Adjust the sleep duration as needed in seconds (1 minute)
MIN_KARMA_THRESHOLD = int(os.getenv('MIN_KARMA_THRESHOLD', '500'))  # Target karma threshold before increasing activity
MAX_COMMENTS_PER_SESSION = int(os.getenv('MAX_COMMENTS_PER_SESSION', '10'))  # Max comments to engage with per session
MAX_REPLY_PER_POST = int(os.getenv('MAX_REPLY_PER_POST', '2'))  # Max replies per post to avoid spam detection