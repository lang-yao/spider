# -*- coding: utf-8 -*-
# author  : sloth
# file    : AutomaticSkyeye.py
# time    : 2020/1/26 10:57
import time
from PIL import Image
from selenium import webdriver
from automatic_monitoring_skyeye.log_config import *


def skyeye_res(pick_num):
    def inner(func):
        def wrapper(self, browser):
            func(self, browser)
            browser.find_element_by_class_name('fa-chevron-down').click()
            browser.find_elements_by_class_name('select-box')[2].click()
            browser.find_elements_by_class_name('skyEye-checkbox__label')[pick_num].click()
            browser.find_element_by_class_name('btn-search').click()
            time.sleep(3)
            # 下载
            if len(browser.find_elements_by_class_name('no-data')) != 0:
                logging.info('暂无数据!')
            else:
                logging.info('已下载数据表!' + '#' * 20)
                browser.find_element_by_xpath('//div/button[2]').click()
            time.sleep(1)

        return wrapper

    return inner


class AutomaticSkyeye:
    def __init__(self, username=None, passwd=None, url=None):
        self.url = url
        self.username = username
        self.passwd = passwd

    def run(self):
        browser = self.start()
        self.__login(browser, self.username, self.passwd)
        self.__exp(browser)
        self.__webshell(browser)
        self.__net_attack(browser)
        self.__alarm(browser)
        self.__done(browser)

    def start(self):
        logging.info('启动chrome浏览器...')
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        browser = webdriver.Chrome(chrome_options=options)
        browser.maximize_window()
        browser.get(self.url)
        time.sleep(2)
        logging.info(browser.title)

        return browser

    def __login(self, browser, username, passwd):
        logging.info('登录中...')
        browser.find_element_by_name('username').send_keys(username)
        browser.find_element_by_name('password').send_keys(passwd)
        # 获取屏幕截图
        while True:
            screen_pic = browser.save_screenshot("login_page.png")
            # 获取验证码位置
            vertify_ele = browser.find_element_by_class_name('refresh-code')
            left = int(vertify_ele.location['x']) + 298
            top = int(vertify_ele.location['y']) + 99  # 获取验证码上边位置
            right = left + int(vertify_ele.size['width']) + 19  # 获取验证码右边位置
            bottom = top + int(vertify_ele.size['height']) + 10  # 获取验证码下边位置

            # 剪切验证码
            has_screen = Image.open('login_page.png')
            vertify_pic = has_screen.crop((left, top, right, bottom))
            # 显示图片
            # vertify_pic.show()
            # vertify_code = identify_pic(vertify_pic)
            # 手动输入
            vertify_code = input('验证码:\n')

            logging.info(vertify_code)
            browser.find_element_by_name('authcode').send_keys(vertify_code)
            browser.find_element_by_class_name('submit-btn').click()
            time.sleep(1)
            if browser.current_url.split('/')[-1] == 'state':
                logging.info('登录成功!')
                break
            browser.find_element_by_class_name('refresh-code').click()
            browser.find_element_by_name('authcode').clear()

    @skyeye_res(44)
    def __exp(self, browser):
        logging.info('网页漏洞利用:')
        browser.find_elements_by_class_name('btn-sub-menu')[1].click()
        browser.find_element_by_xpath('//div/ul/li[2]/ul/li[1]/a')

    @skyeye_res(32)
    def __webshell(self, browser):
        logging.info('webshell上传:')
        browser.find_element_by_xpath('//div/ul/li[2]/ul/li[2]/a').click()

    @skyeye_res(30)
    def __net_attack(self, browser):
        logging.info('网络攻击:')
        browser.find_element_by_xpath('//div/ul/li[2]/ul/li[3]/a').click()

    def __alarm(self, browser):
        logging.info('威胁情报告警:')
        browser.find_element_by_xpath('//div/ul/li[2]/ul/li[4]/a').click()
        time.sleep(3)
        if len(browser.find_elements_by_class_name('no-data')) != 0:
            logging.info('\t 暂无数据!')
        else:
            logging.info('\t 已下载数据表!')
            browser.find_element_by_xpath('//div/button[2]').click()
            time.sleep(5)

    def __done(self, browser):
        logging.info('任务结束,退出！')
        browser.quit()
