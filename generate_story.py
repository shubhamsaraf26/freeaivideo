import json

# Read user input
input_text = open("scripts/input.txt", encoding="utf-8").read()

# Simple rule-based story generator (generic template)
lines = input_text.splitlines()
data = {line.split(":")[0].strip(): line.split(":")[1].strip() for line in lines if ":" in line}

topic = data.get("Topic", "Inspiring Topic")
message = data.get("Message", "An inspiring message")
style = data.get("Style", "calm")
duration = int(data.get("Duration", "30").replace("seconds","").strip())

# Automatically build scenes
story = {
  "title": f"{topic} – Short Story",
  "scenes": [
    {
      "narration_text": f"आज हम जानेंगे {topic} के बारे में।",
      "image_prompt": f"{topic}, cinematic, {style}, high quality illustration",
      "duration_seconds": duration // 3
    },
    {
      "narration_text": message,
      "image_prompt": f"{message}, symbolic scene, {style}, cinematic lighting",
      "duration_seconds": duration // 3
    },
    {
      "narration_text": f"{topic} हमें जीवन में नई दिशा देता है।",
      "image_prompt": f"inspiring ending scene about {topic}, sunrise, hope, cinematic",
      "duration_seconds": duration // 3
    }
  ]
}

# Save story.json
with open("story.json", "w", encoding="utf-8") as f:
    json.dump(story, f, ensure_ascii=False, indent=2)

print("Generic story.json created successfully")