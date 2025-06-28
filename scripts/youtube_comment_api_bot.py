#!/usr/bin/env python3
"""
YouTube Comment API Bot - The Right Way™

This uses the official YouTube Data API v3 instead of fragile browser automation.
No more contenteditable nightmares or accessibility API failures!

Requirements:
    pip install google-api-python-client google-auth-oauthlib google-auth-httplib2

Setup:
1. Go to https://console.cloud.google.com/
2. Create new project or select existing
3. Enable YouTube Data API v3
4. Create OAuth 2.0 credentials (Desktop application)
5. Download credentials JSON file
6. Set YOUTUBE_CLIENT_SECRET_FILE environment variable

Usage:
    python youtube_comment_api_bot.py VIDEO_ID
"""

import os
import sys
import json
import pickle
from typing import List, Dict, Optional

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# YouTube API scopes
SCOPES = [
    'https://www.googleapis.com/auth/youtube.readonly',
    'https://www.googleapis.com/auth/youtube.force-ssl'  # Needed for posting
]

class YouTubeCommentBot:
    def __init__(self, credentials_file: str = None):
        """Initialize the YouTube API client with OAuth authentication."""
        self.credentials_file = credentials_file or os.getenv('YOUTUBE_CLIENT_SECRET_FILE')
        if not self.credentials_file:
            raise ValueError("Please set YOUTUBE_CLIENT_SECRET_FILE environment variable")
        
        self.youtube = self._authenticate()
        print("🎉 Successfully authenticated with YouTube API!")
    
    def _authenticate(self):
        """Handle OAuth 2.0 authentication flow."""
        creds = None
        token_file = 'youtube_token.pickle'
        
        # Load existing token if available
        if os.path.exists(token_file):
            with open(token_file, 'rb') as token:
                creds = pickle.load(token)
        
        # If no valid credentials, go through OAuth flow
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                print("🔄 Refreshing expired token...")
                creds.refresh(Request())
            else:
                print("🔐 Starting OAuth authentication flow...")
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_file, SCOPES)
                creds = flow.run_local_server(port=0)
            
            # Save token for future use
            with open(token_file, 'wb') as token:
                pickle.dump(creds, token)
        
        return build('youtube', 'v3', credentials=creds)
    
    def get_video_comments(self, video_id: str, max_results: int = 100) -> List[Dict]:
        """
        Retrieve comments for a video using the official API.
        
        Args:
            video_id: YouTube video ID (e.g., 'TTa4BOVG7VA')
            max_results: Maximum number of comments to retrieve
            
        Returns:
            List of comment dictionaries with full metadata
        """
        comments = []
        
        try:
            # Get comment threads (top-level comments + some replies)
            request = self.youtube.commentThreads().list(
                part='snippet,replies',
                videoId=video_id,
                maxResults=min(max_results, 100),  # API limit is 100 per request
                order='time'  # or 'relevance'
            )
            
            while request and len(comments) < max_results:
                response = request.execute()
                
                for item in response['items']:
                    comment_data = self._extract_comment_data(item)
                    comments.append(comment_data)
                    
                    if len(comments) >= max_results:
                        break
                
                # Check if there are more pages
                request = self.youtube.commentThreads().list_next(request, response)
            
            print(f"📖 Retrieved {len(comments)} comments for video {video_id}")
            return comments
            
        except HttpError as e:
            print(f"❌ Error retrieving comments: {e}")
            return []
    
    def _extract_comment_data(self, comment_thread: Dict) -> Dict:
        """Extract useful data from comment thread response."""
        snippet = comment_thread['snippet']
        top_comment = snippet['topLevelComment']['snippet']
        
        return {
            'id': comment_thread['id'],
            'video_id': snippet['videoId'],
            'author': top_comment['authorDisplayName'],
            'author_channel_id': top_comment.get('authorChannelId', {}).get('value'),
            'text': top_comment['textDisplay'],
            'text_original': top_comment['textOriginal'],
            'like_count': top_comment['likeCount'],
            'published_at': top_comment['publishedAt'],
            'updated_at': top_comment.get('updatedAt'),
            'reply_count': snippet['totalReplyCount'],
            'can_reply': snippet['canReply'],
            'replies': self._extract_replies(comment_thread.get('replies', {}))
        }
    
    def _extract_replies(self, replies_data: Dict) -> List[Dict]:
        """Extract reply data from comment thread."""
        if not replies_data or 'comments' not in replies_data:
            return []
        
        replies = []
        for reply in replies_data['comments']:
            reply_snippet = reply['snippet']
            replies.append({
                'id': reply['id'],
                'author': reply_snippet['authorDisplayName'],
                'text': reply_snippet['textDisplay'],
                'like_count': reply_snippet['likeCount'],
                'published_at': reply_snippet['publishedAt'],
                'parent_id': reply_snippet['parentId']
            })
        
        return replies
    
    def find_comments_to_reply_to(self, comments: List[Dict], keywords: List[str] = None) -> List[Dict]:
        """
        Find comments that match certain criteria for replies.
        
        Args:
            comments: List of comment dictionaries
            keywords: List of keywords to search for (case-insensitive)
            
        Returns:
            List of comments that match the criteria
        """
        if not keywords:
            keywords = ['github', 'project', 'repository', 'code']
        
        matching_comments = []
        
        for comment in comments:
            text = comment['text'].lower()
            if any(keyword.lower() in text for keyword in keywords):
                matching_comments.append(comment)
        
        print(f"🎯 Found {len(matching_comments)} comments matching keywords: {keywords}")
        return matching_comments
    
    def post_reply(self, parent_comment_id: str, reply_text: str) -> bool:
        """
        Post a reply to a comment using the official API.
        
        Args:
            parent_comment_id: ID of the comment to reply to
            reply_text: Text content of the reply
            
        Returns:
            True if successful, False otherwise
        """
        try:
            request_body = {
                'snippet': {
                    'parentId': parent_comment_id,
                    'textOriginal': reply_text
                }
            }
            
            response = self.youtube.comments().insert(
                part='snippet',
                body=request_body
            ).execute()
            
            print(f"✅ Successfully posted reply: {response['id']}")
            return True
            
        except HttpError as e:
            print(f"❌ Error posting reply: {e}")
            if e.resp.status == 403:
                print("💡 Tip: Make sure your OAuth app is verified and has necessary scopes")
            return False
    
    def create_emacs_cat_reply(self, original_comment: Dict) -> str:
        """
        Generate an appropriate emacs cat reply based on the original comment.
        
        Args:
            original_comment: The comment dictionary to reply to
            
        Returns:
            Generated reply text
        """
        author = original_comment['author']
        text = original_comment['text'].lower()
        
        # Detect what the person is asking about
        if 'github' in text or 'repository' in text or 'project' in text:
            return f"""🐱 *purrs in emacs*

Hello {author}! Yes indeed, this is showcasing the LLOOOOMM project - a fascinating GitHub repository exploring visual programming languages and emoji-based communication.

The project demonstrates expressive, visual programming environments that transcend traditional text-based coding. Think of it as Lisp meets emoji meets visual programming!

You can find the full project at: https://github.com/SimHacker/HackerNews

*adjusts tiny programmer glasses with paw* 🤓

The video shows live coding sessions where Don Hopkins demonstrates the LLOOOOMM language - quite mesmerizing to watch ideas flow from concept to visual representation!"""
        
        elif 'confused' in text or "don't understand" in text or 'what is' in text:
            return f"""🐱 *purrs knowingly*

No worries {author}! LLOOOOMM is a visual programming language that uses emojis and symbols to create expressive code. It's part research project, part artistic exploration of how we communicate with computers.

Think of it as a bridge between human expression and computational logic - where code becomes as expressive as natural language! 

*swishes tail thoughtfully* 📚

The GitHub repo has lots of examples: https://github.com/SimHacker/HackerNews"""
        
        else:
            return f"""🐱 *meows appreciatively*

Thanks for watching, {author}! LLOOOOMM is definitely a unique approach to programming - combining visual elements, emojis, and computational thinking in fascinating ways.

*purrs while compiling* 💻✨"""

