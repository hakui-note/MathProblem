import requests

# YouTube Data API endpoint for trending videos
url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&regionCode=JP&maxResults=10&key={API_KEY}'

# Replace {API_KEY} with your actual API key
response = requests.get(url.format(API_KEY='AIzaSyCoePI37dAeZO6updaP614Reiy48-IbuVg'))
data = response.json()

# Loop through the data to get video name and channel ID
for video in data['items']:
    video_name = video['snippet']['title']
    channel_id = video['snippet']['channelId']
    print("Video Name:", video_name)
    print("Channel ID:", channel_id)
    print("---" * 20)

