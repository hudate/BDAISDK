#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
from urllib import request
import json
import base64
import requests
from BDOCR import getAccessToken

OCRAK = YourAK  # 需要更改
OCRSK = YourSK  # 需要更改

token = getAccessToken.getToken(OCRAK, OCRSK)
# print(token)

print('')
print('--++++++++++++++--')
print('--|百度云OCR识别|--')
print('--++++++++++++++--')
print('')


# 高精度识别
# baidu_api_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=' + token

# 一般精度
baidu_api_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=' + token

# 网络图片识别
# baidu_api_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/webimage?access_token=' + token

# image_url = 'http://www.17500.cn/article/img/id/941875.html'

image_src = YourImgFile     # 需要更改

f = open(image_src,'rb')

img = base64.b64encode(f.read())

params = {'image':img}

# params = {'url': image_url}

params = urllib.parse.urlencode(params).encode('utf-8')

headers = {'Content-Type': 'application/x-www-form-urlencoded'}

# 使用requests库
r = requests.post(baidu_api_url, params=headers, data=params).json()
# print('requests 结果:')
# print(r)
# print(type(r))

# print()

# 使用urllib库
request = urllib.request.Request(url = baidu_api_url, headers = headers, data = params)
response = urllib.request.urlopen(request)
content = json.loads(response.read().decode('utf-8'))

# print('urllib结果：')
# print(content)
# print(type(content))
if (content):
	for a in content['words_result']:
		print(a['words'])
