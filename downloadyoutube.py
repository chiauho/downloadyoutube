import yt_dlp

# Updated options to include subtitles
ydl_opts = {
    "format": "mp4",
    "write_sub": True,  # Download subtitles if available
    "write_auto_sub": True,  # Download auto-generated subtitles if no manual ones exist
    "sub_lang": "en",  # Specify subtitle language (e.g., English)
    "sub_format": "srt",  # Subtitle format (e.g., srt, vtt)
    "embed_subs": True  # Embed subtitles into the video file
}


def dwl_vid(video_url):
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
    except Exception as e:
        print(f"An error occurred: {e}")


channel = 1
while channel == 1:
    try:
        link_of_the_video = input("Copy & paste the URL of the YouTube video you want to download: ")
        zxt = link_of_the_video.strip()

        dwl_vid(zxt)

        # Validate user input for continuation
        channel = int(input("Enter 1 if you want to download more videos\nEnter 0 if you are done: "))
    except ValueError:
        print("Invalid input! Please enter 1 or 0.")
