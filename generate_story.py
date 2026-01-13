import json

story = {
  "title": "क्षमाभाव – जैन धर्म की शक्ति",
  "scenes": [
    {
      "narration_text": "जैन धर्म में क्षमा को सबसे बड़ा धर्म माना गया है।",
      "image_prompt": "peaceful Jain monk meditating, white robes, soft golden light, spiritual atmosphere",
      "duration_seconds": 5
    },
    {
      "narration_text": "क्षमा हमारे अहंकार को समाप्त करती है।",
      "image_prompt": "lotus flower on calm water, sunrise, spiritual, cinematic",
      "duration_seconds": 5
    },
    {
      "narration_text": "जो क्षमा करता है वही सच्चा विजेता है।",
      "image_prompt": "bright sunrise behind mountain temple, peaceful, spiritual",
      "duration_seconds": 5
    }
  ]
}

with open("story.json", "w", encoding="utf-8") as f:
    json.dump(story, f, ensure_ascii=False, indent=2)

print("Local story.json created successfully")