def main():
    """Main function to demonstrate the YouTube Comment Bot."""
    if len(sys.argv) != 2:
        print("Usage: python youtube_comment_api_bot.py VIDEO_ID")
        print("Example: python youtube_comment_api_bot.py TTa4BOVG7VA")
        sys.exit(1)
    
    video_id = sys.argv[1]
    
    try:
        # Initialize the bot
        bot = YouTubeCommentBot()
        
        # Get comments from the video
        print(f"🔍 Fetching comments for video: {video_id}")
        comments = bot.get_video_comments(video_id, max_results=50)
        
        if not comments:
            print("No comments found!")
            return
        
        # Find comments to reply to
        target_comments = bot.find_comments_to_reply_to(
            comments, 
            keywords=['github', 'project', 'repository', 'confused', 'what is this']
        )
        
        if not target_comments:
            print("No suitable comments found to reply to.")
            return
        
        # Demo: Show what we would reply to (but don't actually post)
        print("\n🎭 Found comments to reply to:")
        for i, comment in enumerate(target_comments[:3]):  # Show first 3
            print(f"\n--- Comment {i+1} ---")
            print(f"Author: {comment['author']}")
            print(f"Text: {comment['text'][:100]}...")
            print(f"Generated Reply:")
            reply = bot.create_emacs_cat_reply(comment)
            print(reply)
            print("-" * 50)
        
        # Uncomment to actually post replies (be careful!)
        # for comment in target_comments[:1]:  # Only reply to first one
        #     reply = bot.create_emacs_cat_reply(comment)
        #     bot.post_reply(comment['id'], reply)
        #     break  # Only post one reply for safety
        
        print(f"\n🎉 Analysis complete! Found {len(target_comments)} potential replies.")
        print("💡 Uncomment the posting code to actually reply to comments.")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 