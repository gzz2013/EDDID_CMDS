import unittest
import time
import logging
from Business.CreatEquitiesWithdrawalnew出金 import CreatEquitiesWithdrawal出金
from Common.data_文本读写 import *
#2021年12月30日13:56:22

class Test_CreatEquitiesWithdrawalNew出金(unittest.TestCase):

    def setUp(self):
        self.CreatEquitiesWithdrawal = CreatEquitiesWithdrawal出金()
        logging.info("初始化CreatEquitiesWithdrawal已完成")

    def test_01_createWithdrawal创建出金单(self):
        auditWithdrawalNo = self.CreatEquitiesWithdrawal.createWithdrawal创建出金单()
        self.assertEqual(200, auditWithdrawalNo.status_code)
        self.assertEqual("操作成功", auditWithdrawalNo.json().get("msg"))
        print("已执行用例1===============================================================")

    def test_02_operatingWorkFlowNo(self):
        operatingWorkFlowNo = self.CreatEquitiesWithdrawal.get_current_state()
        self.assertEqual(200, operatingWorkFlowNo.status_code)
        self.assertEqual("操作成功", operatingWorkFlowNo.json().get("msg"))
        self.assertEqual("操作成功", operatingWorkFlowNo.json().get("data")[0].get("operatingMessage"))
        print("已执行用例2===============================================================")

    def test_03_auditWithdrawalAcctPass(self):
        auditWithdrawalAcctPass = self.CreatEquitiesWithdrawal.auditWithdrawalAcctPass()
        self.assertEqual(200, auditWithdrawalAcctPass.status_code)
        self.assertEqual("操作成功", auditWithdrawalAcctPass.json().get("msg"))
        print("已执行用例3===============================================================")

    #数据库gs_apply_work_flow校验
    def test_04_get_current_state_final(self):
        statefinal=self.CreatEquitiesWithdrawal.get_current_state_final()
        self.assertEqual("DONE_8", statefinal[0][3])
        self.assertEqual("withdrawalApply", statefinal[0][2])
        self.assertEqual("N", statefinal[0][4])
        print("已执行用例4===============================================================")

    def tearDown(self):
        a = 6
        time.sleep(a)
        logging.info("接口请求完成后，等待系统处理数据，等待{}秒".format(a))
