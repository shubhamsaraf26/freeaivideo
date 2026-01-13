
import json
from gtts import gTTS

story = json.load(open("story.json", encoding="utf-8"))
full_text = " ".join(scene["narration_text"] for scene in story["scenes"])
gTTS(full_text, lang="hi").save("voice.mp3")
print("Audio created")
