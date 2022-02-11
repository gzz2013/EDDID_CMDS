import unittest
import time
import logging
from Common.com_sql import *
from Business.H5.H5_申请EDDA入金 import *


class Test_H5_EDDAdeposit入金(unittest.TestCase):

    def setUp(self):
        self.EDDAdeposit = Creat_h5_EDDAdeposit入金()
        logging.info("初始化Creat_h5_EDDAdeposit入金")

    def test_01_H5submit_EDDAdeposit(self):
        H5submit_EDDAdeposit = self.EDDAdeposit.H5_submit_EDDAdeposit()
        self.assertEqual(200, H5submit_EDDAdeposit.status_code)
        self.assertEqual("OK", H5submit_EDDAdeposit.json().get("msg"))
        print("已执行用例1===============================================================")


    def test_02_get_current_state_EDDAdeposit(self):
        get_current_state_EDDAdeposit = self.EDDAdeposit.get_current_state_EDDAdeposit()
        self.assertEqual("DONE_7", get_current_state_EDDAdeposit[0][3])
        self.assertEqual("depositApply", get_current_state_EDDAdeposit[0][2])
        # self.assertEqual("入金申请", get_current_state_EDDAdeposit[0][9])
        print("已执行用例2===============================================================")

    def test_03_get_EDDAdeposit(self):
        get_EDDAdeposit = self.EDDAdeposit.get_EDDAdeposit()
        accinfo = datahandle(data_read('F:\\python\\EDDID_CDMS\\Data\\unableAcct.txt'))
        tradeAccountType = accountCategory(accinfo[2])
        self.assertEqual(accinfo[0], get_EDDAdeposit[0][2])
        self.assertEqual(accinfo[1], get_EDDAdeposit[0][3])
        self.assertEqual("edda", get_EDDAdeposit[0][12])
        self.assertEqual(tradeAccountType[0], get_EDDAdeposit[0][5])

        print("已执行用例3===============================================================")


    #
    def tearDown(self):
        a = 6
        time.sleep(a)
        logging.info("接口请求完成后，等待系统处理数据，等待{}秒".format(a))
