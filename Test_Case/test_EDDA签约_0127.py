import unittest
import time
import logging
from Business.H5.H5_申请EDDA签约 import Creat_h5_eDDAcontract
from Common.data_文本读写 import *

class Test_Creat_H5_eDDAcontract(unittest.TestCase):

    def setUp(self):
        self.H5eDDAcontract = Creat_h5_eDDAcontract()
        logging.info("enableAcct停用后开启")


    #开启之前先校验账号状态
    def test_01_H5_submit_eDDAcontract(self):
        submiteDDAcontract = self.H5eDDAcontract.H5submit_eDDAcontract()
        self.assertEqual(200, submiteDDAcontract.status_code)
        self.assertEqual("OK", submiteDDAcontract.json().get("msg"))
        print("已执行用例1===============================================================")

    # 操作开启后校验账号状态
    def test_02_SQLCheck_bank_ac_eddaapply(self):
        Check_bank_ac_eddaapply = self.H5eDDAcontract.check_bank_ac_edda_apply()

        accinfo=datahandle(data_read('F:\\python\\EDDID_CDMS\\Data\\unableAcct.txt'))
        # self.assertEqual("DONE", Check_bank_ac_eddaapply[0][27])
        self.assertEqual(accinfo[0], Check_bank_ac_eddaapply[0][1])
        self.assertEqual(accinfo[5], Check_bank_ac_eddaapply[0][12])
        self.assertEqual(accinfo[4]+" "+accinfo[3], Check_bank_ac_eddaapply[0][7])
        logging.info("已执行用例02，数据库校验已完成")
        print("已执行用例02===============================================================")

    def tearDown(self):
        a = 6
        time.sleep(a)
        logging.info("接口请求完成后，等待系统处理数据，等待{}秒".format(a))