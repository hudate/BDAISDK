#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
sys.path.append('..')

import json
import base64
from bd_api import BDTOKEN


OCRAK = 'Your OCRAK'
OCRSK = 'Your OCRSK'



class BD_ocr(BDTOKEN):

    def __init__(self):

        print('')
        print('--+++++++++++++++--')
        print('--| 百度云OCR识别 |--')
        print('--+++++++++++++++--')
        print('')

        super().__init__(OCRAK, OCRSK)
        self.__token = super().get_token()
        self.__highAccuaryUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=' + self.__token
        self.__basicAccuaryUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=' + self.__token
        self.__webPicUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/webimage?access_token=' + self.__token
        self.__handWritingUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/handwriting'
        self.__accuracy = None

    def set_accuracy(self, accuracy=1):
        '''
        setup OCR accuracy: 1: Generally Accuracy, 2: High Accuracy
        '''
        self.__accuracy = accuracy

    def use_local_pic(self, pic_file):
        if not self.__accuracy:
            raise Exception("You must set accuracy. Set accuracy use function \"set_accuracy([accuracyValue:1 or 2])\".")
        if self.__accuracy == 1:
            url = self.__basicAccuaryUrl
        elif self.__accuracy == 2:
            url = self.__highAccuaryUrl

        f = open(pic_file, 'rb')
        img = base64.b64encode(f.read())
        f.close()
        params = {'image': img}

        return self.get_ocr_infos(url, params)

    def use_web_pic(self, pic_url):
        url = self.__webPicUrl
        params = {'url': pic_url}
        return self.get_ocr_infos(url, params)

    def get_ocr_infos(self, url, data):
        content = self.bd_request(url, data).content
        content = json.loads(content.decode('utf-8'))
        print(content)
        return [a['words'] for a in content['words_result']]

    def use_hand_writing(self, pic_file):
        pass


if __name__ == '__main__':
    ocr = BD_ocr()
    ocr.set_accuracy(2)
    # ocrs = ocr.use_local_pic("/home/hdate/Desktop/12345.png")
    # print("高精度  :", ocrs)
    # ocr.set_accuracy(1)
    ocrs = ocr.use_local_pic("/home/hdate/Desktop/12345.png")
    print("低精度  :", ocrs)
    # ocrs = ocr.use_web_pic('https://ss0.bdstatic.com/-0U0bnSm1A5BphGlnYG/tam-ogel/64a6f131ea2fcea88bb1c24d1a307c77_259_194.jpg')
    # print("网络图片:", ocrs)



