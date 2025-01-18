import base64
from openai import OpenAI, api_key
import os

from samples.image_test import base64_image

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def process_image(image):
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(

        base_url = "https://api.openai.com/v1/"
    )

    file = open("prompt.txt", 'r')
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
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ],
            }
        ],
        temperature=0.5
    )

    for chunk in completion:
        if len(chunk) > 0 and chunk[0] == 'choices':
            print(chunk[1][0].message.content, end='')


if __name__ == "__main__":
    image_path = "../bsa.jpg"
    image = encode_image(image_path)
    process_image(image)
