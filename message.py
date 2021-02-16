#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import urllib
import json
import cv2

import time

cnt = 0
secs = time.time()

def getAccessToken(refreshToken) :
    url = "https://kauth.kakao.com/oauth/token"
    payload = "grant_type=refresh_token&client_id=19838e3704a9c76971ac7a01b7c34db5&refresh_token=" + refreshToken
    headers = {
        'Content-Type' : "application/x-www-form-urlencoded",
        'Cache-Control' : "no-cache",
    }
    reponse = requests.request("POST",url,data=payload, headers=headers)
    access_token = reponse.json()
    return access_token

def sendText(accessToken) :
    url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'
    payloadDict = dict({
            "object_type": "text",
            "text": "사람이 감지되었습니다",
            "link": {
                "web_url": "https://developers.kakao.com",
                "mobile_web_url": "https://developers.kakao.com"
            },
            "button_title": "바로 확인",
    })

    payload = "template_object=" + str(json.dumps(payloadDict))
    print(payload)
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Authorization' : "Bearer " + str(accessToken),
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    #access_token = response.json()
    return (response.text)

def myProfile(accessToken):
    url = 'https://kapi.kakao.com/v1/api/talk/profile'
    headers = {
        'Content-Type': "application/json;charset=UTF-8",
        'Authorization': "Bearer " + str(accessToken)
    }
    response = requests.request("POST", url, headers=headers)
    return (response.text)

def sendimage(accessToken, secs):
    tm = time.localtime(secs)
    current = time.strftime('%Y-%m-%d %I:%M:%S %p', tm)
    url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'
    payloadDict = dict({
        "object_type": "feed",
        "content" : {
            "title": "사람이 감지되었습니다",
            "description": current,
            "image_url": "http://111.91.172.233:5000/static/data/"+str(secs)+".jpg",
            "image_width": 640,
            "image_height": 640,
            "link": {
            "web_url": "http://111.91.172.233:5000",
            "mobile_web_url": "http://111.91.172.233:5000",
            }
        },
        "social": {
        },
        "button_title": "CCTV 확인하기"
    })
    payload = "template_object=" + str(json.dumps(payloadDict))

    headers = {
        'Cache-Control': "no-store",
        'Content-Type': "application/x-www-form-urlencoded",
        'Authorization': "Bearer " + str(accessToken),
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    return (response.text)

result = getAccessToken("rXV9LQ-C_E_pCzdvNgZMTa3-1kMs7SRJExn6Rwo9dRoAAAFysSrsGg") # 메세지 받을 사람의 REFRESH TOKEN 이용
#print(result)
#print(myProfile(result['access_token']))
#print(sendText(result['access_token']))


while(1):
    time.sleep(5)
    cnt += 1
    try:
        f = open("static/flag.txt", 'r')
        line = f.readline()
        f.close()
    except:
        continue

    if line == "1":
        secs = time.time()
        image = cv2.imread('static/res.jpg')
        cv2.imwrite('static/data/'+str(secs)+'.jpg', image)
        print(sendimage(result['access_token'], secs))
    else:
        continue

#print(sendimage(result['access_token']))
#print(sendText(result['access_token']))
