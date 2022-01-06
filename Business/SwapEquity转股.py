# -*- coding:utf-8 -*-
import requests
from Common.random_number import *
from Config.cdms_config import *
from Business.login import cdms_获取token
import logging
from Common.com_sql.eddid_data_select import *
from Common.data_文本读写 import *

class SwapEquity():

    def addEquitySwap(self):

        global token,headers,clientId,accountId,L,intNumber,s
        swapL=[]
        token = cdms_获取token()
        s = requests.Session()

        cookfront=cookfr
        clientId=11431
        accountId=114311110
        intNumber=Randoms().randomintNumber()
        swapL.append(intNumber)
        data_write('F:\\python\\EDDID_CDMS\\Data\\swapequity.txt', swapL)
        print("记录数据的文件名为：swapequity.txt，写入数据为:{}".format(swapL))
        logging.info("记录数据的文件名为：swapequity.txt，写入数据为:{}".format(swapL))
        headers={
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": cookfront + token
        }
        Swapurl= url+"/api/client/equity/swap/addEquitySwap"
        data={
            "clientId":"11431",
            "accountId":"114311110",
            "clientName":"NAMEtrtr6 TETS46",
            "brokerAccountId":"3333312",
            "marketCode":"XHKG",
            "type":"SI IN",
            "brokerNo":"1078",
            "brokerName":"渣打证券(香港)有限公司",
            "brokerLiaison":"甘杰祥",
            "brokerPhone":"39838439",
            "securitiesInfoList":[
                {
                    "securitiesCode":"00001",
                    "securitiesName":"长和",
                    "securitiesNumber":intNumber,
                    "realSecuritiesNumber":"",
                    "securitiesCharge":"",
                    "settlementCurrency":"",
                    "currency":""
                }
            ],
            "applyFileList":[]
        }
        SwapRespo=s.post(url=Swapurl,headers=headers,json=data)
        logging.info("步骤1,转股申请提交，接口：'{}';请求参数为:{};响应结果为：'{}'".format(Swapurl, data, SwapRespo.text))
        print("步骤1,转股申请提交，接口：'{}';请求参数为:{};响应结果为：'{}'".format(Swapurl, data, SwapRespo.text))
        return SwapRespo


    def OperatingWorkFlowon(self):

        global applyId
        applyId=cd_clnt_equity_swap(accountId)[0][0]

        logging.info("通过查询数据库查询到applyid为：'{}'".format(applyId))
        print("通过查询数据库查询到applyid为：'{}'".format(applyId))
        data={
            "applyId":applyId,
            "workFlowCode":"equitySwapInApply",
            "controlCode":"LOCK"
        }
        OperatingWorkFlowonurl=url+"/api/common/newOperatingWorkFlow"
        OperatingWorkFlowonRespo=s.post(url=OperatingWorkFlowonurl,headers=headers,json=data)
        logging.info("步骤2,第一次提交锁，接口：'{}';请求参数为:{};响应结果为：'{}'".format(OperatingWorkFlowonurl, data, OperatingWorkFlowonRespo.text))
        print("步骤2,第一次提交锁，接口：'{}';请求参数为:{};响应结果为：'{}'".format(OperatingWorkFlowonurl, data, OperatingWorkFlowonRespo.text))
        return OperatingWorkFlowonRespo



    def OperatingWorkFlowCS2(self):

        OperatingWorkFlowCS2url=url +"/api/common/newOperatingWorkFlow"
        data={
            "applyId":applyId,
            "workFlowCode":"equitySwapInApply",
            "controlCode":"PASS",
            "applyFileList":[

            ]
        }
        OperatingWorkFlowCS2Respo = s.post(url=OperatingWorkFlowCS2url, headers=headers, json=data)
        logging.info("步骤3,CS2审核通过，接口：'{}';请求参数为:{};响应结果为：'{}'".format(OperatingWorkFlowCS2url, data, OperatingWorkFlowCS2Respo.text))
        print("步骤3,CS2审核通过，接口：'{}';请求参数为:{};响应结果为：'{}'".format(OperatingWorkFlowCS2url, data, OperatingWorkFlowCS2Respo.text))
        return OperatingWorkFlowCS2Respo

    def OperatingWorkFlowtwo(self):

        logging.info("通过查询数据库查询到applyid为：'{}'".format(applyId))
        print("通过查询数据库查询到applyid为：'{}'".format(applyId))
        data={
            "applyId":applyId,
            "workFlowCode":"equitySwapInApply",
            "controlCode":"LOCK"
        }
        OperatingWorkFlowtwourl=url+"/api/common/newOperatingWorkFlow"
        OperatingWorkFlowtwoRespo=s.post(url=OperatingWorkFlowtwourl,headers=headers,json=data)
        logging.info("步骤4,第二次提交锁，接口：'{}';请求参数为:{};响应结果为：'{}'".format(OperatingWorkFlowtwourl, data, OperatingWorkFlowtwoRespo.text))
        print("步骤4,第二次提交锁，接口：'{}';请求参数为:{};响应结果为：'{}'".format(OperatingWorkFlowtwourl, data, OperatingWorkFlowtwoRespo.text))
        return OperatingWorkFlowtwoRespo

    def OperatingWorkFlowSETL(self):

        OperatingWorkFlowSETLurl=url +"/api/common/newOperatingWorkFlow"
        data={
            "applyId":applyId,
            "workFlowCode":"equitySwapInApply",
            "controlCode":"PASS",
            "applyFileList":[

            ],
            "securitiesInfoList":[
                {
                    "securitiesCode":"00001",
                    "securitiesName":"长和",
                    "securitiesNumber":intNumber,
                    "realSecuritiesNumber":"0",
                    "securitiesCharge":"",
                    "settlementCurrency":"",
                    "currency":"HKD",
                    "status":"",
                    "flag":"true",
                    "refuseReasons":"",
                    "marketValue":""
                }
            ]
        }
        OperatingWorkFlowSETRespo = s.post(url=OperatingWorkFlowSETLurl, headers=headers, json=data)
        logging.info("步骤5,SETL审核通过，接口：'{}';请求参数为:{};响应结果为：'{}'".format(OperatingWorkFlowSETLurl, data, OperatingWorkFlowSETRespo.text))
        print("步骤5,SETL审核通过，接口：'{}';请求参数为:{};响应结果为：'{}'".format(OperatingWorkFlowSETLurl, data, OperatingWorkFlowSETRespo.text))
        return OperatingWorkFlowSETRespo

    def sql_cd_clnt_equity_swap_item(self):
        equity_swap_item=cd_clnt_equity_swap_item(applyId)
        logging.info("步骤6,通过applyid:{}查询数据库cd_clnt_equity_swap_item，查询结果为：'{}'".format(applyId,equity_swap_item))
        print("步骤6,通过applyid:{}查询数据库cd_clnt_equity_swap_item，查询结果为：'{}'".format(applyId,equity_swap_item))
        return equity_swap_item

if __name__=="__main__":
    a = 1
    EquitySwap = SwapEquity()

    for i in range(a):
        # 实例化CreatUser
        print("=====================================步骤1：", EquitySwap.addEquitySwap().text)
        time.sleep(8)
        print("=====================================步骤2：", EquitySwap.OperatingWorkFlowon().text)
        time.sleep(5)
        print("=====================================步骤3：", EquitySwap.OperatingWorkFlowCS2().text)
        time.sleep(5)
        print("=====================================步骤4：", EquitySwap.OperatingWorkFlowtwo().text)
        time.sleep(5)
        print("=====================================步骤5：", EquitySwap.OperatingWorkFlowSETL().text)
        time.sleep(5)