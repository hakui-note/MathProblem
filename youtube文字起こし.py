from youtube_transcript_api import YouTubeTranscriptApi

video_id="mmWT5D5A9e0&t=81s&ab_channel=らいとのゆっくり解説"
transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

transcript = transcript_list.find_generated_transcript(['ja'])

#ファイルを開く
f=open("文字起こし.txt",'w',newline='\n')

for d in transcript.fetch():
    #print(d['text'])
    #テキストファイルに書き込み
    f.write(d["text"]+"\n")

f.close()