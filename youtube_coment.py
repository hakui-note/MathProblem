import requests
import json

# API key
api_key = "AIzaSyCoePI37dAeZO6updaP614Reiy48-IbuVg"

# 動画のID
video_id = "YMxQdHtQFGc"

# API endpoint
url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&key={api_key}"

# APIリクエスト
response = requests.get(url)
data = json.loads(response.text)

comments = []
for comment in data["items"]:
    text = comment["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
    like_count = comment["snippet"]["topLevelComment"]["snippet"]["likeCount"]
    comments.append((text, like_count))

next_page_token = data.get("nextPageToken", None)

# 次のページが存在する場合は繰り返す
while next_page_token:
    url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&key={api_key}&pageToken={next_page_token}"
    response = requests.get(url)
    data = json.loads(response.text)

    for comment in data["items"]:
        comment_text = comment["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        like_count = comment["snippet"]["topLevelComment"]["snippet"]["likeCount"]
        comments.append((comment_text, like_count))

    next_page_token = data.get("nextPageToken", None)

# コメントの「高評価数」順に並び替え
comments = sorted(comments, key=lambda x: x[1], reverse=True)

# ファイルに出力
with open("comments.txt", "w", encoding="utf-8") as f:
    for comment, like_count in comments:
        f.write(f"{comment} ({like_count} likes)\n"+"\n")