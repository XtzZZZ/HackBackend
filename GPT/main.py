import base64

from dotenv import load_dotenv
from openai import AsyncOpenAI
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct the correct path to prompt.txt
prompt_path = os.path.join(BASE_DIR, "prompt.txt")


load_dotenv()

client = AsyncOpenAI()

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

async def process_image(ws, image, address):
    with open(prompt_path, 'r') as file:
        prompt = file.read()

    content = [
        {"type": "text", "text": prompt},
        {
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{image}"},
        },
    ]

    if address:
        content.append({"type": "text", "text": f"The photo was made on {address} address"})

    stream = await client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
        temperature=0.9,
        top_p=1,
        stream=True 
    )

    async for chunk in stream:
        await ws.send(json.dumps({"message": chunk.choices[0].delta.content or ""}))

if __name__ == "__main__":
    image_path = "../rad.jpg"
    image = encode_image(image_path)
    process_image(image)
