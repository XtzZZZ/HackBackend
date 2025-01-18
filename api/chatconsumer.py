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

        # Remove the "data:image/png;base64," prefix
        image_data = base64_image.split(",")[1]

        # Decode Base64 into binary image data
        image_binary = base64.b64decode(image_data)

        # Save it as a file (example: save to 'uploaded_image.png')
        with open("uploaded_image.png", "wb") as f:
            f.write(image_binary)

        await self.send(json.dumps({"response": f"You said: {data['image']}"}))

    async def process_with_gpt(self):
        """Call your external ChatGPT package to process the image."""
        try:
            response = await chatgpt_service.process_image(base64_image)  # ✅ Calls function from your package
            return response  # ✅ Returns the result from ChatGPT
        except Exception as e:
            print(f"Error processing image with ChatGPT: {e}")
            return {"error": "Failed to process image with ChatGPT"}

    async def disconnect(self, close_code):
        """Handle WebSocket disconnection."""
        print(f"WebSocket closed with code {close_code}")
