
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials
import os

creds = Credentials(
    None,
    refresh_token=os.environ["YT_REFRESH_TOKEN"],
    token_uri="https://oauth2.googleapis.com/token",
    client_id=os.environ["YT_CLIENT_ID"],
    client_secret=os.environ["YT_CLIENT_SECRET"]
)

youtube = build("youtube", "v3", credentials=creds)

request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": "AI Generated Jainism Short",
            "description": "Fully AI generated video",
            "tags": ["AI", "Jainism", "Shorts"],
            "categoryId": "22"
        },
        "status": {"privacyStatus": "public"}
    },
    media_body=MediaFileUpload("final_video.mp4", mimetype="video/mp4", resumable=True)
)

response = request.execute()
print("Uploaded Video ID:", response["id"])
