
import json, requests, os

story = json.load(open("story.json", encoding="utf-8"))
os.makedirs("images", exist_ok=True)

for i, scene in enumerate(story["scenes"], start=1):
    prompt = scene["image_prompt"].replace(" ", "%20")
    url = f"https://image.pollinations.ai/prompt/{prompt}?width=1024&height=1024"
    img = requests.get(url).content
    open(f"images/scene_{i}.png","wb").write(img)

print("Images generated using Pollinations AI")
