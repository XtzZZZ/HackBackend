import os

from openai import OpenAI


# def sendGPTRequest(image, address: str):
def sendGPTRequest(image):
    assistant_id = "asst_gShRAai0FxG4sHmtfdlS87dx"
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    thread = client.beta.threads.create()

    # message = {
    #    "role": "user",
    #    "content": "Say this is a test",
    # }

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe image"},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"{image}"},
                    },
                ],
            }
        ],
    )

if __name__ == "__main__":
    sendGPTRequest("../bsa.jpg")
