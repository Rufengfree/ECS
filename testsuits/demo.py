#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: rufeng

import unittest

from testsuits.Order_Create import Createorder
from testsuits.printandsend import Printsend

suite = unittest.TestSuite()
suite.addTest(Createorder('test_order_create'))
suite.addTest(Printsend('test_print_and_send'))


if __name__ == '__main__':
    # 执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)