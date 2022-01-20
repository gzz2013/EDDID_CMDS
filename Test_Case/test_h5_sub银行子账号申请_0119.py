import unittest
import time
import logging
from Business.H5.H5_银行子账号申请 import Creat_account_sub
from Common.com_sql import *
from Common.data_文本读写 import *
#2021年12月30日13:56:22

class Test_sub_account_银行子账号申请及审核(unittest.TestCase):

    def setUp(self):
        self.Subaccount = Creat_account_sub()
        logging.info("Creat_account_sub初始化完成")


    #校验H5登录
    def test_01_H5sub_account(self):
        subaccount = self.Subaccount.H5sub_account()
        self.assertEqual(200, subaccount.status_code)
        self.assertEqual("OK", subaccount.json().get("msg"))
        print("已执行用例01===============================================================")

    # 第一次提交锁校验
    def test_02_operatingWorkFlowone提交锁(self):
        operatingWorkFlowone = self.Subaccount.operatingWorkFlowone提交锁()
        self.assertEqual(200, operatingWorkFlowone.status_code)
        self.assertEqual("操作成功", operatingWorkFlowone.json().get("msg"))
        print("已执行用例02===============================================================")

    # 提交CS2审批
    def test_03_auditRtqSubscptn(self):
        approvalBankSubAccountCS2 = self.Subaccount.approvalBankSubAccountCS2审核()
        self.assertEqual(200, approvalBankSubAccountCS2.status_code)
        self.assertEqual("操作成功", approvalBankSubAccountCS2.json().get("msg"))
        print("已执行用例03===============================================================")

    # 第二次提交锁校验
    def test_04_operatingWorkFlowtwo提交锁(self):
        operatingWorkFlowtwo = self.Subaccount.operatingWorkFlowtwo提交锁()
        self.assertEqual(200, operatingWorkFlowtwo.status_code)
        self.assertEqual("操作成功", operatingWorkFlowtwo.json().get("msg"))
        print("已执行用例04===============================================================")

    # 提交最终审批
    def test_05_approvalBankSubAccountfinal审批(self):
        approvalBankSubAccountfinal = self.Subaccount.approvalBankSubAccountfinal审批()
        self.assertEqual(200, approvalBankSubAccountfinal.status_code)
        self.assertEqual("操作成功", approvalBankSubAccountfinal.json().get("msg"))
        print("已执行用例05===============================================================")

    # 数据库数据测试
    def test_06_check_gs_mrktdat_sub(self):
        infotxt=datahandle(data_read('F:\\python\\EDDID_CDMS\\Data\\unableAcct.txt'))
        subacct = self.Subaccount.check_cd_clnt_bank_sub_acct()
        self.assertEqual("ICBC", subacct[0][2])
        self.assertEqual("072"+infotxt[1]+"951", subacct[0][3])
        self.assertEqual("ESFL-Owen StockU", subacct[0][4])
        self.assertEqual(infotxt[1], subacct[0][1])
        logging.info("已执行用例06，数据库校验已完成")
        print("已执行用例06===============================================================")

    def tearDown(self):
        a = 4
        time.sleep(a)
        logging.info("接口请求完成后，等待系统处理数据，等待{}秒".format(a))
