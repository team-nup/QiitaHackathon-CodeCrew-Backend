from fastapi import FastAPI, WebSocket
from typing import Dict, Set
from websoket.room_operations import websocket_endpoint

app = FastAPI()

room_websockets: Dict[str, Set[WebSocket]] = {}


@app.websocket("/public/{room_name}")
async def websocket_handler_wrapper(websocket: WebSocket, room_name: str):
    await websocket_endpoint(websocket, room_name)