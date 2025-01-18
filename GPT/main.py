import base64

from dotenv import load_dotenv
from openai import OpenAI
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct the correct path to prompt.txt
prompt_path = os.path.join(BASE_DIR, "prompt.txt")


load_dotenv()


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def process_image(image):
    client = OpenAI(
        base_url = "https://api.openai.com/v1/"
    )

    with open(prompt_path, 'r') as file:
        prompt = file.read()

    completion = client.chat.completions.create(
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
        top_p=1
    )

    response = ""
    for chunk in completion:
        if len(chunk) > 0 and chunk[0] == 'choices':
            response += chunk[1][0].message.content

    return response


if __name__ == "__main__":
    image_path = "../rad.jpg"
    image = encode_image(image_path)
    process_image(image)
