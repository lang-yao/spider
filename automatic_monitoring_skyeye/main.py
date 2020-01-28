# -*- coding: utf-8 -*-
# author  : sloth
# file    : main.py
# time    : 2020/1/28 9:27
import time
from automatic_monitoring_skyeye.log_config import *
from automatic_monitoring_skyeye.AutomaticSkyeye import AutomaticSkyeye
import configparser


def main():
    skyeyes = configparser.ConfigParser()
    skyeyes.read('skyeye.ini')
    for api in skyeyes.sections():
        url = skyeyes[api]['url']
        username = skyeyes[api]['username']
        passwd = skyeyes[api]['passwd']
        logging.info(api + '开始巡检：')
        logging.info(url)
        skyeye = AutomaticSkyeye(username, passwd, url)
        skyeye.run()
        logging.info('巡检结束...')
        time.sleep(10)

    logging.info('-' * 10 + 'over' + '-' * 10)


if __name__ == '__main__':
    main()
