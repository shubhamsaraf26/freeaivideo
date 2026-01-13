import requests, json, os, time

HF_API_TOKEN = os.environ.get("HF_API_TOKEN", "")
headers = {"Authorization": f"Bearer {HF_API_TOKEN}"} if HF_API_TOKEN else {}

prompt = open("scripts/input.txt", encoding="utf-8").read()

system_prompt = (
    "Create a YouTube short story in Hindi. "
    "Return ONLY valid JSON in format: "
    "{title:string, scenes:[{narration_text:string, image_prompt:string, duration_seconds:int}]}"
)

full_prompt = system_prompt + "\n\n" + prompt

API_URL = "https://router.huggingface.co/hf-inference/models/mistralai/Mistral-7B-Instruct-v0.2"

payload = {
    "inputs": full_prompt,
    "parameters": {"max_new_tokens": 600}
}

print("Requesting HuggingFace model...")

response = requests.post(API_URL, headers=headers, json=payload)
result = response.json()

# Handle model loading or error
if isinstance(result, dict) and "error" in result:
    print("HuggingFace response:", result["error"])
    print("Waiting 20 seconds and retrying...")
    time.sleep(20)
    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()

# Normal result
if isinstance(result, list) and "generated_text" in result[0]:
    text = result[0]["generated_text"]
else:
    print("Unexpected HuggingFace response:")
    print(result)
    raise Exception("HuggingFace API did not return generated_text")

# Extract JSON from model text
start = text.find("{")
end = text.rfind("}") + 1
json_text = text[start:end]

open("story.json", "w", encoding="utf-8").write(json_text)

print("Story generated successfully using HuggingFace")
