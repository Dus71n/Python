from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('/home/dus71n/Downloads')

/* you can create a bash script to throw it url to download yt videos
#!/bin/bash
cd /home/user/Downloads
python 3 ytdl.py $1
*/
