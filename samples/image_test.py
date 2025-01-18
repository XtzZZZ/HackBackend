from openai import OpenAI
import os
import base64


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


# Path to your image
#image_path = "demo.jpeg"
#image_path = "rijksmuseum.jpeg"
image_path = "bsa.jpg"
#image_path = "bsa1.png"
#image_path = "rijskmuseum1.png"

# Getting the base64 string
base64_image = encode_image(image_path)


def get_response():
    client = OpenAI(
        #api_key=os.getenv("DASHSCOPE_API_KEY"),
        api_key="eyJhbGciOiJIUzI1NiIsImtpZCI6IlV6SXJWd1h0dnprLVRvdzlLZWstc0M1akptWXBvX1VaVkxUZlpnMDRlOFUiLCJ0eXAiOiJKV1QifQ.eyJzdWIiOiJnb29nbGUtb2F1dGgyfDExNzgwNTMzMzMxMDk2MzUzMjIzMSIsInNjb3BlIjoib3BlbmlkIG9mZmxpbmVfYWNjZXNzIiwiaXNzIjoiYXBpX2tleV9pc3N1ZXIiLCJhdWQiOlsiaHR0cHM6Ly9uZWJpdXMtaW5mZXJlbmNlLmV1LmF1dGgwLmNvbS9hcGkvdjIvIl0sImV4cCI6MTg5NDg3ODU5NSwidXVpZCI6IjAzODNhYjA1LWQ4ZmEtNGZkMS1hMWZiLWIwZWJjNTNmNjUzZiIsIm5hbWUiOiJuZWJpdXNfYXBpIiwiZXhwaXJlc19hdCI6IjIwMzAtMDEtMTdUMTE6MDk6NTUrMDAwMCJ9.Wak3-W2Tv4k3BpmEOs6Tdv1EkldUwNlYUTzor36tRaY",
        base_url="https://api.studio.nebius.ai/v1/"
    )
    completion = client.chat.completions.create(
        model="Qwen/Qwen2-VL-7B-Instruct",
        #model="Qwen/Qwen2-VL-72B-Instruct",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What is this?"},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                    {"type": "text", "text": "Havenstraat 6, 1075 PR Amsterdam"},

                ],
            }
        ],
        top_p=0.8,
        stream=True,
        stream_options={"include_usage": True},
    )
    for chunk in completion:
        if len(chunk.choices) > 0:
            print(chunk.choices[0].delta.content, end="")
        #print(chunk.model_dump_json())


if __name__ == "__main__":
    get_response()
