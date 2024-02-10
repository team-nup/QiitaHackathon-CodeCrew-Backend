from fastapi import WebSocket
from typing import Dict, Set
from fastapi.websockets import WebSocketDisconnect
import json

room_websockets: Dict[str, Set[WebSocket]] = {}

async def join_room(websocket: WebSocket, room_name: str):
    await websocket.accept()

    if room_name not in room_websockets:
        room_websockets[room_name] = set()
        
    room_websockets[room_name].add(websocket)

async def leave_room(websocket: WebSocket, room_name: str):
    room_websockets[room_name].remove(websocket)
    if not room_websockets[room_name]:
        del room_websockets[room_name]
        
async def send_message(room_name: str, data: dict):
    user_name = data.get("userName")
    message = data.get("message")
    action = data.get("action") # target || message
    
    response_data = {
        "userName": user_name,
        "message": message,
        "action": action
    }
    

    for ws in room_websockets.get(room_name, []):
        await ws.send_text(json.dumps(response_data))

async def websocket_endpoint(websocket: WebSocket, room_name: str,):
    await join_room(websocket, room_name, target)

    try:
        while True:
            data = await websocket.receive_text()
            data = json.loads(data)
            await send_message(room_name, data)
                
    except WebSocketDisconnect:
        await leave_room(websocket, room_name)
