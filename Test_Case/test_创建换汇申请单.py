import unittest
import time
import logging
from Business.Creat创建换汇申请单 import CreateExchange
from Common.data_文本读写 import *
#2021年12月30日13:56:22


class Test_CreateExchange新建换汇申请单(unittest.TestCase):

    def setUp(self):
        self.CreateExchange = CreateExchange()
        logging.info("初始化CreateExchange已完成")

    def test_01_createExchange创建换汇申请单(self):
        createExchange = self.CreateExchange.createExchange创建换汇申请单()
        self.assertEqual(200, createExchange.status_code)
        self.assertIn(createExchange.json().get("msg"),"操作成功，OK")
        print("已执行用例1===============================================================")

    def test_02_operatingWorkFlowFirst提交锁(self):
        operatingWorkFlowFirst = self.CreateExchange.operatingWorkFlowFirst提交锁()
        self.assertEqual(200, operatingWorkFlowFirst.status_code)
        self.assertEqual("操作成功", operatingWorkFlowFirst.json().get("msg"))
        self.assertEqual("操作成功", operatingWorkFlowFirst.json().get("data")[0].get("operatingMessage"))
        print("已执行用例3===============================================================")

    def test_03_auditExchange提交审核换汇申请单(self):
        auditExchange = self.CreateExchange.auditExchange提交审核换汇申请单()
        self.assertEqual(200, auditExchange.status_code)
        self.assertEqual("操作成功", auditExchange.json().get("msg"))
        print("已执行用例2===============================================================")

    def test_04_SQLCheckexchorder(self):
        #数据库查询出数据
        SQLCheckexchorderinfor = self.CreateExchange.SQLCheckexchorder()

        #从文本中读取数据
        Txtexchorderinfor=datahandle(data_read('F:\\python\\EDDID_CDMS\\Data\\exchorderinfor.txt'))
        logging.info("从文本中读到的换汇单基本信息为：{}".format(Txtexchorderinfor))
        print(Txtexchorderinfor,type(Txtexchorderinfor))
        self.assertEqual("USD", SQLCheckexchorderinfor[0][6])
        self.assertEqual("HKD", SQLCheckexchorderinfor[0][5])
        # self.assertEqual(2, SQLCheckexchorderinfor[0][-1])
        self.assertEqual(Txtexchorderinfor[0], SQLCheckexchorderinfor[0][2])
        self.assertEqual(Txtexchorderinfor[1], SQLCheckexchorderinfor[0][3])
        #截取数据库的金额字段后再做比较
        self.assertEqual(float(Txtexchorderinfor[2]), float('%.2f'%(SQLCheckexchorderinfor[0][9])))
        self.assertEqual(float(Txtexchorderinfor[3]), float('%.3f'%(SQLCheckexchorderinfor[0][7])))

        print("已执行用例3===============================================================")

    def tearDown(self):
        a = 6
        time.sleep(a)
        logging.info("接口请求完成后，等待系统处理数据，等待{}秒".format(a))
