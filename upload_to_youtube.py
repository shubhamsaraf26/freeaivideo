from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials
import os, json

# --- Load story.json to get dynamic title ---
story = json.load(open("story.json", encoding="utf-8"))
video_title = story.get("title", "AI Generated Short")

# --- YouTube Authentication ---
creds = Credentials(
    None,
    refresh_token=os.environ["YT_REFRESH_TOKEN"],
    token_uri="https://oauth2.googleapis.com/token",
    client_id=os.environ["YT_CLIENT_ID"],
    client_secret=os.environ["YT_CLIENT_SECRET"]
)

youtube = build("youtube", "v3", credentials=creds)

# --- Upload Request ---
request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": video_title,   # ✅ Dynamic title
            "description": "This video was generated automatically using AI",
            "tags": ["AI", "Shorts", "Automation"],
            "categoryId": "22"
        },
        "status": {
            "privacyStatus": "public"
        }
    },
    media_body=MediaFileUpload("final_video.mp4", mimetype="video/mp4", resumable=True)
)

response = request.execute()
print("Uploaded Video ID:", response["id"])
print("Video Title:", video_title)