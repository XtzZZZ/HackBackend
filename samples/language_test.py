import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.studio.nebius.ai/v1/",
    #api_key=os.environ.get("NEBIUS_API_KEY"),
    api_key="eyJhbGciOiJIUzI1NiIsImtpZCI6IlV6SXJWd1h0dnprLVRvdzlLZWstc0M1akptWXBvX1VaVkxUZlpnMDRlOFUiLCJ0eXAiOiJKV1QifQ.eyJzdWIiOiJnb29nbGUtb2F1dGgyfDExNzgwNTMzMzMxMDk2MzUzMjIzMSIsInNjb3BlIjoib3BlbmlkIG9mZmxpbmVfYWNjZXNzIiwiaXNzIjoiYXBpX2tleV9pc3N1ZXIiLCJhdWQiOlsiaHR0cHM6Ly9uZWJpdXMtaW5mZXJlbmNlLmV1LmF1dGgwLmNvbS9hcGkvdjIvIl0sImV4cCI6MTg5NDg3ODU5NSwidXVpZCI6IjAzODNhYjA1LWQ4ZmEtNGZkMS1hMWZiLWIwZWJjNTNmNjUzZiIsIm5hbWUiOiJuZWJpdXNfYXBpIiwiZXhwaXJlc19hdCI6IjIwMzAtMDEtMTdUMTE6MDk6NTUrMDAwMCJ9.Wak3-W2Tv4k3BpmEOs6Tdv1EkldUwNlYUTzor36tRaY",
)

completion = client.chat.completions.create(
  #model="meta-llama/Meta-Llama-3.1-70B-Instruct",
  #model="meta-llama/Llama-3.2-1B-Instruct",
  #model="meta-llama/Llama-3.2-3B-Instruct",
  #model="meta-llama/Meta-Llama-3.1-8B-Instruct",
  #model="meta-llama/Meta-Llama-3.1-70B-Instruct",
  #model="meta-llama/Meta-Llama-3.1-405B-Instruct",
  #model="nvidia/Llama-3.1-Nemotron-70B-Instruct-HF",
  #model="mistralai/Mistral-Nemo-Instruct-2407", # +
  #model="mistralai/Mixtral-8x7B-Instruct-v0.1",
  #model="mistralai/Mixtral-8x22B-Instruct-v0.1",
  #model="cognitivecomputations/dolphin-2.9.2-mixtral-8x22b",
  #model="microsoft/Phi-3.5-mini-instruct",
  #model="microsoft/Phi-3.5-MoE-instruct",
  #model="microsoft/Phi-3-mini-4k-instruct",
  #model="microsoft/Phi-3-medium-128k-instruct",
  #model="deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct",
  #model="Qwen/Qwen2.5-1.5B-Instruct",
  #model="Qwen/Qwen2.5-72B-Instruct",
  #model="google/gemma-2-27b-it",
  model="google/gemma-2-9b-it",
  messages=[
    {
        "role": "user",
        #"content": "What is the building at  Museumstraat 1, 1071 XX Amsterdam"
        #"content": "What is the building at  Havenstraat 6, 1075 PR Amsterdam"
        "content" : "What address at GPS location 41.89082166666667 N 12.49277 E"
    }
  ],
  temperature=0.6
)

print(completion.to_json())