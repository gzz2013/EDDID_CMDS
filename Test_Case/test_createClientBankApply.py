import unittest
import time
import logging
from Business.createClientBankApply import CreateClientBank
from Common.com_sql import *
from Common.data_文本读写 import *
from Config.cdms_config import *
#2021年12月30日13:56:22

class Test_CreateClientBank添加银行卡(unittest.TestCase):

    def setUp(self):
        self.CreateClientBank = CreateClientBank()
        logging.info("CreateClientBank初始化完成")

    def test_01_createClientBankApply(self):
        createClientBankApply = self.CreateClientBank.createClientBankApply()
        self.assertEqual(200, createClientBankApply.status_code)
        self.assertEqual("操作成功", createClientBankApply.json().get("msg"))
        # self.assertEqual(True, addAccountTrading.json().get("data")[0].get("result"))
        print("已执行用例01===============================================================")
    def test_02_createClientBankApply(self):
        approvalClientBankApply = self.CreateClientBank.approvalClientBankApply()
        self.assertEqual(200, approvalClientBankApply.status_code)
        self.assertEqual("操作成功", approvalClientBankApply.json().get("msg"))
        # self.assertEqual(True, addAccountTrading.json().get("data")[0].get("result"))
        print("已执行用例02===============================================================")

    def test_03_approvalClientBankApplytwo(self):
        approvalClientBankApplytwo = self.CreateClientBank.approvalClientBankApplytwo()
        self.assertEqual(200, approvalClientBankApplytwo.status_code)
        self.assertEqual("操作成功", approvalClientBankApplytwo.json().get("msg"))
        # self.assertEqual(True, addAccountTrading.json().get("data")[0].get("result"))
        print("已执行用例03===============================================================")

    def test_04_sql_check_BankCard(self):
        bankCardinformation=datahandle(data_read('F:\\python\\EDDID_CDMS\\Data\\bankCardinformation.txt'))
        logging.info("从文本中读到的银行卡基本信息为：{}".format(bankCardinformation))
        sql_check_BankCard=self.CreateClientBank.sql_check_BankCard()
        # 检验clnt_id
        self.assertEqual(bankCardinformation[0], sql_check_BankCard[0][1])
        # 检验银行code
        self.assertEqual(bankCardinformation[2], sql_check_BankCard[0][2])
        # 检验银行卡号
        self.assertEqual(bankCardinformation[1], sql_check_BankCard[0][3])
        # 检验银行用户名
        self.assertEqual(bankCardinformation[3], sql_check_BankCard[0][4])
        # 检验币种
        self.assertIn("USD", sql_check_BankCard[0][6])
        self.assertIn("HKD", sql_check_BankCard[0][6])
        self.assertIn("CNY", sql_check_BankCard[0][6])
        #非空校验
        self.assertIsNotNone(sql_check_BankCard)
        logging.info("已执行用例04，数据库校验已完成")
        print("已执行用例04===============================================================")


    def tearDown(self):
        a = 6
        time.sleep(a)
        logging.info("接口请求完成后，等待系统处理数据，等待{}秒".format(a))