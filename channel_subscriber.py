import google.auth
from googleapiclient.discovery import build

# APIキーを取得
API_KEY = "AIzaSyCoePI37dAeZO6updaP614Reiy48-IbuVg"

# YouTube APIクライアントを作成
youtube = build("youtube", "v3", developerKey=API_KEY)

# チャンネルIDを指定
channel_id_1 = "@Kuzuha"
channel_id_2 = "@YashiroKizuku"

# チャンネルのサブスクライバーを取得
subscribers_1 = set()
subscribers_2 = set()

next_page_token = None
while True:
    # チャンネル1のサブスクライバーを取得
    request = youtube.subscriptions().list(
        part="subscriberSnippet",
        channelId=channel_id_1,
        maxResults=50,
        pageToken=next_page_token
    )
    response = request.execute()
    for item in response["items"]:
        subscriber_id = item["subscriberSnippet"]["channelId"]
        subscribers_1.add(subscriber_id)
    next_page_token = response.get("nextPageToken")
    if not next_page_token:
        break

next_page_token = None
while True:
    # チャンネル2のサブスクライバーを取得
    request = youtube.subscriptions().list(
        part="subscriberSnippet",
        channelId=channel_id_2,
        maxResults=50,
        pageToken=next_page_token
    )
    response = request.execute()
    for item in response["items"]:
        subscriber_id = item["subscriberSnippet"]["channelId"]
        subscribers_2.add(subscriber_id)
    next_page_token = response.get("nextPageToken")
    if not next_page_token:
        break

# 共通の視聴者IDを計算
intersection = subscribers_1.intersection(subscribers_2)

# 視聴者の重複率を計算
overlap_ratio = len(intersection) / (len(subscribers_1) + len(subscribers_2) - len(intersection))

print("視聴者の重複率: {:.2f}%".format(overlap_ratio * 100))
