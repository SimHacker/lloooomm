#!/usr/bin/env python3
import click
import os
import tempfile
import json
from pathlib import Path
from .downloader import download_audio, download_metadata, download_comments
from .transcriber import transcribe_audio
from .formatter import format_output
from .cleaner import clean_long_transcript
from .trimmer import trim_audio
from .video_utils import compress_video, extract_audio
from pytube import Playlist, YouTube
from .uploader import upload_video
import yaml

@click.group()
def cli():
    """A tool to fetch YouTube metadata and transcribe local videos for the lloooomm project."""
    pass

@cli.command(name="fetch-meta")
@click.option('--url', help='URL of a single YouTube video.')
@click.option('--playlist-url', help='URL of the YouTube playlist.')
@click.option('--output-dir', '-o', default='.', help='Base directory to save the data.')
@click.option('--youtube-api-key', envvar='YOUTUBE_API_KEY', help='YouTube Data API v3 key. Can also be set with YOUTUBE_API_KEY env var.')
def fetch_meta_command(url, playlist_url, output_dir, youtube_api_key):
    """Fetches metadata and comments from YouTube and creates the directory structure."""
    if not url and not playlist_url:
        raise click.UsageError("Must provide --url or --playlist-url.")
    
    if playlist_url:
        click.echo(f"Fetching playlist metadata from: {playlist_url}")
        pl = Playlist(playlist_url)
        playlist_title = get_safe_filename(pl.title)
        base_dir = Path(output_dir) / playlist_title
        base_dir.mkdir(parents=True, exist_ok=True)
        click.echo(f"Creating directories in: {base_dir}")
        for video_url in pl.video_urls:
            fetch_single_video_meta(video_url, base_dir, youtube_api_key)
    elif url:
        fetch_single_video_meta(url, Path(output_dir), youtube_api_key)

def fetch_single_video_meta(url, base_dir, api_key):
    try:
        click.echo(f"-> Fetching metadata for {url}")
        metadata = download_metadata(url)
        video_title = get_safe_filename(metadata['title'])
        video_dir = base_dir / video_title
        video_dir.mkdir(parents=True, exist_ok=True)

        # Save JSON metadata
        metadata_path = video_dir / 'metadata.json'
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        click.echo(f"  📝 Saved metadata.json to {video_dir}")
        
        # Download and save comments
        comments = download_comments(metadata['video_id'], api_key)
        if comments is not None:
            comments_path = video_dir / 'comments.json'
            with open(comments_path, 'w', encoding='utf-8') as f:
                json.dump(comments, f, indent=2, ensure_ascii=False)
            click.echo(f"  💬 Saved {len(comments)} comments to {comments_path}")

        # Create lloooomm.yml manifest
        lloooomm_manifest = {
            'source_youtube_url': url,
            'title': metadata['title'],
            'description': metadata['description'],
            'local_video_path': 'PLACEHOLDER: Add your local .mov or .mp4 file here',
            'transcript_vtt_path': None,
            'characters_present': [],
            'key_concepts': [],
            'emotional_arc': [],
            'annotations': []
        }
        manifest_path = video_dir / 'lloooomm.yml'
        with open(manifest_path, 'w', encoding='utf-8') as f:
            yaml.dump(lloooomm_manifest, f, default_flow_style=False, sort_keys=False)
        click.echo(f"  ✨ Created lloooomm.yml in {video_dir}")

    except Exception as e:
        click.echo(f"❌ Failed to fetch metadata for {url}: {e}", err=True)

@cli.command(name="transcribe-local")
@click.argument('path', type=click.Path(exists=True))
@click.option('--model', '-m', default='large', help='Whisper model size.')
@click.option('--language', '-l', help='Language code.')
@click.option('--clean/--no-clean', 'clean_transcript', default=True, help='Clean transcript using LLM.')
@click.option('--llm-model', default='claude-3-5-sonnet-20240620', help='LLM model for cleaning.')
@click.option('--cleaning-style', default='presentation', help='Style of cleaning.')
@click.option('--force', is_flag=True, help='Force re-transcription even if transcript exists.')
def transcribe_local_command(path, **kwargs):
    """
    Transcribes local video files in a specified directory structure.
    
    Can be run on a single video directory or a parent playlist directory
    to process all missing transcriptions.
    """
    path = Path(path)
    if (path / 'lloooomm.yml').is_file(): # It's a single video directory
        process_local_video_dir(path, **kwargs)
    elif path.is_dir(): # It's a playlist directory
        click.echo(f"Scanning directory for videos to transcribe: {path}")
        for video_dir in sorted(path.iterdir()):
            if video_dir.is_dir() and (video_dir / 'lloooomm.yml').is_file():
                process_local_video_dir(video_dir, **kwargs)

