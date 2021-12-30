import unittest
import time
import logging
from Business.closeAcct_关闭账号 import CloseAcct账号关闭
# from Common.com_sql import *
# from Common.data_文本读写 import *
#2021年12月30日13:56:22

class Test_closeAcct账号关闭(unittest.TestCase):

    def setUp(self):
        self.closeAcct = CloseAcct账号关闭()
        logging.info("enableAcct停用后开启")


    #开启之前先校验账号状态
    def test_01_SQLCheck_ac_stat_front(self):
        ac_stat_front = self.closeAcct.SQLCheck_ac_stat_front()
        self.assertEqual("NORMAL", ac_stat_front[0][13])
        # self.assertEqual("操作成功", applyClient.json().get("msg"))
        print("已执行用例1===============================================================")

    def test_02_enableAcct账号停用(self):
        enableAcct = self.closeAcct.closeAcct账号关闭()
        self.assertEqual(200, enableAcct.status_code)
        self.assertEqual("操作成功", enableAcct.json().get("msg"))
        print("已执行用例2===============================================================")

    # 操作关闭后校验账号状态
    def test_03_SQLCheckUser(self):
        ac_stat_after = self.closeAcct.SQLCheck_ac_stat_after()
        self.assertEqual("CLOSED", ac_stat_after[0][13])
        # self.assertEqual("操作成功", applyClient.json().get("msg"))

        logging.info("已执行用例03，数据库校验已完成")
        print("已执行用例03===============================================================")

    def tearDown(self):
        a = 6
        time.sleep(a)
        logging.info("接口请求完成后，等待系统处理数据，等待{}秒".format(a))
