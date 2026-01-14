import json, os, shutil

STORY_DIR = "scripts/stories"
PROCESSED_DIR = "scripts/processed"

os.makedirs(PROCESSED_DIR, exist_ok=True)

story_files = sorted([f for f in os.listdir(STORY_DIR) if f.endswith(".txt")])

if not story_files:
    raise Exception("No new story files found in scripts/stories")

TOTAL_VIDEO_DURATION = 60   # 1 minute video

def get_section(name, text):
    start = text.find(name + ":")
    if start == -1:
        return ""
    start += len(name) + 1
    end = text.find("\n\n", start)
    return text[start:end].strip() if end != -1 else text[start:].strip()

# -------- Process ALL stories --------
for story_file in story_files:
    story_path = os.path.join(STORY_DIR, story_file)
    print("\nProcessing story file:", story_file)

    text = open(story_path, encoding="utf-8").read()

    title = get_section("TITLE", text)
    description = get_section("DESCRIPTION", text)
    script_text = get_section("SCRIPT", text)
    scenes_text = get_section("SCENES", text)

    narration_lines = [l.strip() for l in script_text.splitlines() if l.strip()]
    scene_prompts = [l.strip() for l in scenes_text.splitlines() if l.strip()]

    if not scene_prompts:
        print("No SCENES found in:", story_file)
        continue

    scene_count = len(scene_prompts)
    default_duration = max(3, TOTAL_VIDEO_DURATION // scene_count)

    # Build story.json
    story = {
        "title": title if title else "AI Generated Short",
        "description": description if description else "AI generated video",
        "scenes": []
    }

    for i in range(scene_count):
        story["scenes"].append({
            "narration_text": narration_lines[i] if i < len(narration_lines) else narration_lines[-1],
            "image_prompt": scene_prompts[i],
            "duration_seconds": default_duration
        })

    # Save story.json (used by other scripts)
    with open("story.json", "w", encoding="utf-8") as f:
        json.dump(story, f, ensure_ascii=False, indent=2)

    print("story.json created for:", story["title"])

    # -------- Run rest of pipeline --------
    os.system("python generate_audio.py")
    os.system("python generate_images.py")
    os.system("python create_video.py")
    os.system("python upload_to_youtube.py")

    # Move processed story file
    shutil.move(story_path, os.path.join(PROCESSED_DIR, story_file))
    print("Moved", story_file, "to scripts/processed/")

print("\nAll stories processed successfully!")