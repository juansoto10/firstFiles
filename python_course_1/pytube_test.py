from pytube import YouTube

link='https://www.youtube.com/watch?v=C7OQHIpDlvA'
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()