import os
import click
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
CLIENT_SECRETS_FILE = 'client_secrets.json'
TOKEN_FILE = 'token.json'

def get_authenticated_service():
    """Authenticate and return a YouTube API service object."""
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CLIENT_SECRETS_FILE):
                raise FileNotFoundError(
                    f"OAuth secrets file not found at {CLIENT_SECRETS_FILE}. "
                    "Please download it from the Google Cloud Console and place it in the script's directory."
                )
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
            
    return build('youtube', 'v3', credentials=creds)

def upload_video(video_path, metadata_path, playlist_id, privacy_status='private'):
    """Uploads a video to YouTube, adds it to a playlist, and sets metadata."""
    try:
        youtube = get_authenticated_service()
        
        with open(metadata_path, 'r', encoding='utf-8') as f:
            metadata = json.load(f)

        body = {
            'snippet': {
                'title': metadata.get('title', 'Untitled Video'),
                'description': metadata.get('description', ''),
                'tags': metadata.get('keywords', []),
                'categoryId': '22' # 22 = People & Blogs, a reasonable default
            },
            'status': {
                'privacyStatus': privacy_status,
                'selfDeclaredMadeForKids': False,
            }
        }
        
        click.echo(f"⬆️  Uploading video: {video_path}...")
        media = MediaFileUpload(video_path, chunksize=-1, resumable=True)
        
        request = youtube.videos().insert(
            part=','.join(body.keys()),
            body=body,
            media_body=media
        )
        
        response = request.execute()
        video_id = response['id']
        click.echo(f"✅ Video uploaded successfully! Video ID: {video_id}")
        
        if playlist_id:
            click.echo(f"➕ Adding video to playlist: {playlist_id}")
            playlist_item_body = {
                'snippet': {
                    'playlistId': playlist_id,
                    'resourceId': {
                        'kind': 'youtube#video',
                        'videoId': video_id
                    }
                }
            }
            youtube.playlistItems().insert(
                part='snippet',
                body=playlist_item_body
            ).execute()
            click.echo("✅ Video added to playlist.")
            
    except Exception as e:
        click.echo(f"❌ An error occurred during upload: {e}", err=True)
        raise

if __name__ == '__main__':
    click.echo("This module is not meant to be run directly. Use it via main.py's 'upload' command.") 