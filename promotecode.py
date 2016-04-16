# coding: UTF-8
"""
show me the code 0001
做为 Apple Store App 独立开发者，你要搞限时促销，
为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？
"""
__author__ = 'tunzao'
import string
import random
import pprint

def generatecodes(num):
    codes = []
    for i in range(num):
        while True:
            code = codegenerator()
            if code not in codes:
                codes.append(code)
                break
    return codes


def codegenerator(size=6, chars=string.ascii_uppercase + string.digits):
    """
    generate code of size <code>size</code> with chars in <code>chars</code>
    """
    return ''.join(random.choice(chars) for i in range(size) )


if __name__ == '__main__':
    pprint.pprint(generatecodes(200))
