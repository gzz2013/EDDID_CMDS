import unittest
import time
import logging
from Business.Creat没有结构性产品账号及申请结构性产品审批 import CreatUser无结构性产品用户创建
from Common.com_sql import *
from Common.data_文本读写 import *
#2021年12月30日13:56:22

class Test_creatUser没有结构性产品账号及申请结构性产品审批(unittest.TestCase):

    def setUp(self):
        self.creatUser = CreatUser无结构性产品用户创建()
        logging.info("初始化CreatUser")

    def test_01_applyClient用户资料提交用例校验(self):
        applyClient = self.creatUser.ApplyClinet资料提交()
        self.assertEqual(200, applyClient.status_code)
        self.assertEqual("OK", applyClient.json().get("msg"))
        print("已执行用例1===============================================================")

    def test_02_submitAudit提交审核(self):
        submitAudit = self.creatUser.SubmitAudit提交审核()
        self.assertEqual(200, submitAudit.status_code)
        self.assertEqual("操作成功", submitAudit.json().get("msg"))
        print("已执行用例2===============================================================")

    def test_03_operatingWorkFlowFirst提交锁(self):
        operatingWorkFlowFirst = self.creatUser.operatingWorkFlowFirst提交锁()
        self.assertEqual(200, operatingWorkFlowFirst.status_code)
        self.assertEqual("操作成功", operatingWorkFlowFirst.json().get("msg"))
        self.assertEqual("操作成功", operatingWorkFlowFirst.json().get("data")[0].get("operatingMessage"))
        print("已执行用例3===============================================================")

    def test_04_saveRiskAssessment风控评估提交(self):
        saveRiskAssessment = self.creatUser.saveRiskAssessment风控评估提交()
        self.assertEqual(200, saveRiskAssessment.status_code)
        self.assertEqual("操作成功", saveRiskAssessment.json().get("msg"))
        print("已执行用例4===============================================================")

    def test_05_operatingWorkFlow内部人员审核(self):
        operatingWorkFlow = self.creatUser.operatingWorkFlow内部人员审核()
        self.assertEqual(200, operatingWorkFlow.status_code)
        self.assertEqual("操作成功", operatingWorkFlow.json().get("msg"))
        self.assertEqual(True, operatingWorkFlow.json().get("data")[0].get("result"))
        print("已执行用例5===============================================================")

    def test_06_operatingWorkFlowNo不用锁定审核通过(self):
        operatingWorkFlowNo = self.creatUser.operatingWorkFlowNo不用锁定审核通过()
        self.assertEqual(200, operatingWorkFlowNo.status_code)
        self.assertEqual("操作成功", operatingWorkFlowNo.json().get("msg"))
        self.assertEqual(True, operatingWorkFlowNo.json().get("data")[0].get("result"))
        print("已执行用例6===============================================================")

    def test_07_operatingWorkFlowAgaint提交锁(self):
        operatingWorkFlowAgaint = self.creatUser.operatingWorkFlowAgain提交锁()
        self.assertEqual(200, operatingWorkFlowAgaint.status_code)
        self.assertEqual("操作成功", operatingWorkFlowAgaint.json().get("msg"))
        self.assertEqual("操作成功", operatingWorkFlowAgaint.json().get("data")[0].get("operatingMessage"))
        print("已执行用例7===============================================================")

    def test_08_batchOperatingWorkFlow批量生成账号确定(self):
        batchOperatingWorkFlow = self.creatUser.batchOperatingWorkFlow批量生成账号确定()
        self.assertEqual(200, batchOperatingWorkFlow.status_code)
        self.assertEqual("操作成功", batchOperatingWorkFlow.json().get("msg"))
        self.assertEqual(True, batchOperatingWorkFlow.json().get("data")[0].get("result"))
        print("已执行用例8===============================================================")

    def test_09_operatingWorkFlowThird提交锁(self):
        operatingWorkFlowThird = self.creatUser.operatingWorkFlowThird提交锁()
        self.assertEqual(200, operatingWorkFlowThird.status_code)
        self.assertEqual("操作成功", operatingWorkFlowThird.json().get("msg"))
        self.assertEqual("操作成功", operatingWorkFlowThird.json().get("data")[0].get("operatingMessage"))
        self.assertEqual(True, operatingWorkFlowThird.json().get("data")[0].get("result"))
        print("已执行用例9===============================================================")

    def test_10_batchOperatingWorkFlowEnd批量确认(self):
        batchOperatingWorkFlowEnd = self.creatUser.batchOperatingWorkFlowEnd批量确认()
        self.assertEqual(200, batchOperatingWorkFlowEnd.status_code)
        self.assertEqual("操作成功", batchOperatingWorkFlowEnd.json().get("msg"))
        self.assertEqual(True, batchOperatingWorkFlowEnd.json().get("data")[0].get("result"))
        print("已执行用例10===============================================================")

    def test_11_SQLCheckUser(self):
        global userinf
        userinf=datahandle(data_read('F:\\python\\EDDID_CDMS\\Data\\userdatainf_1.txt'))
        logging.info("从文本中读到的用户基本信息为：{}".format(userinf))
        SQLCheckUser=self.creatUser.SQLCheckUser()
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

        logging.info("已执行用例11，数据库校验已完成")
        print("已执行用例11===============================================================")

    def test_12_addAccountStructure增加结构性产品(self):
        addAccountStructure = self.creatUser.addAccountStructure增加结构性产品()
        self.assertEqual(200, addAccountStructure.status_code)
        self.assertEqual("操作成功", addAccountStructure.json().get("msg"))
        # self.assertEqual(True, addAccountStructure.json().get("data")[0].get("result"))
        print("已执行用例12===============================================================")

    def test_13_addAccountStructure结构性产品申请第一次审批(self):
        addAccountStructurenN = self.creatUser.addAccountStructure第一次审批()
        self.assertEqual(200, addAccountStructurenN.status_code)
        self.assertEqual("操作成功", addAccountStructurenN.json().get("msg"))
        # self.assertEqual(True, addAccountStructure.json().get("data")[0].get("result"))
        print("已执行用例13===============================================================")

    def test_14_addAccountStructure结构性产品申请第二次审批(self):
        addAccountStructureT= self.creatUser.addAccountStructure第二次审批()
        self.assertEqual(200, addAccountStructureT.status_code)
        self.assertEqual("操作成功", addAccountStructureT.json().get("msg"))
        # self.assertEqual(True, addAccountStructure.json().get("data")[0].get("result"))
        print("已执行用例14===============================================================")

    def test_15_SQLCheckcd_ac_struc_appl(self):
        SQLCheckcd_ac_struc_appl=self.creatUser.SQLCheckcd_ac_struc_appl()
        # 检验电话
        self.assertEqual(3, SQLCheckcd_ac_struc_appl[0][-1])
        # 检验邮箱
        # self.assertEqual(userinf[1], SQLCheckUser[0][15])
        # # 检验英文姓
        # self.assertEqual(userinf[3], SQLCheckUser[0][10])
        # # 检验英文名
        # self.assertEqual(userinf[2], SQLCheckUser[0][9])
        # # 检验中文姓名
        self.assertEqual(userinf[4], SQLCheckcd_ac_struc_appl[0][5])
        # # 检验身份证
        # self.assertEqual(userinf[5], SQLCheckUser[0][4])
        # # 检验称谓
        # self.assertEqual(userinf[6], SQLCheckUser[0][8])
        # #非空校验
        # self.assertIsNotNone(SQLCheckUser)
        # self.assertEqual("PERSONAL", SQLCheckUser[0][2])

        logging.info("已执行用例15，数据库校验已完成")
        print("已执行用例15===============================================================")


    def tearDown(self):
        a = 6
        time.sleep(a)
        logging.info("接口请求完成后，等待系统处理数据，等待{}秒".format(a))
