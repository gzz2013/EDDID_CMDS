import unittest
import time
import logging
from Business.updateClientInfo import updateClientInfo
from Common.data_文本读写 import data_read,datahandle

class Test_UpdateClientInfo修改用户资料及审批(unittest.TestCase):

    def setUp(self):
        self.UpdateClientInfo = updateClientInfo()
        logging.info("updateClientInfo方法实例化完成")

    def test_01_updateClientInfo(self):
        updateClientInfo = self.UpdateClientInfo.updateClientInfo()
        self.assertEqual(updateClientInfo.status_code, 200)
        self.assertEqual(updateClientInfo.json().get("msg"), "操作成功")

    def test_02_operatingWorkFlowonce(self):
        operatingWorkFlowonce = self.UpdateClientInfo.operatingWorkFlowonce()
        self.assertEqual(operatingWorkFlowonce.status_code, 200)
        self.assertEqual(operatingWorkFlowonce.json().get("msg"), "操作成功")
        self.assertEqual(operatingWorkFlowonce.json().get("data")[0].get("operatingMessage"),"操作成功")

    def test_03_OperatingWorkFlowCS2(self):
        OperatingWorkFlowCS2 = self.UpdateClientInfo.operatingWorkFlowCS2()
        self.assertEqual(OperatingWorkFlowCS2.status_code, 200)
        self.assertEqual(OperatingWorkFlowCS2.json().get("msg"), "操作成功")

    def test_04_OperatingWorkFlowOR(self):
        operatingWorkFlowOR = self.UpdateClientInfo.operatingWorkFlowOR()
        self.assertEqual(operatingWorkFlowOR.status_code, 200)
        self.assertEqual(operatingWorkFlowOR.json().get("msg"), "操作成功")

    def test_05_operatingWorkFlowtwo(self):
        operatingWorkFlowtwo = self.UpdateClientInfo.operatingWorkFlowtwo()
        self.assertEqual(operatingWorkFlowtwo.status_code, 200)
        self.assertEqual(operatingWorkFlowtwo.json().get("msg"), "操作成功")
        self.assertEqual(operatingWorkFlowtwo.json().get("data")[0].get("operatingMessage"),"操作成功")

    def test_06_OperatingWorkFlowCLER(self):
        operatingWorkFlowCLER = self.UpdateClientInfo.operatingWorkFlowCLER()
        self.assertEqual(operatingWorkFlowCLER.status_code, 200)
        self.assertEqual(operatingWorkFlowCLER.json().get("msg"), "操作成功")

    def test_07_sql_cd_enty(self):
        sql_cd_enty=self.UpdateClientInfo.sql_cd_enty()
        txtdata=datahandle(data_read('F:\\python\\EDDID_CDMS\\Data\\updateClient.txt'))
        #校验邮箱
        self.assertEqual(sql_cd_enty[0][15],txtdata[0])
        #校验身份证号
        self.assertEqual(int(sql_cd_enty[0][4]),int(txtdata[1]))


    def tearDown(self):
        a = 6
        time.sleep(a)
        logging.info("接口请求完成后，等待系统处理数据，等待{}秒".format(a))