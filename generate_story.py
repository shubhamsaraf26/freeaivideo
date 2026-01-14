import json, os, shutil

STORY_DIR = "scripts/stories"
PROCESSED_DIR = "scripts/processed"

os.makedirs(PROCESSED_DIR, exist_ok=True)

# Pick first unprocessed story file
story_files = sorted([f for f in os.listdir(STORY_DIR) if f.endswith(".txt")])

if not story_files:
    raise Exception("No new story files found in scripts/stories")

story_file = story_files[0]
story_path = os.path.join(STORY_DIR, story_file)

print("Using story file:", story_file)

text = open(story_path, encoding="utf-8").read()

def get_section(name, text):
    start = text.find(name + ":")
    if start == -1:
        return ""
    start += len(name) + 1
    end = text.find("\n\n", start)
    return text[start:end].strip() if end != -1 else text[start:].strip()

title = get_section("TITLE", text)
description = get_section("DESCRIPTION", text)
script_text = get_section("SCRIPT", text)
scenes_text = get_section("SCENES", text)

narration_lines = [l.strip() for l in script_text.splitlines() if l.strip()]
scene_prompts = [l.strip() for l in scenes_text.splitlines() if l.strip()]

scene_count = len(scene_prompts)
default_duration = max(3, 30 // scene_count)

story = {
    "title": title,
    "description": description,
    "scenes": []
}

for i in range(scene_count):
    story["scenes"].append({
        "narration_text": narration_lines[i] if i < len(narration_lines) else narration_lines[-1],
        "image_prompt": scene_prompts[i],
        "duration_seconds": default_duration
    })

# Save story.json for rest of pipeline
with open("story.json", "w", encoding="utf-8") as f:
    json.dump(story, f, ensure_ascii=False, indent=2)

# Move processed story file
shutil.move(story_path, os.path.join(PROCESSED_DIR, story_file))

print("story.json created and story file moved to processed/")