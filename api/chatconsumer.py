import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """Handle a new WebSocket connection."""
        await self.accept()
        await self.send(json.dumps({"message": "WebSocket connected!"}))

    async def receive(self, text_data):
        """Handle incoming messages from WebSocket."""
        data = json.loads(text_data)
        print(f"Received message: {data['message']}")

        # Send response back to WebSocket client
        await self.send(json.dumps({"response": f"You said: {data['message']}"}))


    async def disconnect(self, close_code):
        """Handle WebSocket disconnection."""
        print(f"WebSocket closed with code {close_code}")
