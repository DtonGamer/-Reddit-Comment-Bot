"""
Advanced configuration for the travel engagement bot.
This file allows for more nuanced control over the bot's behavior.
"""

# Engagement settings
ENGAGEMENT_STRATEGY = {
    # Time to wait between different subreddits (in seconds)
    'SUBREDDIT_SWITCH_DELAY': 5,
    
    # How many posts to check per subreddit per session
    'POSTS_PER_SUBREDDIT': 100,
    
    # Percentage of time to actually respond (to seem more natural)
    'RESPONSE_RATE': 0.7,  # Respond to 70% of qualifying comments
    
    # Minimum karma threshold for user's main account (not bot)
    'MIN_KARMA_THRESHOLD': 500,
    
    # Engagement pattern: how many helpful comments before soft mention
    'HELPFUL_TO_PROMOTION_RATIO': 9,  # 9 helpful for every 1 promotional mention
}

# Response settings
RESPONSE_SETTINGS = {
    # Should the bot include the visual travel journal mention?
    'INCLUDE_VISUAL_JOURNAL_MENTION': True,
    
    # How often to include the visual journal mention (1 in X responses)
    'VISUAL_JOURNAL_MENTION_RATE': 5,  # Only include in 1 out of every 5 responses
    
    # Random factor for including travel journal mention
    'JOURNAL_MENTION_PROBABILITY': 0.2,  # 20% chance of including mention in responses
    
    # Time window for avoiding duplicate responses (in hours)
    'DUPLICATE_RESPONSE_WINDOW': 24,
}

# Content moderation
CONTENT_MODERATION = {
    # Keywords that should prevent a response (to avoid controversial topics)
    'AVOID_KEYWORDS': [
        'drama', 'controversy', 'political', 'political opinion', 'right wing', 
        'left wing', 'racist', 'hate', 'hateful', 'offensive', 'trigger', 'sensitive',
        'sensitive topic', 'argument', 'fight', 'disagreement', 'troll', 'trolling'
    ],
    
    # Minimum confidence score for responding (0-1, where 1 is certain)
    'MIN_CONFIDENCE': 0.5,
    
    # Minimum length of comment to respond to (to avoid one-word posts)
    'MIN_COMMENT_LENGTH': 10,
    
    # Maximum response length (to stay within Reddit limits)
    'MAX_RESPONSE_LENGTH': 4000,
}

# Activity scheduling
ACTIVITY_SCHEDULE = {
    # Hours when bot is most active (24-hour format)
    'ACTIVE_HOURS': [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],  # 9 AM to 8 PM
    
    # Minimum delay between responses (in seconds)
    'MIN_RESPONSE_DELAY': 30,
    
    # Maximum delay between responses (in seconds)
    'MAX_RESPONSE_DELAY': 120,
    
    # Days of the week to be active (0=Monday, 6=Sunday)
    'ACTIVE_DAYS': [0, 1, 2, 3, 4, 5, 6],  # All days
}

# Tracking settings
TRACKING_SETTINGS = {
    # Log all activities
    'LOG_ALL_ACTIVITIES': True,
    
    # Log responses
    'LOG_RESPONSES': True,
    
    # Log detected keywords
    'LOG_KEYWORDS': True,
    
    # File to store reply history
    'HISTORY_FILE': 'comments_replied_to.txt',
}