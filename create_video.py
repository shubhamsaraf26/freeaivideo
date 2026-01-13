
from moviepy import ImageClip, AudioFileClip, concatenate_videoclips
import json

story = json.load(open("story.json"))
audio = AudioFileClip("voice.mp3")

clips = []
for i, scene in enumerate(story["scenes"], start=1):
    clip = ImageClip(f"images/scene_{i}.png").with_duration(scene["duration_seconds"]).resized(height=1280)
    clips.append(clip)

video = concatenate_videoclips(clips).with_audio(audio)
video.write_videofile("final_video.mp4", fps=24, codec="libx264", audio_codec="aac")
