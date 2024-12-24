
from yt_dlp import YoutubeDL

options = {
    'writeinfojson': True,  
    'outtmpl': '%(title)s.%(ext)s',  
    'nocheckcertificate': True,  
    'ratelimit': 4*1024*1024,
}

with YoutubeDL(options) as ydl:
    print(ydl.search("lol"))
    # ydl.download('https://youtu.be/Ofr6mp8zGNI?si=h5OS5Zci9xbRuRE9')


