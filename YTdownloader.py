from pytube import YouTube
from sys import argv
link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("Age Restricted: ", yt.age_restricted)
print("View: ", yt.views)
print("Link To Channel: ", yt.channel_url)
print("Publisher: ", yt.author)
print("Day Of Being Publised: ", yt.publish_date)
yd = yt.streams.get_highest_resolution()

yd.download('downloads')
