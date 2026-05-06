import yt_dlp
import sys

def get_youtube_link(url, quality):
    ydl_opts = {
        'format': f'best[height<={quality}]',
        'quiet': True,
        'no_warnings': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            direct_url = info.get('url')
            
            print(f"VIDEO_TITLE: {info.get('title', 'Unknown')}")
            print(f"VIDEO_URL: {direct_url}")
            return direct_url
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return None

if __name__ == "__main__":
    # لینک فیلم و کیفیت رو اینجا عوض کن
    VIDEO_LINK = "https://youtu.be/lXlc1IWHX6Q"  # <-- لینک خودتو اینجا بذار
    QUALITY = 720  # یا 480
    
    get_youtube_link(VIDEO_LINK, QUALITY)
