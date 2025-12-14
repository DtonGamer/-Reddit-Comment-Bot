# Reddit Comment Bot - Project Documentation

## Project Overview

The Reddit Comment Bot is a Python-based automation tool that scans Reddit for specific comments matching a designated search string and replies to them with a predefined message. The bot runs continuously, checking for new comments in a specified subreddit and avoiding duplicate replies by tracking previous interactions in a local file.

### Main Components

- **reddit_bot.py**: The main executable script that handles Reddit API interaction, comment scanning, and reply functionality
- **config.py**: Configuration file containing all necessary settings including Reddit credentials, target parameters, and bot behavior
- **comments_replied_to.txt**: Persistent storage file that tracks comment IDs the bot has already replied to
- **readme.md**: Basic setup and usage instructions

### Technologies Used

- **Python**: Core programming language
- **PRAW (Python Reddit API Wrapper)**: Library for interacting with the Reddit API
- **Prawcore**: Core library for PRAW that handles API communications
- **Built-in Python modules**: logging, time, os

## Building and Running

### Prerequisites

1. Install Python (3.x recommended)
2. Install the PRAW library:
   ```bash
   pip install praw
   ```

### Setup Process

1. **Create Reddit App**:
   - Navigate to https://www.reddit.com/prefs/apps/
   - Click "create an app"
   - Set name, type as "Script", and redirect URI as "http://localhost:8080"
   - Note the client ID and secret

2. **Configure the Bot**:
   - Update `config.py` with your Reddit credentials and API details
   - Set target subreddit, search string, and reply message
   - Adjust sleep duration as needed

3. **Run the Bot**:
   ```bash
   python reddit_bot.py
   ```

### Running the Bot

The bot operates as an infinite loop with the following cycle:
- Scans the last 1,000 comments in the target subreddit
- Looks for comments containing the target string
- Replies to qualifying comments with the configured message
- Tracks replied comments to prevent duplicates
- Sleeps for the configured duration before repeating

## Development Conventions

### Code Structure

The code follows a modular approach with dedicated functions for:
- `bot_login()`: Handles Reddit authentication
- `run_bot()`: Main bot execution loop
- `process_comments()`: Iterates through comments in subreddit
- `process_single_comment()`: Evaluates and responds to individual comments
- `get_saved_comments()`: Manages persistent reply tracking

### Error Handling

The bot includes robust error handling for:
- Rate limiting with exponential backoff
- Permission errors when replying to restricted posts
- General API exceptions
- Connection issues and unexpected errors

### Logging

The bot implements comprehensive logging with timestamps and severity levels to track:
- Login and authentication events
- Found target strings in comments
- Successful replies to comments
- Errors and exception handling

### File Tracking

The bot maintains state between sessions using `comments_replied_to.txt`:
- Each comment ID is stored after a successful reply
- Previously replied comments are skipped to prevent spam
- The file persists across bot restarts

## Key Features

- **Persistent Reply Tracking**: Avoids replying multiple times to the same comment
- **Rate Limit Handling**: Implements backoff strategies for Reddit API rate limits
- **Configurable Settings**: Easy configuration through the config.py file
- **Comprehensive Logging**: Detailed logs for monitoring bot activity
- **Error Resilience**: Continues operation even when encountering errors
- **Permission Handling**: Gracefully handles posts where replies are forbidden