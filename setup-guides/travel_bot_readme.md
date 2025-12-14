# Crayon Travel Helper - Reddit Engagement Bot

## Overview
The Crayon Travel Helper is an automated Reddit bot designed to engage with travel communities by providing helpful advice and building trust through genuine community participation. The bot monitors specific travel-related subreddits for posts with travel planning questions and responds with contextually appropriate advice using advanced AI.

## Features
- Monitors multiple travel-related subreddits (travel, solotravel, JapanTravel, etc.)
- Searches for specific keywords related to travel planning and advice requests
- Generates contextual responses using Hugging Face AI models for natural, relevant replies
- Includes session-based limitations to avoid spamming
- Tracks replied comments to prevent duplicate responses
- Comprehensive logging for monitoring bot activity
- Natural mentions of your crayon-style travel journals when contextually appropriate

## Configuration

Update the `config.py` file with your Reddit account details:

- `REDDIT_USERNAME`: Your Reddit username (default: crayontravel_helper)
- `REDDIT_PASSWORD`: Your Reddit account password
- `REDDIT_CLIENT_ID`: Your Reddit app client ID (from Reddit App Preferences)
- `REDDIT_CLIENT_SECRET`: Your Reddit app client secret
- `REDDIT_USER_AGENT`: A unique identifier for your bot
- `TARGET_SUBREDDITS`: List of subreddits to monitor (already configured)
- `TARGET_STRINGS`: Keywords that trigger bot responses (already configured)
- `REPLY_TEMPLATES`: Generic response starters (already configured)
- `SLEEP_DURATION`: Time between scanning sessions (default: 60 seconds)

**Using Environment Variables:**
For security, it's recommended to use environment variables instead of editing config.py directly:

1. Copy the `.env` template file to `.env.local`
2. Fill in your credentials in the `.env.local` file
3. The bot will automatically load these values
4. The `.env` file is included in `.gitignore` to protect your credentials

## AI Integration Setup

To enable contextual response generation with Hugging Face models:

1. Get a Hugging Face token from https://huggingface.co/settings/tokens
2. Set the environment variable `HF_TOKEN` with your token
3. Optionally set `HF_MODEL` to specify which model to use (default: Qwen/Qwen2.5-7B-Instruct)

See hf_setup_guide.md for complete setup instructions.

## Ethical Usage Guidelines

This bot is designed to follow Reddit's engagement best practices:

- Builds karma through valuable contributions (targets 500+ karma initially)
- Never leads with promotional content - always answers the question first
- Uses the 9:1 rule (9 helpful comments for every 1 soft mention of your service)
- Limits responses to avoid appearing spammy
- Provides genuine value before mentioning your crayon-style travel journal service

## Deployment

### Local Deployment
1. Install dependencies: `pip install -r requirements.txt`
2. Configure your Reddit app credentials in `config.py` or use environment variables
3. Customize the response templates as needed
4. Run the bot: `python reddit_bot.py`

### Cloud Deployment (Recommended for 24/7 operation)
For continuous operation, we recommend deploying to Railway:

1. Push your code to a GitHub repository
2. Sign up at https://railway.app
3. Connect your GitHub repository to Railway
4. Set the required environment variables in Railway dashboard:
   - `REDDIT_USERNAME`, `REDDIT_PASSWORD`, `REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET`
   - `HF_TOKEN` (optional, for AI responses)
5. Add the Procfile, runtime.txt, and requirements.txt files (included in this project)
6. Click "Deploy Now"

See `railway_setup_guide.md` for complete step-by-step instructions.

## Customizing Responses

The bot includes special handling for Tokyo and Paris queries. You can extend the `generate_response` function in `reddit_bot.py` to add more destination-specific responses based on the example templates provided.

## Important Notes

- Monitor your bot's activity to ensure compliance with subreddit rules
- Adjust the target strings and reply templates to match your engagement strategy
- Be mindful of rate limits when testing
- Consider Reddit's terms of service and each subreddit's specific rules

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.