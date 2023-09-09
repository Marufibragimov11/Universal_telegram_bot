import random
import yt_dlp
from pytube import YouTube


def name_generator():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"

    string = lower + upper + numbers
    length = 16
    random_name = "".join(random.sample(string, length))
    return random_name


def download_yt(url):
    direction = []
    ydl_opts = {
        # 'format': 'bestvideo[ext=mp4]+bestaudio[ext=mp4]/mp4+best[height<=480]',
        'format': 'best',
        'outtmpl': f"D:/python/Mohirdev/telegram_bot/aiogram/Expences/downloads/{name_generator()}.mp4",
    }
    ydl = yt_dlp.YoutubeDL(ydl_opts)
    ydl.download([url])
    direction.append(ydl_opts['outtmpl'])
    return direction[0]['default']


# download_yt("https://youtu.be/07qgqXRw9dE?si=Ikr4STBsqOUYLB3Z")

# def download_yt(url):
#     yt = YouTube(url)
#     video_stream = yt.streams.get_highest_resolution()
#     output_dir = "D:\\python\\Mohirdev\\telegram_bot\\aiogram\\Expences\\downloads"
#     output_filename = f"{name_generator()}.mp4"
#     video_stream.download(output_path=output_dir, filename=output_filename)
#     return output_filename
#
#
# print(download_yt("https://youtu.be/FuLFuU2BCgU?si=D2TQpF4NoSb6tncB"))
