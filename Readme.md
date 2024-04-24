Youtube Playlist Downloader
==========================

A simple Python script to download YouTube videos or playlists and save them to a designated folder.

Features
--------

* Download YouTube videos or playlists with a single command.
* Save videos to a specified folder.
* Log download events and errors to a file (app.log).
* Handle invalid characters in video titles to prevent download errors.

Requirements
------------

* Python 3.x
* [pytube](https://pypi.org/project/pytube/) library

A `requirements.txt` file has been included in the project for easy installation of dependencies.

Installation
------------

1. Clone the repository:
```bash
git clone https://github.com/mohammedz1ane/youtube-playlist-downloader.git
```
2. Install the required library using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```
Usage
-----

1. Run the script:
```bash
python3 main.py
```
2. Choose whether you want to download a video or a playlist (1-video/2-playlist).
3. Enter the URL of the video or playlist you want to download.

The script will download the video or playlist and save it to the "Download" folder in the project directory.

Logging
-------

The script logs download events and errors to a file named "app.log" in the project directory.

---