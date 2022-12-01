import asyncio
import websockets
import random

"""实现一直给客户端发消息，异步等待3秒，达到特定要求给客户端发送"""


async def echo(websocket, path):
    x = 0
    y = 10
    while True:

        await websocket.send("{\"name\":\"cc\",\"coord\":[["+str(x)+",10],["+str(x+0.001)+",10]]}")  # 第几个2传过来
        x =x+0.1
        await asyncio.sleep(1)


start_server = websockets.serve(echo, '127.0.0.1', 5678)  # 地址改为你自己的地址
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
