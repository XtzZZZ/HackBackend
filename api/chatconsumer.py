import base64
import json
from channels.generic.websocket import AsyncWebsocketConsumer
import GPT

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """Handle a new WebSocket connection."""
        await self.accept()
        await self.send(json.dumps({"status": "connected"}))

    async def receive(self, text_data):
        """Handle incoming messages from WebSocket."""
        data = json.loads(text_data)
        base64_image = data["image"]  # Extract Base64 image data
        address = data["address"]  # Extract Base64 image data

        try:
            await GPT.process_image(self, base64_image, address)
            return {}
        except Exception as e:
            print(f"Error processing image with ChatGPT: {e}")
            self.send(json.dumps({"error": {"error": str(e)}})) 

    async def disconnect(self, close_code):
        """Handle WebSocket disconnection."""
        print(f"WebSocket closed with code {close_code}")
