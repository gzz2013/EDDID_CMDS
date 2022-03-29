# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
代码案例：
在下面的代码中，在__init__中没有加self.的时候，
外部访问不到变量 c
可以访问到变量 a, b, e
如果实在不想添加self的情况下，可以将写法改成变量 e 的写法即可。
"""


class TestA(object):
    e = 2

    def __init__(self):
        self.a = 10
        self.b = 5
        c = 3


if __name__ == '__main__':
    test_a = TestA()
    print(test_a.a)
    print(test_a.b)
    print(test_a.e)
    print(test_a.c)  # 错误的写法