import unittest
import time
import logging
from Business.CreatEquitiesDeposit入金 import CreatEquitiesDeposit入金
from Common.data_文本读写 import *
#2021年12月30日13:56:22


class Test_CreatEquitiesDeposit入金(unittest.TestCase):

    def setUp(self):
        self.CreatEquitiesDeposit =CreatEquitiesDeposit入金()
        logging.info("初始化CreatEquitiesDeposit入金已完成")

    def test_01_createDeposit创建入金单(self):
        createDeposit = self.CreatEquitiesDeposit.createDeposit创建入金单()
        self.assertEqual(200, createDeposit.status_code)
        self.assertEqual("操作成功", createDeposit.json().get("msg"))
        print("已执行用例1===============================================================")

    def test_02_operatingWorkFlowNo(self):
        operatingWorkFlowNo = self.CreatEquitiesDeposit.operatingWorkFlowNo()
        self.assertEqual(200, operatingWorkFlowNo.status_code)
        self.assertEqual("操作成功", operatingWorkFlowNo.json().get("msg"))
        self.assertEqual("操作成功", operatingWorkFlowNo.json().get("data")[0].get("operatingMessage"))
        print("已执行用例2===============================================================")

    def test_03_auditDepositNo(self):
        auditDepositNo = self.CreatEquitiesDeposit.auditDepositNo()
        self.assertEqual(200, auditDepositNo.status_code)
        self.assertEqual("操作成功", auditDepositNo.json().get("msg"))
        print("已执行用例3===============================================================")

    def test_04_get_current_state_deposit(self):
        get_current_state_deposit = self.CreatEquitiesDeposit.get_current_state_deposit()
        self.assertEqual("DONE_7", get_current_state_deposit[3])
        self.assertEqual("depositApply", get_current_state_deposit[2])
        self.assertEqual("N", get_current_state_deposit[4])
        print("已执行用例4===============================================================")


    #
    def tearDown(self):
        a = 6
        time.sleep(a)
        logging.info("接口请求完成后，等待系统处理数据，等待{}秒".format(a))
