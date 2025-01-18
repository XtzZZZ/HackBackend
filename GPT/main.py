import json
import os
import websocket
from openai import OpenAI
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# url = "wss://api.openai.com/v1/realtime?model=gpt-4o-realtime-preview-2024-12-17"
# headers = [
#     "Authorization: Bearer " + OPENAI_API_KEY,
#     "OpenAI-Beta: realtime=v1"
# ]
#
# def on_open(ws):
#     print("Connected to server.")
#
# def on_message(ws, message):
#     data = json.loads(message)
#     print("Received event:", json.dumps(data, indent=2))
#
# ws = websocket.WebSocketApp(
#     url,
#     header=headers,
#     on_open=on_open,
#     on_message=on_message,
# )
#
# ws.run_forever()
#
# # def sendGPTRequest(image, address: str):

def process_image(image):
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
    pass
    # sendGPTRequest("../bsa.jpg")
