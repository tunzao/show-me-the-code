"""
show me the code 0001
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
    generate code of size size with chars in chars
    """
    return ''.join(random.choice(chars) for i in range(size) )


if __name__ == '__main__':
    pprint.pprint(generatecodes(200))
