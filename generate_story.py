import json

# Read full input file
text = open("scripts/input.txt", encoding="utf-8").read()

# Split sections
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

# Narration lines
narration_lines = [line.strip() for line in script_text.splitlines() if line.strip()]

# Scene prompts
scene_prompts = [line.strip() for line in scenes_text.splitlines() if line.strip()]

# Auto-balance durations
scene_count = len(scene_prompts)
default_duration = 30 // scene_count if scene_count else 5

# Build story.json
story = {
    "title": title,
    "description": description,
    "scenes": []
}

for i in range(scene_count):
    scene = {
        "narration_text": narration_lines[i] if i < len(narration_lines) else narration_lines[-1],
        "image_prompt": scene_prompts[i],
        "duration_seconds": default_duration
    }
    story["scenes"].append(scene)

# Save story.json
with open("story.json", "w", encoding="utf-8") as f:
    json.dump(story, f, ensure_ascii=False, indent=2)

print("Structured story.json created successfully")