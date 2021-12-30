import unittest
import time
import logging
from Business.CreatUser_创建其他交易类型账号 import CreatUser创建其他类型交易账号
from Common.com_sql import *
from Common.data_文本读写 import *
from Config.cdms_config import *
#2021年12月30日13:56:22

class Test_CreatUser创建其他类型交易账号(unittest.TestCase):

    def setUp(self):
        self.CreatUseraddAccountTrading = CreatUser创建其他类型交易账号()
        logging.info("CreatUser创建其他类型交易账号")

    def test_01_addAccountTrading(self):
        addAccountTrading = self.CreatUseraddAccountTrading.addAccountTrading()
        self.assertEqual(200, addAccountTrading.status_code)
        self.assertEqual("操作成功", addAccountTrading.json().get("msg"))
        # self.assertEqual(True, addAccountTrading.json().get("data")[0].get("result"))
        print("已执行用例11===============================================================")

    def test_02_auditAccountTradingno(self):
        auditAccountTradingno = self.CreatUseraddAccountTrading.auditAccountTradingno()
        self.assertEqual(200, auditAccountTradingno.status_code)
        self.assertEqual("操作成功", auditAccountTradingno.json().get("msg"))
        # self.assertEqual(True, auditAccountTradingno.json().get("data")[0].get("result"))
        print("已执行用例12===============================================================")

    def test_03_auditAccountTradingto(self):
        auditAccountTradingto = self.CreatUseraddAccountTrading.auditAccountTradingto()
        self.assertEqual(200, auditAccountTradingto.status_code)
        self.assertEqual("操作成功", auditAccountTradingto.json().get("msg"))
        # self.assertEqual(True, auditAccountTradingto.json().get("data")[0].get("result"))
        print("已执行用例13===============================================================")

    def test_04_auditAccountTradingth(self):
        auditAccountTradingth = self.CreatUseraddAccountTrading.auditAccountTradingth()
        self.assertEqual(200, auditAccountTradingth.status_code)
        self.assertEqual("操作成功", auditAccountTradingth.json().get("msg"))
        # self.assertEqual(True, auditAccountTradingth.json().get("data")[0].get("result"))
        print("已执行用例14===============================================================")

    def test_05_SQLCheckUser(self):
        userinf=datahandle(data_read('F:\\python\\EDDID_CDMS\\Data\\userdatainf.txt'))
        logging.info("从文本中读到的用户基本信息为：{}".format(userinf))
        SQLCheckUser=self.CreatUseraddAccountTrading.SQLCheckUser()
        # 检验电话
        self.assertEqual(userinf[0], SQLCheckUser[0][18])
        # 检验邮箱
        self.assertEqual(userinf[1], SQLCheckUser[0][15])
        # 检验英文姓
        self.assertEqual(userinf[3], SQLCheckUser[0][10])
        # 检验英文名
        self.assertEqual(userinf[2], SQLCheckUser[0][9])
        # 检验中文姓名
        self.assertEqual(userinf[4], SQLCheckUser[0][13])
        # 检验身份证
        self.assertEqual(userinf[5], SQLCheckUser[0][4])
        # 检验称谓
        self.assertEqual(userinf[6], SQLCheckUser[0][8])
        #非空校验
        self.assertIsNotNone(SQLCheckUser)
        self.assertEqual("PERSONAL", SQLCheckUser[0][2])
        logging.info("已执行用例15，数据库校验已完成")
        print("已执行用例15===============================================================")


    def tearDown(self):
        a = 6
        time.sleep(a)
        logging.info("接口请求完成后，等待系统处理数据，等待{}秒".format(a))
