# Deploying Crayon Travel Helper Bot to Railway

## Overview
This guide will help you deploy your Reddit engagement bot to Railway for 24/7 operation.

## Prerequisites

1. **GitHub Account**: Your code must be in a GitHub repository
2. **Railway Account**: Sign up at https://railway.app
3. **Reddit App Credentials**: You need your Reddit API credentials
4. **Hugging Face Token** (optional): For AI-powered responses

## Step-by-Step Deployment

### 1. Prepare Your GitHub Repository
1. Initialize a git repository in your bot directory:
   ```bash
   git init
   git add .
   git commit -m "Initial commit for Railway deployment"
   ```
2. Create a new repository on GitHub
3. Push your code:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
   git branch -M main
   git push -u origin main
   ```

### 2. Deploy to Railway
1. Go to https://railway.app and sign in
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Choose your bot repository
5. Railway will automatically detect your Python project

### 3. Configure Environment Variables
After connecting your repo, go to the "Variables" section on Railway and add these variables:

**Required Reddit Variables:**
- `REDDIT_USERNAME`: Your Reddit username (e.g., crayontravel_helper)
- `REDDIT_PASSWORD`: Your Reddit account password
- `REDDIT_CLIENT_ID`: Your Reddit app client ID
- `REDDIT_CLIENT_SECRET`: Your Reddit app client secret
- `REDDIT_USER_AGENT`: A unique identifier for your bot

**Optional Hugging Face Variables:**
- `HF_TOKEN`: Your Hugging Face API token (for AI responses)
- `HF_MODEL`: Model to use (default: Qwen/Qwen2.5-7B-Instruct)

**Optional Bot Configuration Variables:**
- `SLEEP_DURATION`: Seconds between scanning sessions (default: 60)
- `MAX_COMMENTS_PER_SESSION`: Max comments per session (default: 10)
- `MAX_REPLY_PER_POST`: Max replies per post (default: 2)

### 4. Deploy
1. Click "Deploy Now" in the Railway dashboard
2. Monitor the deployment logs to ensure everything installs properly

### 5. Monitor Your Bot
1. Use the "Logs" tab to monitor your bot's activity
2. Check that it's connecting to Reddit and responding to comments
3. Verify that environment variables are properly loaded

## Important Notes

- **Rate Limits**: Be mindful of Reddit's API rate limits even when deployed
- **Free Tier Limits**: Railway's free tier provides $5/month credit which is typically sufficient for a single bot
- **Reliability**: Railway automatically restarts your bot if it crashes
- **No Downtime**: Your bot will run continuously until you stop it or change plans

## Troubleshooting

1. **Deployment Fails**:
   - Check that requirements.txt is properly formatted
   - Verify your Python version in runtime.txt is supported

2. **Bot Won't Connect to Reddit**:
   - Verify all Reddit credentials are correct in environment variables
   - Check that your Reddit app is properly configured with correct permissions

3. **Hugging Face Integration Not Working**:
   - Confirm your HF_TOKEN is correctly set
   - Check the logs for any error messages related to the API

## Updating Your Bot

1. Make changes to your code locally
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Description of changes"
   git push origin main
   ```
3. Railway will automatically redeploy your bot

Your Reddit engagement bot will now run continuously on Railway, engaging with travel communities 24/7 without requiring your personal computer to stay on!