# Crayon Travel Helper - Reddit Engagement Bot

This is an advanced Reddit engagement bot designed for travel communities. It uses AI to generate contextual, human-like responses to travel-related questions while building genuine community trust.

## Features

- **AI-Powered Responses**: Uses Hugging Face models to generate natural, contextual replies
- **Travel-Focused**: Pre-configured for travel-related subreddits (travel, solotravel, JapanTravel, etc.)
- **Ethical Engagement**: Follows Reddit best practices with 9:1 helpful-to-promotional ratio
- **Smart Targeting**: Monitors multiple keywords and subreddits relevant to travel planning
- **Rate Limiting**: Includes session-based limits to avoid spam detection
- **24/7 Operation**: Can be deployed to Railway for continuous operation
- **Customizable**: Easy configuration via environment variables

## Requirements

- [Python](https://www.python.org/downloads/)
- [Praw](https://praw.readthedocs.io/en/latest/getting_started/installation.html)
- A Reddit Account
- (Optional) Hugging Face API token for AI responses

## Setup

### Reddit App Configuration:
1. [Navigate to the Apps page](https://www.reddit.com/prefs/apps/)
2. Click *create an app*
3. **name:** Set a name for your app
4. **type:** Script
5. **description:** Optional
6. **about url:** Optional
7. **redirect uri:** http://localhost:8080
8. Note the outputted *client id* and *secret*

### Environment Variables (recommended):
Set these environment variables:

**Required Reddit Credentials:**
- `REDDIT_USERNAME`: Your Reddit username
- `REDDIT_PASSWORD`: Your Reddit password
- `REDDIT_CLIENT_ID`: Your Reddit app client ID
- `REDDIT_CLIENT_SECRET`: Your Reddit app client secret
- `REDDIT_USER_AGENT`: A unique identifier for your bot

**Optional Hugging Face Integration:**
- `HF_TOKEN`: Hugging Face API token (for AI responses)
- `HF_MODEL`: Model to use (default: Qwen/Qwen2.5-7B-Instruct)

**Optional Bot Configuration:**
- `SLEEP_DURATION`: Sleep duration between bot runs in seconds (default: 60)
- `MAX_COMMENTS_PER_SESSION`: Max comments per session (default: 10)
- `MAX_REPLY_PER_POST`: Max replies per post (default: 2)

**Using the .env file:**
1. Copy the `.env` template file to `.env.local`
2. Fill in your credentials in the `.env.local` file
3. The bot will automatically load these values

⚠️ **Security Warning**: The `.env` file is ignored by git to protect your credentials. Never commit credentials to version control.

## Usage

### Local Installation:
1. Install dependencies: `pip install -r requirements.txt`
2. Set environment variables with your Reddit credentials
3. Run the bot: `python reddit_bot.py`

### Railway Deployment (24/7 Operation):
1. Push your code to a GitHub repository
2. Connect to Railway (see setup-guides/railway_setup_guide.md)
3. Set environment variables in Railway dashboard
4. Bot runs continuously without requiring your computer to stay on

## Advanced Configuration

The bot includes sophisticated configuration options:
- Multiple target subreddits (travel, solotravel, JapanTravel, etc.)
- Smart keyword detection for travel planning questions
- Time-based activity scheduling
- Content moderation to avoid controversial topics
- Session-limited engagement to follow Reddit guidelines
- **Context Management**: Provide specific context for different destinations and topics to make responses more targeted and relevant

### Context Management
The bot can use specific context for different subreddits and topics:
- Context files are stored in the `context/` directory
- Different contexts are automatically applied based on the subreddit
- You can create custom context files for specific destinations or topics
- Context helps the AI generate more accurate and relevant responses

See `config.py` and `advanced_config.py` for detailed settings.

## Ethical Usage Guidelines

This bot follows Reddit engagement best practices:
- Builds karma through valuable contributions
- Never leads with promotional content - always answers the question first
- Uses the 9:1 rule (9 helpful comments for every 1 soft mention of your service)
- Limits responses to avoid appearing spammy
- Provides genuine value before mentioning your crayon-style travel journal service

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.