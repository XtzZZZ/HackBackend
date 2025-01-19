import base64

from dotenv import load_dotenv
from openai import OpenAI
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct the correct path to prompt.txt
prompt_path = os.path.join(BASE_DIR, "prompt.txt")


load_dotenv()

client = OpenAI()

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

async def process_image(image, ws):
    with open(prompt_path, 'r') as file:
        prompt = file.read()

    stream = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{image}"},
                    },
                ],
            }
        ],
        temperature=0.9,
        top_p=1,
        stream=True 
    )

    for chunk in stream:
        await ws.send(json.dumps({"message": chunk.choices[0].delta.content or ""}))

if __name__ == "__main__":
    image_path = "../rad.jpg"
    image = encode_image(image_path)
    process_image(image)
