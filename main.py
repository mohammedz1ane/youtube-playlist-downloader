import pytube
import os
import logging
import string
import re

def sanitize_filename(filename):
    # Replace invalid characters with an underscore (_)
    invalid_chars = re.compile('[/\\\\:*?"<>|]')
    filename = invalid_chars.sub('_', filename)

    # Remove leading and trailing whitespace and replace consecutive whitespace with a single underscore
    filename = re.sub(r'\s+', '_', filename).strip()

    # Replace consecutive underscores with a single underscore
    filename = re.sub(r'_+', '_', filename)

    return filename

def download_video(url, download_path="Download"):
    try:
        # Create a YouTube object from the URL
        youtube = pytube.YouTube(url)

        # Ensure the download path exists
        os.makedirs(download_path, exist_ok=True)

        # Sanitize the video title
        sanitized_title = sanitize_filename(youtube.title)

        # Set the download file path
        file_path = os.path.join(download_path, sanitized_title)

        # Download the video
        youtube.streams.get_highest_resolution().download(file_path)
        logging.info(f"{youtube.title} downloaded successfully.")
        print(f"{youtube.title} downloaded successfully.")
    except Exception as e:
        # Handle exceptions
        logging.error(f"{youtube.title} could not be downloaded: {e}")
        print(f"{youtube.title} could not be downloaded: {e}")

def download_playlist(url, download_path="Download"):
    try:
        # Create a Playlist object from the URL
        playlist = pytube.Playlist(url)

        # Iterate through each video in the playlist
        for video in playlist.videos:
            download_video(video.watch_url, download_path)
    except Exception as e:

        logging.error(f"The playlist could not be downloaded: {e}")
        print(f"The playlist could not be downloaded: {e}")

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO)

download_type = input("Do you want to download a video or a playlist? (1-video/2-playlist): ")

if download_type.lower() == "1":

    video_url = input("Enter Video URL: ")
    download_video(video_url)
elif download_type.lower() == "2":

    playlist_url = input("Enter Playlist URL: ")
    download_playlist(playlist_url)
else:
    print("Invalid input. Please enter '1'for video or '2'for playlist.")
