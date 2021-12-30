import unittest
import time
import logging
from Business.enableAcct_停用账号开启 import enableAcct停用后开启
# from Common.com_sql import *
# from Common.data_文本读写 import *
#2021年12月30日13:56:22

class Test_enableAcct停用后开启(unittest.TestCase):

    def setUp(self):
        self.enableAcct = enableAcct停用后开启()
        logging.info("enableAcct停用后开启")


    #开启之前先校验账号状态
    def test_01_SQLCheck_ac_stat_front(self):
        ac_stat_front = self.enableAcct.SQLCheck_ac_stat_front()
        self.assertEqual("SUSPENDED", ac_stat_front[0][13])
        # self.assertEqual("操作成功", applyClient.json().get("msg"))
        print("已执行用例1===============================================================")

    def test_02_enableAcct账号停用(self):
        enableAcct = self.enableAcct.enableAcct账号停用()
        self.assertEqual(200, enableAcct.status_code)
        self.assertEqual("操作成功", enableAcct.json().get("msg"))
        print("已执行用例2===============================================================")

    # 操作开启后校验账号状态
    def test_03_SQLCheckUser(self):
        ac_stat_after = self.enableAcct.SQLCheck_ac_stat_after()
        self.assertEqual("NORMAL", ac_stat_after[0][13])
        # self.assertEqual("操作成功", applyClient.json().get("msg"))

        logging.info("已执行用例03，数据库校验已完成")
        print("已执行用例03===============================================================")

    def tearDown(self):
        a = 6
        time.sleep(a)
        logging.info("接口请求完成后，等待系统处理数据，等待{}秒".format(a))
