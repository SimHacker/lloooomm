# YouTube API Bot Setup Guide

## Overview

This is the **proper way** to interact with YouTube comments - using Google's official YouTube Data API v3 instead of fragile browser automation. No more contenteditable nightmares!

## Step 1: Install Dependencies

```bash
cd lloooomm/scripts
pip install -r requirements.txt
```

## Step 2: Google Cloud Console Setup

### 2.1 Create Project
1. Go to https://console.cloud.google.com/
2. Click "Select a project" → "NEW PROJECT"
3. Choose a project name (e.g., "YouTube Comment Bot")
4. Click "Create"

### 2.2 Enable YouTube Data API
1. In your project dashboard, click "APIs & Services" → "Library"
2. Search for "YouTube Data API v3"
3. Click on it and press "ENABLE"

### 2.3 Create OAuth 2.0 Credentials
1. Go to "APIs & Services" → "Credentials"
2. Click "CREATE CREDENTIALS" → "OAuth client ID"
3. If prompted, configure the consent screen:
   - Application name: "YouTube Comment Bot"
   - Authorized domains: (leave blank for now)
   - Save
4. Choose application type: **"Desktop application"**
5. Name: "YouTube Bot Client"
6. Click "Create"
7. **Download the JSON file** (e.g., `client_secret_123.json`)

## Step 3: Configure Environment

```bash
# Set environment variable pointing to your credentials file
export YOUTUBE_CLIENT_SECRET_FILE="/path/to/your/client_secret_123.json"

# Or add to your ~/.bashrc / ~/.zshrc:
echo 'export YOUTUBE_CLIENT_SECRET_FILE="/path/to/your/client_secret_123.json"' >> ~/.bashrc
```

## Step 4: Test the Bot

```bash
# Test with your LLOOOOMM video
python youtube_comment_api_bot.py TTa4BOVG7VA

# Or any other video ID
python youtube_comment_api_bot.py VIDEO_ID_HERE
```

### First Run Authentication
1. The script will open a browser window
2. Sign in to your Google account
3. Grant permission to access YouTube
4. Copy the authorization code back to terminal
5. A `youtube_token.pickle` file will be saved for future use

## Step 5: Understanding the Output

The bot will:
1. 🔍 Fetch comments from the specified video
2. 🎯 Find comments matching keywords (github, project, repository, etc.)
3. 🎭 Generate appropriate emacs cat replies
4. 💡 Show what it would post (but won't actually post unless you uncomment the code)

## Step 6: Enable Actual Posting (Optional)

⚠️ **BE CAREFUL!** Only uncomment this after testing:

In `youtube_comment_api_bot.py`, find this section:
```python
# Uncomment to actually post replies (be careful!)
# for comment in target_comments[:1]:  # Only reply to first one
#     reply = bot.create_emacs_cat_reply(comment)
#     bot.post_reply(comment['id'], reply)
#     break  # Only post one reply for safety
```

Remove the `#` comments to enable actual posting.

## API Quotas and Limits

- **Free quota**: 10,000 units per day
- **Reading comments**: 1 unit per request
- **Posting comments**: 50 units per comment
- **Rate limits**: 100 requests per 100 seconds per user

## Security Best Practices

1. **Never commit credentials** to version control
2. **Use environment variables** for sensitive data
3. **Restrict OAuth scopes** to minimum required
4. **Monitor API usage** in Google Cloud Console
5. **Test thoroughly** before enabling posting

## Advanced Features

### Custom Comment Matching
Modify the `find_comments_to_reply_to()` method to use:
- Sentiment analysis
- Regular expressions
- Machine learning models
- User whitelist/blacklist

### Multiple Accounts
Create separate credential files for different YouTube accounts.

### Batch Processing
Process multiple videos by reading video IDs from a file.

### Database Integration
Store comments and replies in a database for analytics.

## Troubleshooting

### "Error: Please set YOUTUBE_CLIENT_SECRET_FILE"
Make sure the environment variable points to your downloaded JSON file.

### "Error 403: Access forbidden"
Your OAuth app needs to be verified for posting comments. During development, add test users in the OAuth consent screen.

### "Error: Video not found"
Check that the video ID is correct and the video is public.

### "NoLinkedYouTubeAccount error"
You're trying to use service account credentials. Use OAuth 2.0 instead.

## Why This Approach is Superior

| Browser Automation | YouTube Data API |
|-------------------|------------------|
| ❌ Fragile (breaks with UI changes) | ✅ Stable API contract |
| ❌ Slow DOM manipulation | ✅ Fast JSON responses |
| ❌ Security restrictions | ✅ Designed for automation |
| ❌ Against Terms of Service | ✅ Official Google API |
| ❌ Contenteditable nightmares | ✅ Clean data structures |
| ❌ No rate limiting | ✅ Proper quota management |

## Further Reading

- [YouTube Data API Documentation](https://developers.google.com/youtube/v3)
- [OAuth 2.0 Authentication](https://developers.google.com/youtube/v3/guides/authentication)
- [Comment API Reference](https://developers.google.com/youtube/v3/docs/comments)
- [Best Practices](https://developers.google.com/youtube/v3/guides/implementation/comments) 