#!/usr/bin/python
import json
import time

#
import random


def getStaPos(distance,interval):
    staPos = []
    a = list(range(0, distance, interval)) #distance总长度，interval间隔
    for i in a:
        tmp = {}
        tmp['name'] = "sta" + str(int(i/5))
        tmp['power'] = 0
        tmp['loc'] = [i,50]
        tmp['isWork'] = 0
        tmp['workTime'] = 0
        tmp['sleepTime'] = 0
        staPos.append(tmp)
    return staPos

def startWs(uri):
    from websocket import create_connection
    return create_connection(uri)

def getRoute(name,startPoint,time,speed): #一维的
    route = {}
    route['name'] = name
    route['point'] = [time * speed + startPoint, 10]
    return route




if __name__ == "__main__":

    ##################################仿真配置项##########################################################

    # 配置定位频率
    t = 1  # 单位秒,现在是一秒一次
    #仿真路线长度
    distance = 500   #单位是10m，500代表5公里
    #基站部署间隔
    interval = 5     #单位是10m，代表间隔50m一个基站
    #随机速度
    minSpeed = 0
    maxSpeed = 5   #单位10m/s,代表2m/s
    #基站工作时每次消耗功率
    powerForWork = 10
    #基站休眠时每次消耗功率
    powerForSleep = 1


    ##################################仿真配置项##########################################################

    staInfo = getStaPos(distance,interval)
    name = [0,0,0,0,0,0,0,0,0,0]
    for i in range(len(name)):
        name[i] = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    end = [0,0,0,0,0,0,0,0,0,0]


    routeData = {}
    staData = {}




    ws = startWs("ws://60.205.57.192:8282/?type=box")

    while True:
        # strdata = "{\"name\":\"cc\",\"coord\":[["+str(x)+",10]]}"

        # ws.send(strdata)
        routeList = []
        for i in range(10):
            speed = random.uniform(minSpeed,maxSpeed)   #产生随机速度,设置随机速度区间，0-0.2表示0-2m/s以内
            if end[i] > 500 :
                speed = 0
            tmpDic = getRoute(name[i],end[i],t,speed)  #产生随机速度的定位结果
            end[i] = tmpDic['point'][0]
            tmpDic['point'][1] = tmpDic['point'][1]*i+5
            routeList.append(tmpDic)


            for sta in staInfo:
                if abs(end[i] - sta['loc'][0]) <= interval/2:
                    sta['isWork'] = 1
        for sta in staInfo:
            if sta['isWork'] == 1:
                sta['power'] = sta['power'] + powerForWork
                sta['workTime'] = sta['workTime'] + t
            if sta['isWork'] == 0:
                sta['power'] = sta['power'] + powerForSleep
                sta['sleepTime'] = sta['sleepTime'] + t

        print(staInfo)
        routeData['type'] = "userRoute"
        routeData['data'] = routeList
        staData['type'] = "sta"
        staData['data'] = staInfo

        # print(json.dumps(routeList, ensure_ascii=False))
        ws.send(json.dumps(routeData, ensure_ascii=False))
        ws.send(json.dumps(staData, ensure_ascii=False))
        for sta in staInfo:
            sta['isWork'] = 0
        # print(end)
        # dic = getRoute("cc",end,t,random.uniform(0,5))  #产生随机速度的定位结果
        # print(dic)
        # print(dic['endPoint'][0])
        time.sleep(t)