import unittest
import time
import logging
from Business.SwapEquity转股 import SwapEquity
from Common.data_文本读写 import data_read,datahandle

class Test_SwapEquity转股(unittest.TestCase):

    def setUp(self):
        self.SwapEquity = SwapEquity()
        logging.info("SwapEquity方法实例化完成")


    def test_01_addEquitySwap(self):
        addEquitySwap = self.SwapEquity.addEquitySwap()
        self.assertEqual(addEquitySwap.status_code, 200)
        self.assertEqual(addEquitySwap.json().get("msg"), "操作成功")

    def test_02_OperatingWorkFlowon(self):
        WorkFlowon = self.SwapEquity.OperatingWorkFlowon()
        self.assertEqual(WorkFlowon.status_code, 200)
        self.assertEqual(WorkFlowon.json().get("msg"), "操作成功")
        self.assertEqual(WorkFlowon.json().get("data")[0].get("operatingMessage"),"操作成功")

    def test_03_OperatingWorkFlowCS2(self):
        WorkFlowCS2 = self.SwapEquity.OperatingWorkFlowCS2()
        self.assertEqual(WorkFlowCS2.status_code, 200)
        self.assertEqual(WorkFlowCS2.json().get("msg"), "操作成功")

    def test_04_OperatingWorkFlowtwo(self):
        WorkFlowtwo = self.SwapEquity.OperatingWorkFlowtwo()
        self.assertEqual(WorkFlowtwo.status_code, 200)
        self.assertEqual(WorkFlowtwo.json().get("msg"), "操作成功")
        self.assertEqual(WorkFlowtwo.json().get("data")[0].get("operatingMessage"),"操作成功")

    def test_05_OperatingWorkFlowSETL(self):
        WorkFlowCS2 = self.SwapEquity.OperatingWorkFlowSETL()
        self.assertEqual(WorkFlowCS2.status_code, 200)
        self.assertEqual(WorkFlowCS2.json().get("msg"), "操作成功")

    def test_06_sql_cd_clnt_equity_swap_item(self):
        sqlcheck=self.SwapEquity.sql_cd_clnt_equity_swap_item()
        txtdata=datahandle(data_read('F:\\python\\EDDID_CDMS\\Data\\swapequity.txt'))
        self.assertEqual(sqlcheck[0][4],int(txtdata[0]))
        self.assertEqual(sqlcheck[0][10],"完成")


    def tearDown(self):
        a = 6
        time.sleep(a)
        logging.info("接口请求完成后，等待系统处理数据，等待{}秒".format(a))