def process_local_video_dir(video_dir, force, **kwargs):
    click.echo("\n" + "="*50)
    click.echo(f"Processing directory: {video_dir}")
    manifest_path = video_dir / 'lloooomm.yml'
    
    with open(manifest_path, 'r') as f:
        manifest = yaml.safe_load(f)

    vtt_path_str = manifest.get('transcript_vtt_path')
    if vtt_path_str and Path(vtt_path_str).exists() and not force:
        click.echo("✅ Transcript already exists. Skipping.")
        return

    local_video_path_str = manifest.get('local_video_path')
    local_video_path = find_video_file(video_dir)

    if not local_video_path:
        click.echo(f"⚠️  No video file (.mp4, .mov) found in {video_dir}. Skipping.")
        return
        
    if local_video_path_str == 'PLACEHOLDER' or local_video_path_str != str(local_video_path):
         manifest['local_video_path'] = str(local_video_path)
        
        with tempfile.TemporaryDirectory() as temp_dir:
        # The downloader now handles its own temp/output logic
        audio_path, _, video_path = download_audio(str(local_video_path), str(video_dir), download_video=True)
        
        click.echo(f"🎙️  Transcribing with {kwargs['model']} model...")
        result = transcribe_audio(audio_path, kwargs.get('model'), kwargs.get('language'))
        
        output_path = video_dir / f"{video_dir.name}.vtt"
        process_transcription(result, str(output_path), 'vtt', **kwargs)

        # Update manifest
        manifest['transcript_vtt_path'] = str(output_path)
        with open(manifest_path, 'w') as f:
            yaml.dump(manifest, f, default_flow_style=False, sort_keys=False)
        click.echo(f"✨ Updated lloooomm.yml with transcript path.")

def find_video_file(directory: Path):
    """Finds the first .mp4 or .mov file in a directory."""
    for ext in ('.mp4', '.mov'):
        for file in directory.glob(f'*{ext}'):
            return file
    return None

def get_safe_filename(title, max_length=100):
    """Create a safe, shortened, snake_cased filename from a title."""
    if not title:
        return "untitled"
    # Remove special characters
    safe_title = "".join(c for c in title if c.isalnum() or c.isspace()).strip()
    # Replace spaces with underscores
    snake_cased = "_".join(safe_title.split())
    # Truncate to max_length
    return snake_cased[:max_length]

def process_transcription(result, output, output_format, clean_transcript, llm_model, cleaning_style, **kwargs):
    """Helper function to process and save the transcription results."""
        output_path = Path(output)

        # Clean transcript if requested
        final_result = result
        if clean_transcript:
            click.echo(f"🧹 Cleaning transcript with {llm_model}...")
            raw_text = result['text']
            cleaned_text = clean_long_transcript(raw_text, llm_model, cleaning_style)
            
            if cleaned_text:
                final_result = result.copy()
                final_result['text'] = cleaned_text
            if 'segments' in result: final_result['segments'] = result['segments']
            else:
            click.echo("⚠️  Cleaning failed, using original transcript.")
        
        # Format and save final output
            formatted_output = format_output(final_result, output_format)
    with open(output_path, 'w', encoding='utf-8') as f:
                f.write(formatted_output)

    click.echo(f"✅ Transcription saved to: {output_path}")

@cli.command(name="upload")
@click.argument('video_dir', type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.option('--playlist-id', required=True, help='The ID of the YouTube playlist to add the video to.')
@click.option('--privacy', type=click.Choice(['public', 'private', 'unlisted']), default='private', help='Privacy status of the video.')
def upload_command(video_dir, playlist_id, privacy):
    """Uploads a processed video directory to YouTube."""
    video_dir = Path(video_dir)
    video_title = video_dir.name
    
    video_file = video_dir / f"{video_title}.mp4"
    metadata_file = video_dir / "metadata.json"
    
    if not video_file.exists():
        raise click.UsageError(f"Video file not found: {video_file}")
    if not metadata_file.exists():
        raise click.UsageError(f"Metadata file not found: {metadata_file}")

    click.echo(f"Preparing to upload from {video_dir}")
    upload_video(str(video_file), str(metadata_file), playlist_id, privacy)

if __name__ == '__main__':
    cli()