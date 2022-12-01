# import socket
# import numpy as np
# host = "localhost"
# port = 8765
# def recv(host = '',port = 0):
#     clientRecv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     clientRecv.connect((host, port))
#     #接收服务端返回的数据
#     while True:
#         msg = clientRecv.recv(1024)
#         print("接收：", msg.decode("utf-8"))
# recv(host,port)





import asyncio
import json

import websockets
import urllib.parse
import urllib.request
import time


# def sendPosition(data = ''):
#     data = bytes(urllib.parse.urlencode({'username': '机场专有终端06', 'password': '123456'}), encoding='utf8')
#     print(data)
#     response = urllib.request.urlopen('http://61.240.144.70:5604/api/apiLogin', data=data)
#     print(response.read())
import asyncio
import websockets

post_data = {
    "type": "location",
    "serial": 1231,
    "deviceID": "Z31446409000925",
    "lat": 40.90785361164368,
    "lng": 115.46692175501954,
    "h": 1635,
    "z": 1635,
    "floor": 2,
    "x": 4531475.533,
    "y": 370798.955,
    "positionType": 1,
    "power": 56
}

# -*-coding:utf-8-*-

import asyncio
import websockets
import json



async def send_data():
    uri = "ws://61.240.144.73:8080"
    async with websockets.connect(uri) as websocket:
        while True:
            post_data['lng'] -= 0.000001
            post_data['y'] -= 0.1
            print(bytes(json.dumps(post_data, ensure_ascii=False).encode("utf-8")))
            await websocket.send(bytes(json.dumps(post_data, ensure_ascii=False).encode("utf-8")))
            greeting = await websocket.recv()
            print(greeting)
            time.sleep(1)


loop = asyncio.get_event_loop()
loop.run_until_complete(send_data())
loop.close()
