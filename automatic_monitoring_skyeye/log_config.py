# -*- coding: utf-8 -*-
# author  : sloth
# file    : log_config.py
# time    : 2020/1/28 11:13

import logging

logging.basicConfig(format='%(asctime)s: %(message)s',
                    level=logging.INFO,
                    filename='skyeye.log',
                    filemode='a')
