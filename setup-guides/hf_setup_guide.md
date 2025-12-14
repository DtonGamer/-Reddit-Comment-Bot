# Crayon Travel Helper Bot - Hugging Face Integration Setup

## Overview
The bot now includes integration with Hugging Face models for generating contextual, human-like responses. This enhances the bot's ability to provide relevant, natural-sounding responses based on the specific comment and subreddit context.

## Required Setup

### 1. Get a Hugging Face Token
1. Go to https://huggingface.co/settings/tokens
2. Create a new token with read access
3. Copy the token value

### 2. Set Environment Variables
You need to set the HF_TOKEN environment variable:

**Windows:**
```
set HF_TOKEN=your_token_here
```

Or permanently in system variables:
- Open System Properties → Advanced → Environment Variables
- Add new system variable: `HF_TOKEN` with your token as value

**Linux/Mac:**
```bash
export HF_TOKEN=your_token_here
```

### 3. Optional: Customize Model
By default, the bot uses `Qwen/Qwen2.5-7B-Instruct`. You can change this by setting the `HF_MODEL` environment variable:

```
HF_MODEL=meta-llama/Llama-3.1-8B-Instruct
```

Available recommended models:
- `Qwen/Qwen2.5-7B-Instruct` (default - good balance)
- `meta-llama/Llama-3.1-8B-Instruct` (high quality)
- `teknium/OpenHermes-2.5-Mistral-7B` (natural conversation)
- `microsoft/Phi-3-mini-4k-instruct` (lightweight)

## How It Works

The bot uses the Hugging Face Serverless Inference API to:
1. Analyze the user's comment and subreddit context
2. Generate a relevant, contextual response
3. Include natural mentions of your crayon-style travel journals when appropriate
4. Maintain the friendly, helpful tone of "Travel Planning Enthusiast"

## Fallback Behavior

If Hugging Face integration isn't configured or fails, the bot falls back to:
1. Destination-specific rule-based responses (Tokyo, Paris, etc.)
2. Generic response templates

## Rate Limits

Hugging Face's free tier includes limited requests per hour. The bot is configured to handle API failures gracefully with fallback responses.

## Testing

After setting up your token, you can test the integration by:
1. Running the bot
2. Looking for log messages about Hugging Face initialization
3. Checking if responses appear more contextual than template-based ones

Example prompt sent to the model:
```
You are a helpful travel advisor named Travel Planning Enthusiast (username: crayontravel_helper).
You create hand-drawn style travel journals and share travel planning tips.
A Reddit user in r/travel asked: "Planning a trip to Japan, overwhelmed by options"
Provide helpful, friendly travel advice that addresses their question directly.
Keep responses concise but informative (2-3 paragraphs max).
At the end, naturally mention that you create crayon-style travel journals if relevant to their query,
but only if it fits naturally and adds value.
Use a friendly, knowledgeable tone.
```