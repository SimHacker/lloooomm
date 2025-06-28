import ffmpeg
import click

def compress_video(input_path: str, output_path: str):
    """
    Compresses a video to a web-friendly H.264 MP4 format.
    """
    click.echo(f"⚙️  Compressing video: {input_path}")
    try:
        (
            ffmpeg
            .input(input_path)
            .output(output_path, vcodec='libx264', crf=23, preset='fast', acodec='aac', strict='experimental')
            .overwrite_output()
            .run(quiet=True)
        )
        click.echo(f"✅ Video compressed to: {output_path}")
    except ffmpeg.Error as e:
        raise RuntimeError(f"FFmpeg compression failed: {e.stderr.decode()}") from e

def extract_audio(input_path: str, output_path: str):
    """
    Extracts audio from a video file and saves it as an MP3.
    """
    click.echo(f"🎵 Extracting audio from: {input_path}")
    try:
        (
            ffmpeg
            .input(input_path)
            .output(output_path, acodec='libmp3lame', audio_bitrate='192k', ar=44100)
            .overwrite_output()
            .run(quiet=True)
        )
        click.echo(f"✅ Audio extracted to: {output_path}")
    except ffmpeg.Error as e:
        raise RuntimeError(f"FFmpeg audio extraction failed: {e.stderr.decode()}") from e 