import click
from pytube import YouTube
import ffmpeg
import os

def download_audio(url, output_dir, start_time=None, end_time=None, download_video=False):
    """
    Downloads audio and optionally video from a YouTube URL.
    Uses pytube to get stream URLs and ffmpeg to process them.
    """
    click.echo(f"Processing URL: {url}")
    yt = YouTube(url)
    video_title = yt.title
    safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).rstrip()

    video_path = None
    if download_video:
        click.echo("📹 Getting video stream...")
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if stream:
            video_path = os.path.join(output_dir, f"{safe_title}.mp4")
            click.echo(f"Downloading video to {video_path}...")
            ffmpeg.input(stream.url).output(video_path, c='copy').overwrite_output().run(quiet=True)
            click.echo("✅ Video download complete.")
        else:
            click.echo("⚠️ No progressive mp4 stream found.")

    click.echo("🎵 Getting audio stream...")
    audio_stream = yt.streams.filter(only_audio=True).first()
    if not audio_stream:
        raise ValueError("No audio stream found.")

    audio_path = os.path.join(output_dir, f"{safe_title}.mp3")
    click.echo(f"Downloading and converting audio to {audio_path}...")
    
    input_options = {}
    if start_time:
        input_options['ss'] = start_time
    
    output_options = {
        'acodec': 'libmp3lame',
        'audio_bitrate': '192k',
    }
    if end_time:
        output_options['to'] = end_time

    ffmpeg.input(audio_stream.url, **input_options).output(audio_path, **output_options).overwrite_output().run(quiet=True)
    click.echo("✅ Audio extraction complete.")
    
    return audio_path, video_title, video_path

def download_metadata(url):
    """Fetches metadata for a YouTube video without downloading the content."""
    try:
        yt = YouTube(url)
        metadata = {
            'video_id': yt.video_id,
            'title': yt.title,
            'author': yt.author,
            'length': yt.length,
            'publish_date': yt.publish_date.isoformat() if yt.publish_date else None,
            'views': yt.views,
            'keywords': yt.keywords,
            'description': yt.description,
            'thumbnail_url': yt.thumbnail_url,
        }
        return metadata
    except Exception as e:
        click.echo(f"Error fetching metadata for {url}: {str(e)}", err=True)
        raise

def download_comments(video_id, api_key):
    """Fetches all comments for a YouTube video using the YouTube Data API."""
    if not api_key:
        click.echo("⚠️  --youtube-api-key not provided. Skipping comment download.", err=True)
        return None

    click.echo("💬 Fetching comments...")
    all_comments = []
    try:
        youtube = build('youtube', 'v3', developerKey=api_key)
        request = youtube.commentThreads().list(
            part='snippet,replies',
            videoId=video_id,
            maxResults=100,
            textFormat='plainText'
        )
        
        while request:
            response = request.execute()
            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']
                all_comments.append({
                    'author': comment['authorDisplayName'],
                    'text': comment['textDisplay'],
                    'published_at': comment['publishedAt'],
                    'like_count': comment['likeCount'],
                    'total_reply_count': item['snippet']['totalReplyCount'],
                    'replies': []
                })
                if 'replies' in item and item['snippet']['totalReplyCount'] > 0:
                    for reply_item in item['replies']['comments']:
                        reply = reply_item['snippet']
                        all_comments[-1]['replies'].append({
                            'author': reply['authorDisplayName'],
                            'text': reply['textDisplay'],
                            'published_at': reply['publishedAt'],
                            'like_count': reply['likeCount'],
                        })
            request = youtube.commentThreads().list_next(request, response)
        
        click.echo(f"✅ Fetched {len(all_comments)} top-level comments.")
        return all_comments

    except Exception as e:
        click.echo(f"❌ Failed to fetch comments: {e}", err=True)
        click.echo("   Please ensure your YouTube Data API v3 key is correct and has the API enabled.", err=True)
        return None