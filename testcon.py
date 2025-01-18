import asyncio
import websockets
import json

async def test_websocket():
    uri = "ws://127.0.0.1:8000/ws/chat/"  # Update this if your WebSocket URL is different
    print("rrr")
    async with websockets.connect(uri) as websocket:
        print("Connected to WebSocket server")

        # Send a message to the server
        message = json.dumps({"message": "Hello, WebSocket!"})
        await websocket.send(message)
        print(f"Sent: {message}")

        # Receive a response
        response = await websocket.recv()
        print(f"Received: {response}")

# Run the WebSocket test
asyncio.run(test_websocket())
