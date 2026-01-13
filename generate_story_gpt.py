from openai import OpenAI
import os, json

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

topic = open("scripts/input.txt", encoding="utf-8").read()

prompt = f"""
Create a YouTube Short story in Hindi on topic: {topic}

Return ONLY valid JSON in this format:
{{
"title": "...",
"scenes":[
  {{"narration_text":"...", "image_prompt":"...", "duration_seconds":5}},
  ...
]
}}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user","content":prompt}]
)

story = response.choices[0].message.content
open("story.json","w",encoding="utf-8").write(story)
print("AI story created")
