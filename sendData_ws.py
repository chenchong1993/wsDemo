#!/usr/bin/python
import json
import time

def startWs(uri):
    from websocket import create_connection
    return create_connection(uri)

if __name__ == "__main__":


    # ws = startWs("ws://127.0.0.1:8282/?topic=10086")
    # ws = startWs("ws://192.168.153.129/ws/?topic=10086")
    # ws = startWs("ws://60.205.57.192:8282/?topic=10086")
    # ws = startWs("ws://60.205.57.192:8282/?type=box")
    ws = startWs("wss://60.205.57.192/pos-server/websocket/rxd/ws/sendFastLocationData")
    file_object = open('absolute_0(2).txt', 'r')
    try:
        for line in file_object:
            print(line.split()[1])
            position = {}
            position['type'] = 'fastlocation'
            position['time'] = time.time()
            data = []
            point = {}
            point['name'] = 'lidar'
            point['lat'] = line.split()[1]
            point['lng'] = line.split()[2]
            data.append(point)
            position['data'] = data

            ws.send(json.dumps(position, ensure_ascii=False))
            time.sleep(0.01)
    finally:
        file_object.close()

    # file_object = open('gnss0(2).txt', 'r')
    # try:
    #     for line in file_object:
    #         print(line.split()[1])
    #         position = {}
    #         position['type'] = 'fastlocation'
    #         position['time'] = time.time()
    #         data = []
    #         point = {}
    #         point['name'] = 'lidar11'
    #         point['lat'] = line.split()[1]
    #         point['lng'] = line.split()[2]
    #         data.append(point)
    #         position['data'] = data
    #
    #         ws.send(json.dumps(position, ensure_ascii=False))
    #         time.sleep(0.01)
    # finally:
    #     file_object.close()





