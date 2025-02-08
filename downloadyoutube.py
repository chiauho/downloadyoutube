import yt_dlp

# Options for video download (MP4 with subtitles)
video_opts = {
    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
    "write_sub": True,
    "write_auto_sub": True,
    "sub_lang": "en",
    "sub_format": "srt",
    "embed_subs": True
}


# Options for audio download (MP3)
audio_opts = {
    "format": "bestaudio/best",
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192",
    }],
    "outtmpl": "%(title)s.%(ext)s",
}


def download_content(video_url, download_type):
    """
    Downloads content based on the specified type (video or audio)
    """
    try:
        opts = video_opts if download_type == "video" else audio_opts
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([video_url])
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    channel = 1
    while channel == 1:
        try:
            # Ask user for download type
            print("\nWhat would you like to download?")
            print("1. Video (MP4 with subtitles)")
            print("2. Audio only (MP3)")

            while True:
                try:
                    choice = int(input("Enter your choice (1 or 2): "))
                    if choice in [1, 2]:
                        break
                    else:
                        print("Please enter either 1 or 2.")
                except ValueError:
                    print("Please enter a valid number (1 or 2).")

            # Get the URL
            link_of_the_video = input("\nCopy & paste the URL of the YouTube video: ")
            zxt = link_of_the_video.strip()

            # Download based on user choice
            if choice == 1:
                print("\nDownloading video (MP4 with subtitles)...")
                download_content(zxt, "video")
            else:
                print("\nDownloading audio (MP3)...")
                download_content(zxt, "audio")

            # Ask if user wants to continue
            while True:
                try:
                    channel = int(input("\nEnter 1 to download more content\nEnter 0 to exit: "))
                    if channel in [0, 1]:
                        break
                    else:
                        print("Please enter either 0 or 1.")
                except ValueError:
                    print("Please enter a valid number (0 or 1).")

        except Exception as e:
            print(f"An error occurred: {e}")
            channel = 0  # Exit the program if an unexpected error occurs


if __name__ == "__main__":
    main()
