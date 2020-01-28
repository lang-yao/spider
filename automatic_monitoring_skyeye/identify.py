# -*- coding: utf-8 -*-
# author  : sloth
# file    : identify.py
# time    : 2020/1/26 18:02
import pytesseract
from PIL import Image
from PIL import ImageDraw
from automatic_monitoring_skyeye.baidu_identify import img_to_str


def get_binary_pic(img):
    w, h = img.size
    for x in range(w):
        for y in range(h):
            r, g, b = x, y, img.getpixel((x, y))
            if 190 <= r <= 255 and 170 <= g <= 255 and 0 <= b <= 140:
                img.putpixel((x, y), (0, 0, 0))
            if 0 <= r <= 90 and 210 <= g <= 255 and 0 <= b <= 90:
                img.putpixel((x, y), (0, 0, 0))
    img = img.convert('L').point([0] * 150 + [1] * (256 - 150), '1')
    return img


# 二值数组
def twoValue(image, imgage_arr, G):
    for y in range(0, image.size[1]):
        for x in range(0, image.size[0]):
            g = image.getpixel((x, y))
            if g > G:
                imgage_arr[(x, y)] = 1
            else:
                imgage_arr[(x, y)] = 0
    return imgage_arr


# 根据一个点A的RGB值，与周围的8个点的RBG值比较，设定一个值N（0 <N <8），当A的RGB值与周围8个点的RGB相等数小于N时，此点为噪点
# G: Integer 图像二值化阀值
# N: Integer 降噪率 0 <N <8
# Z: Integer 降噪次数
# 输出
#  0：降噪成功
#  1：降噪失败
def clearNoise(image, image_arr, N, Z):
    for i in range(0, Z):
        image_arr[(0, 0)] = 1
        image_arr[(image.size[0] - 1, image.size[1] - 1)] = 1

        for x in range(1, image.size[0] - 1):
            for y in range(1, image.size[1] - 1):
                nearDots = 0
                L = image_arr[(x, y)]
                if L == image_arr[(x - 1, y - 1)]:
                    nearDots += 1
                if L == image_arr[(x - 1, y)]:
                    nearDots += 1
                if L == image_arr[(x - 1, y + 1)]:
                    nearDots += 1
                if L == image_arr[(x, y - 1)]:
                    nearDots += 1
                if L == image_arr[(x, y + 1)]:
                    nearDots += 1
                if L == image_arr[(x + 1, y - 1)]:
                    nearDots += 1
                if L == image_arr[(x + 1, y)]:
                    nearDots += 1
                if L == image_arr[(x + 1, y + 1)]:
                    nearDots += 1

                if nearDots < N:
                    image_arr[(x, y)] = 1
    return image_arr


# 保存图片
def draw_pic(image_arr, size):
    image = Image.new("1", size)
    draw = ImageDraw.Draw(image)

    for x in range(0, size[0]):
        for y in range(0, size[1]):
            draw.point((x, y), image_arr[(x, y)])
    image.save('a.jpg')
    return image


# def recognize_captcha():

def recognize_captcha(im):
    tessdata_dir_config = '--tessdata-dir "D:/Program Files (x86)/Tesseract-OCR/tessdata"'
    pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
    res = pytesseract.image_to_string(im)
    return res


def identify_pic(imgage):
    img = get_binary_pic(imgage).convert("L")
    image_arr = {}
    twoValue(img, image_arr, 100)
    clearNoise(img, image_arr, 3, 2)
    img = draw_pic(image_arr, img.size)
    # img.show()
    # tesseract识别
    # res = recognize_captcha(img)
    # baidu api
    img.save('vertify_code.png')
    res = img_to_str()

    return res


if __name__ == '__main__':
    recognize_captcha()
