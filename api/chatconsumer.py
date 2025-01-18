import base64
import json
from channels.generic.websocket import AsyncWebsocketConsumer
import GPT

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """Handle a new WebSocket connection."""
        await self.accept()
        await self.send(json.dumps({"message": "WebSocket connected!"}))

    async def receive(self, text_data):
        """Handle incoming messages from WebSocket."""
        data = json.loads(text_data)
        base64_image = data["image"]  # Extract Base64 image data

        resp = await self.process_with_gpt(base64_image)
        await self.send(json.dumps({"message": resp}))

    @staticmethod
    async def process_with_gpt(base64_image):
        """Call your external ChatGPT package to process the image."""
        try:
            response = GPT.process_image(base64_image)
            return response
        except Exception as e:
            print(f"Error processing image with ChatGPT: {e}")
            return {"error": str(e)}

    async def disconnect(self, close_code):
        """Handle WebSocket disconnection."""
        print(f"WebSocket closed with code {close_code}")
