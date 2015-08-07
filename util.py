#!/usr/bin/env python3
#-*- coding:utf-8 -*-
请在Python3下运行此程序='Please run this program with Python3'
import re

# From: http://stackoverflow.com/questions/2545532/python-analog-of-natsort-function-sort-a-list-using-a-natural-order-algorithm
def natural_key(string_):
    """
    See http://www.codinghorror.com/blog/archives/001018.html
    list_ = ['img1', 'img12', 'img5', 'img13', 'img2']
    print(sorted(list_, key=natural_key))
    """
    return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_)]
