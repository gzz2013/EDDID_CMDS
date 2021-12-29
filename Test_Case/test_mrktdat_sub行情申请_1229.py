import unittest
import time
import logging
from Business.H5.H5_行情申请 import Creat_mrktdat_sub
from Common.com_sql import *
from Common.data_文本读写 import *


class Test_Submit_mrktdat行情提交及审核(unittest.TestCase):

    def setUp(self):
        self.Creatmrktdat = Creat_mrktdat_sub()
        logging.info("Creat_mrktdat_sub初始化完成")


    #校验H5登录
    def test_01_H5submit_mrktdat(self):
        enableAcct = self.Creatmrktdat.H5submit_mrktdat()
        self.assertEqual(200, enableAcct.status_code)
        self.assertEqual("OK", enableAcct.json().get("msg"))
        print("已执行用例1===============================================================")

    # 校验提交锁
    def test_02_operatingWorkFlow提交锁(self):
        operatingWorkFlow = self.Creatmrktdat.operatingWorkFlow提交锁()
        self.assertEqual(200, operatingWorkFlow.status_code)
        self.assertEqual("操作成功", operatingWorkFlow.json().get("msg"))
        print("已执行用例2===============================================================")

    # 提交审批
    def test_03_auditRtqSubscptn(self):
        auditRtqSubscptn = self.Creatmrktdat.auditRtqSubscptn审批()
        self.assertEqual(200, auditRtqSubscptn.status_code)
        self.assertEqual("操作成功", auditRtqSubscptn.json().get("msg"))
        print("已执行用例03===============================================================")

    # 提交审核
    def test_03_check_gs_mrktdat_sub(self):
        infotxt=datahandle(data_read('F:\\python\\EDDID_CDMS\\Data\\unableAcct.txt'))
        gs_mrktdat_sub = self.Creatmrktdat.check_gs_mrktdat_sub()
        self.assertEqual("PAID", gs_mrktdat_sub[0][7])
        self.assertEqual("HKD", gs_mrktdat_sub[0][3])
        self.assertEqual("1个月港股实时行情", gs_mrktdat_sub[0][4])
        self.assertEqual(infotxt[0], gs_mrktdat_sub[0][2])
        self.assertEqual("cpH5", gs_mrktdat_sub[0][15])
        logging.info("已执行用例03，数据库校验已完成")
        print("已执行用例03===============================================================")




    def tearDown(self):
        a = 3
        time.sleep(a)
        logging.info("接口请求完成后，等待系统处理数据，等待{}秒".format(a))
