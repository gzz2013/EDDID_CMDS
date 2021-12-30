import unittest
import time
import logging
from Business.CreatEquitiesWithdrawal出金 import CreatEquitiesWithdrawal出金
from Common.data_文本读写 import *
#2021年12月30日13:56:22

class Test_CreatEquitiesWithdrawal出金(unittest.TestCase):

    def setUp(self):
        self.CreatEquitiesWithdrawal = CreatEquitiesWithdrawal出金()
        logging.info("初始化CreatEquitiesWithdrawal已完成")

    def test_01_createWithdrawal创建出金单(self):
        auditWithdrawalNo = self.CreatEquitiesWithdrawal.createWithdrawal创建出金单()
        self.assertEqual(200, auditWithdrawalNo.status_code)
        self.assertEqual("操作成功", auditWithdrawalNo.json().get("msg"))
        print("已执行用例1===============================================================")

    def test_02_operatingWorkFlowNo(self):
        operatingWorkFlowNo = self.CreatEquitiesWithdrawal.operatingWorkFlowNo()
        self.assertEqual(200, operatingWorkFlowNo.status_code)
        self.assertEqual("操作成功", operatingWorkFlowNo.json().get("msg"))
        self.assertEqual("操作成功", operatingWorkFlowNo.json().get("data")[0].get("operatingMessage"))
        print("已执行用例2===============================================================")

    def test_03_auditWithdrawalNo(self):
        auditWithdrawalNo = self.CreatEquitiesWithdrawal.auditWithdrawalNo()
        self.assertEqual(200, auditWithdrawalNo.status_code)
        self.assertEqual("操作成功", auditWithdrawalNo.json().get("msg"))
        print("已执行用例3===============================================================")

    def test_04_operatingWorkFlowTO(self):
        operatingWorkFlowTO = self.CreatEquitiesWithdrawal.operatingWorkFlowTO()
        self.assertEqual(200, operatingWorkFlowTO.status_code)
        self.assertEqual("操作成功", operatingWorkFlowTO.json().get("msg"))
        self.assertEqual("操作成功", operatingWorkFlowTO.json().get("data")[0].get("operatingMessage"))
        print("已执行用例4===============================================================")

    def test_05_auditWithdrawalTo(self):
        auditWithdrawalTo = self.CreatEquitiesWithdrawal.auditWithdrawalTo()
        self.assertEqual(200, auditWithdrawalTo.status_code)
        self.assertEqual("操作成功", auditWithdrawalTo.json().get("msg"))
        print("已执行用例5===============================================================")

    def test_06_get_current_state(self):
        get_current_state = self.CreatEquitiesWithdrawal.get_current_state()
        self.assertEqual(200, get_current_state.status_code)
        self.assertEqual("操作成功", get_current_state.json().get("msg"))
        print("已执行用例6===============================================================")

    def test_07_operatingWorkFlowfourth(self):
        operatingWorkFlowfourth = self.CreatEquitiesWithdrawal.operatingWorkFlowfourth()
        self.assertEqual(200, operatingWorkFlowfourth.status_code)
        self.assertEqual("操作成功", operatingWorkFlowfourth.json().get("msg"))
        self.assertEqual("操作成功", operatingWorkFlowfourth.json().get("data")[0].get("operatingMessage"))
        print("已执行用例7===============================================================")

    def test_08_auditWithdrawalAcctPass(self):
        auditWithdrawalAcctPass = self.CreatEquitiesWithdrawal.auditWithdrawalAcctPass()
        self.assertEqual(200, auditWithdrawalAcctPass.status_code)
        self.assertEqual("操作成功", auditWithdrawalAcctPass.json().get("msg"))
        print("已执行用例8===============================================================")

    #
    def tearDown(self):
        a = 6
        time.sleep(a)
        logging.info("接口请求完成后，等待系统处理数据，等待{}秒".format(a))
