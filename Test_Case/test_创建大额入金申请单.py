import unittest
import time
import logging
from Business.CreatEquitiesDeposit大额入金 import CreatEquitiesDeposit大额入金
#2021年12月30日13:56:22

class Test_CreatEquitiesDeposit大额入金(unittest.TestCase):

    def setUp(self):
        self.CreatEquitiesDeposit = CreatEquitiesDeposit大额入金()
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

    # def test_04_operatingWorkFlowTo(self):
    #     operatingWorkFlowNo = self.CreatEquitiesDeposit.operatingWorkFlowTo()
    #     self.assertEqual(200, operatingWorkFlowNo.status_code)
    #     self.assertEqual("操作成功", operatingWorkFlowNo.json().get("msg"))
    #     self.assertEqual("操作成功", operatingWorkFlowNo.json().get("data")[0].get("operatingMessage"))
    #     print("已执行用例4===============================================================")

    # def test_05_auditDeposit_comp_p(self):
    #     auditDeposit_comp_p = self.CreatEquitiesDeposit.auditDeposit_comp_p()
    #     self.assertEqual(200, auditDeposit_comp_p.status_code)
    #     self.assertEqual("操作成功", auditDeposit_comp_p.json().get("msg"))
    #     print("已执行用例5===============================================================")

    def test_06_get_current_state_deposit(self):
        get_current_state_deposit = self.CreatEquitiesDeposit.get_current_state_deposit()
        self.assertEqual(200, get_current_state_deposit.status_code)
        self.assertEqual("操作成功", get_current_state_deposit.json().get("msg"))
        # self.assertEqual("操作成功", get_current_state_deposit.json().get("data")[0].get("operatingMessage"))
        print("已执行用例4===============================================================")

    #
    def tearDown(self):
        a = 6
        time.sleep(a)
        logging.info("接口请求完成后，等待系统处理数据，等待{}秒".format(a))
