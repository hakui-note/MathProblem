import io
import os

# pip install google-cloud-vision
from google.cloud import vision
from google.cloud.vision import types

# 認証情報を環境変数から読み込む
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'Downloads/reflecting-node-298502-bdb17399bf03.json'

# 画像を読み込む
with io.open('path/to/image.jpg', 'rb') as image_file:
    content = image_file.read()

# Vision APIのクライアントを作成する
client = vision.ImageAnnotatorClient()

# 画像をVision APIに送信してラベルを取得する
image = types.Image(content=content)
response = client.label_detection(image=image)
labels = response.label_annotations

# 取得したラベルを表示する
for label in labels:
    print(label.description)
