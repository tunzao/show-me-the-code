#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'tunzao'

"""
show me the code 0002
将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
"""
from promotecode import generatecodes
import MySQLdb

# generate 200 promote codes
promote_codes = generatecodes(200)

user = 'root'
passworld = '123456'
database = 'test'

# connect to mysql
db = MySQLdb.connect('localhost', user, passworld, database)
cursor = db.cursor()

try:
    for code in promote_codes:
        # insert promote code into database
        cursor.execute('insert into promote_codes (promote_code, created) values ("%s", now())' %
                code)
    db.commit()
except Exception, e:
    print e
    # rollback if exception raised
    db.rollback()

# close database connection
db.close()
