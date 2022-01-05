import unittest
import time
import logging
from Common.com_sql import *
from Business.H5.H5_FUTURES申请入金 import *
#2021年12月30日13:56:22

class Test_H5_DEPOSIT入金(unittest.TestCase):

    def setUp(self):
        self.H5DEPOSIT入金 = Creat_h5_deposit()
        logging.info("初始化Creat_h5_deposit已完成")

    def test_01_H5submit_deposit(self):
        H5submit_deposit = self.H5DEPOSIT入金.H5submit_deposit()
        self.assertEqual(200, H5submit_deposit.status_code)
        self.assertEqual("OK", H5submit_deposit.json().get("msg"))
        print("已执行用例1===============================================================")

    def test_02_operatingWorkFlowNo(self):
        operatingWorkFlowNo = self.H5DEPOSIT入金.operatingWorkFlowNo()
        self.assertEqual(200, operatingWorkFlowNo.status_code)
        self.assertEqual("操作成功", operatingWorkFlowNo.json().get("msg"))
        self.assertEqual("操作成功", operatingWorkFlowNo.json().get("data")[0].get("operatingMessage"))
        print("已执行用例2===============================================================")

    def test_03_auditDepositNo(self):
        auditDepositNo = self.H5DEPOSIT入金.auditDepositNo()
        self.assertEqual(200, auditDepositNo.status_code)
        self.assertEqual("操作成功", auditDepositNo.json().get("msg"))
        print("已执行用例3===============================================================")

    def test_06_get_current_state_deposit(self):
        get_current_state_deposit = self.H5DEPOSIT入金.get_current_state_deposit()
        self.assertEqual("DONE_7", get_current_state_deposit[3])
        self.assertEqual("depositApply", get_current_state_deposit[8])
        self.assertEqual("入金申请", get_current_state_deposit[9])
        print("已执行用例4===============================================================")

    #
    def tearDown(self):
        a = 6
        time.sleep(a)
        logging.info("接口请求完成后，等待系统处理数据，等待{}秒".format(a))
