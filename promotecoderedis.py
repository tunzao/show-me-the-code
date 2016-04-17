#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'tunzao'

"""
show me the code 0003
将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
"""
from promotecode import generatecodes
from redis import Redis

# generate 200 promote codes
promote_codes = generatecodes(200)

# connect to redis
db = Redis()
redis_key = 'promote.codes'

try:
    for code in promote_codes:
        # insert promote code into redis
        db.sadd(redis_key, code)
except Exception, e:
    print e
