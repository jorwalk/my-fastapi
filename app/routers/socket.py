import json
import base64
import time
import re
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request, Cookie, Depends, FastAPI, Query, WebSocket, WebSocketDisconnect, status
from typing import Optional, List
from io import BytesIO
from PIL import Image
from fastapi import APIRouter
from typing import List

router = APIRouter()


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


templates = Jinja2Templates(directory='app/templates')


@router.get("/socket", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse("base.html", {"request": request, "id": id})


def getI420FromBase64(codec, image_path="./app/static/img/"):
    base64_data = re.sub('^data:image/.+;base64,', '', codec)
    byte_data = base64.b64decode(base64_data)
    image_data = BytesIO(byte_data)
    img = Image.open(image_data)
    t = time.time()
    url = image_path + str(t) + '.png'
    img.save(url, "PNG")
    return url


@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            json_data = json.loads(data)
            image = json_data.get('result')
            filepath = getI420FromBase64(image).replace('/app', '')
            response = {
                'message': 'file',
                'path': filepath
            }
            await manager.send_personal_message(json.dumps(response), websocket)
            await manager.broadcast(json.dumps({
                'message': 'text',
                'response': f"Client #{client_id} add a new photo",
                'path': filepath
            }))

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")
