'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/6/2 10:50
@Software: PyCharm
@File    : start.py
'''
from scrapy import cmdline
cmdline.execute("scrapy crawl qsbk_spider".split())
# cmdline.execute(['scrapy' 'crawl' 'qsbk_spider'])