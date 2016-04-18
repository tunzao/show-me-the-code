#!/usr/bin/env python
# -*_ coding: utf-8 -*-
__author__ = 'tunzao'

'''
第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。
'''

import fileinput
import re

total = 0
for line in fileinput.input():
    words = re.findall('[a-zA-Z]+', line)
    total = len(words)

print 'total words:', str(total)
