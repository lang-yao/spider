# -*- coding: utf-8 -*-
# author  : sloth
# file    : baidu_identify.py
# time    : 2020/1/27 13:48

from aip import AipOcr

config = {
    'appId': '18346048',
    'apiKey': 'qsCOX2baWYUaKvVnlWHCAqow',
    'secretKey': 'uy3vnBTsaDRfG7WApYpH2XfffQ7Ytn09'
}
file = 'vertify_code.png'
client = AipOcr(**config)


def get_file_content():
    with open(file, 'rb') as fp:
        return fp.read()


def img_to_str():
    image = get_file_content()
    result = client.basicGeneral(image)
    return '\n'.join([w['words'] for w in result['words_result']])


if __name__ == '__main__':
    imagepath = 'a.jpg'
    img_to_str()
