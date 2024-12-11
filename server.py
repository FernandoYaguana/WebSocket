import asyncio
import websockets

async def hello_world(websocket):  # Incluye 'path' como segundo parámetro
    try:
        await websocket.send("Hola Mundo desde WebSocket")
    except Exception as e:
        print(f"Error al enviar el mensaje: {e}")

async def start():
    try:
        # Usa '0.0.0.0' para aceptar conexiones externas
        server = await websockets.serve(hello_world, "0.0.0.0", 8765)
        print("Servidor WebSocket iniciado en ws://0.0.0.0:8765")
        await server.wait_closed()
    except Exception as e:
        print(f"Error al iniciar el servidor WebSocket: {e}")

if __name__ == "__main__":
    asyncio.run(start())