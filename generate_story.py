
import requests, json, os

HF_API_TOKEN = os.environ.get("HF_API_TOKEN", "")
headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}

prompt = open("scripts/input.txt", encoding="utf-8").read()

system_prompt = (
    "Create a YouTube short story in Hindi. "
    "Return ONLY valid JSON in format: "
    "{title:string, scenes:[{narration_text:string, image_prompt:string, duration_seconds:int}]}"
)

full_prompt = system_prompt + "\n\n" + prompt

response = requests.post(
    "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2",
    headers=headers,
    json={"inputs": full_prompt, "parameters": {"max_new_tokens": 600}}
)

result = response.json()
text = result[0]["generated_text"]

start = text.find("{")
end = text.rfind("}") + 1
json_text = text[start:end]

open("story.json","w",encoding="utf-8").write(json_text)
print("Story generated using HuggingFace")
