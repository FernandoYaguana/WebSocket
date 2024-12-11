import asyncio
import websockets

async def test():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = await websocket.recv()
        print(f"Mensaje recibido: {message}")

asyncio.run(test())