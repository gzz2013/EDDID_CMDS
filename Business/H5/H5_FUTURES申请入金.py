# -*- coding:utf-8 -*-
import requests
from Business.H5.mobile_login import h5_caccessToken
from Business.login import cdms_获取token
from Common.random_number import Randoms
import logging
from Common.com_sql.eddid_data_update import *
import time
from Common.com_sql.eddid_data_select import *
from Config.cdms_config import *
from Common.data_文本读写 import *


class Creat_h5_deposit():

    # 步骤1,H5页面提交入金申请
    def H5submit_deposit(self):
        global clientId,tanceAmount
        tokenh5=h5_caccessToken()
        H5requests = requests.Session()

        clientId="501098"

        tanceAmount = Randoms().randomAmount()
        headers = {
            "accept": "application/json, text/plain, */*",
            "authorization": "Bearer "+ tokenh5,
            "content-type": "application/json;charset=utf-8",
            "accept-encoding": "gzip, deflate, br",
        }
        print("当前token为:{}".format(tokenh5))
        print("headers", headers)
        # closeAccturl = eddidhost + "/api/acct/closeAcct"
        H5submitdepositurl = app_base_url + "/open/account/fund/deposit/application"
        print("H5submitmrktdaturl为：", H5submitdepositurl)
        data = {
            "beneficiaryAccount":"016-478-000324487",
            "depositImages":[
                "4e70f72d-6ebc-48dd-abfb-d8e50723358e.jpg"
            ],
            "depositType":"ATM_TRANSFER_DEPOSIT",
            "remittanceAmount":tanceAmount,
            "remittanceBankAccount":"658899",
            "remittanceBankCode":"024",
            "remittanceBankType":"OTHER",
            "remittanceCurrency":"HKD",
            "submitSource":"CP_H5",
            "tradeAccountNumber":"5010983210",
            "tradeAccountType":"FUTURES_MARGIN"
        }
        print("data=", data)
        H5submitdeposiResp = H5requests.post(url=H5submitdepositurl, headers=headers, json=data)
        logging.info("步骤1提交接口'{}';请求参数为:{};的响应结果为:'{}'".format(H5submitdepositurl, data, H5submitdeposiResp.text))
        print("步骤1提交接口'{}';请求参数为:{};响应结果为:'{}'".format(H5submitdepositurl, data, H5submitdeposiResp.text))
        return H5submitdeposiResp

    def operatingWorkFlowNo(self):
        global applyId,token,eddidhost,s
        #web端的请求体
        s=requests.Session()
        token=cdms_获取token()
        eddidhost=url

        applyId = cd_deposit(clientId,tanceAmount)[0][0]
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        operatingWorkFlowurl = eddidhost + "/api/common/operatingWorkFlow"
        print("applyClienturl:", operatingWorkFlowurl)
        # logging.info("提交申请单时注册用户手机号码为：{}".format(clientId))
        data = {
            "applyId": applyId,
            "workFlowCode": "depositApply",
            "controlCode": "LOCK"
        }
        operatingWorkFlowNoResp = s.post(url=operatingWorkFlowurl, headers=headers, json=data)
        logging.info("步骤2接口'{}';请求参数为:{};响应结果为：'{}'".format(operatingWorkFlowurl, data, operatingWorkFlowNoResp.text))
        print("步骤2接口'{}';请求参数为:{};响应结果为：'{}'".format(operatingWorkFlowurl, data, operatingWorkFlowNoResp.text))
        return operatingWorkFlowNoResp

    def auditDepositNo(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        auditDepositNourl = eddidhost + "/api/funds/auditDeposit"
        print("applyClienturl:", auditDepositNourl)
        # logging.info("提交申请单时注册用户手机号码为：{}".format(clientId))

        crvalueDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        data = {
            "applyId": applyId,
            "approvalResult": "CS2_PASS_7",
            "statusCode": "CS2_7",
            "fileList": [
                {
                    "file": "/hzlc_20211101100818.jpg",
                    "type": "user"
                }
            ],
            "depositType": "online_bank_deposit",
            # 提交前填写的金额
            "realAmount": tanceAmount,
            # 提交前填写的银行卡号
            "realBankCard": "012-873-2-002063-5",
            "realBankCode": "016",
            # 提交前选到的币种
            "realCurrency": "HKD",
            "valueDate": crvalueDate
        }
        auditDepositNoResp = s.post(url=auditDepositNourl, headers=headers, json=data)
        logging.info("步骤3接口'{}';请求参数为:{};响应结果为：'{}'".format(auditDepositNourl, data, auditDepositNoResp.text))
        print("步骤3接口'{}';请求参数为:{};响应结果为：'{}'".format(auditDepositNourl, data, auditDepositNoResp.text))
        return auditDepositNoResp

    def get_current_state_deposit(self):

        cstate = gs_wrkflw_log(applyId)[0][3]
        print("数据库查询到当前流程状态cstate的值为{}".format(cstate))
        # 如果系统处理中，一直循环不中断
        b = 20
        while cstate == "SYS_HANDLEING_7":
            time.sleep(20)
            print("当前状态为：系统处理中，流程等待！当前时间为：{},剩余等待{}次！".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), b))
            logging.info(
                "当前状态为：系统处理中，流程等待！当前时间为：{},剩余等待{}次！".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), b))
            cstate = gs_wrkflw_log(applyId)[0][3]
            print("数据库查询到当前流程状态cstate的值为{}".format(cstate))
            logging.info("数据库查询到当前流程状态cstate的值为{}".format(cstate))
            b -= 1
            if b < 0:
                print("系统处理时间过长，不再等待，进程结束！")
                break
        print("当前状态为：系统处理失败，流程继续！")

        # 如果当前状态为成功，不做任何操作，流程结束！
        if cstate == 'DONE_7':
            print("当前状态为成功，流程结束！")
            logging.info("当前状态为成功，流程结束！")
        # 如果返回的是系统处理失败，就再次锁定推进

        # 如果是CLER处理中
        elif cstate == 'CLER_HANDLEING_7':
            time.sleep(15)
            headers = {
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Connection": "keep-alive",
                "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
            }

            # 系统处理出金返回结果后，首先提交锁
            logging.info("当前token为:{}".format(token))
            print("当前token为:{}".format(token))
            print("headers", headers)
            operatingWorkFlowTourl = eddidhost + "/api/common/operatingWorkFlow"
            print("applyClienturl:", operatingWorkFlowTourl)
            data = {
                "applyId": applyId,
                "workFlowCode": "depositApply",
                "controlCode": "LOCK"
            }
            # 提交锁

            # 等待系统处理
            time.sleep(15)
            s.post(url=operatingWorkFlowTourl, headers=headers, json=data)
            print("####################################################已提交锁！！")
            auditDepositTourl = eddidhost + "/api/funds/auditDeposit"
            print("applyClienturl:", auditDepositTourl)
            data = {
                "applyId": applyId,
                "approvalResult": "CLER_HANDLEING_PASS_7",
                "statusCode": "CLER_HANDLEING_7",
                "fileList": [
                    {
                        "file": "/hzlc_20211101100818.jpg",
                        "type": "user"
                    }
                ],
                "depositType": "online_bank_deposit"
            }
            auditDepositToResp = s.post(url=auditDepositTourl, headers=headers, json=data)
            logging.info("步骤4接口'{}';请求参数为:{};响应结果为：'{}'".format(auditDepositTourl, data, auditDepositToResp.text))
            print("步骤4接口'{}';请求参数为:{};响应结果为：'{}'".format(auditDepositTourl, data, auditDepositToResp.text))
            # return auditDepositToResp
        # 如果是系统处理失败
        else:
            time.sleep(15)
            headers = {
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Connection": "keep-alive",
                "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
            }

            # 系统处理出金返回结果后，首先提交锁
            logging.info("当前token为:{}".format(token))
            print("当前token为:{}".format(token))
            print("headers", headers)
            operatingWorkFlowTourl = eddidhost + "/api/common/operatingWorkFlow"
            print("applyClienturl:", operatingWorkFlowTourl)
            data = {
                "applyId": applyId,
                "workFlowCode": "depositApply",
                "controlCode": "LOCK"
            }
            # 提交锁

            # 等待系统处理
            time.sleep(15)
            s.post(url=operatingWorkFlowTourl, headers=headers, json=data)
            print("####################################################已提交锁！！")
            auditDepositTourl = eddidhost + "/api/funds/auditDeposit"
            print("applyClienturl:", auditDepositTourl)
            data = {
                "applyId": applyId,
                "approvalResult": "SYS_ERROR_PASS_7",
                "statusCode": "SYS_ERROR_7",
                "fileList": [
                    {
                        "file": "/hzlc_20211101100818.jpg",
                        "type": "user"
                    }
                ],
                "depositType": "online_bank_deposit"
            }
            auditDepositToResp = s.post(url=auditDepositTourl, headers=headers, json=data)
            logging.info("步骤4接口'{}';请求参数为:{};响应结果为：'{}'".format(auditDepositTourl, data, auditDepositToResp.text))
            print("步骤4接口'{}';请求参数为:{};响应结果为：'{}'".format(auditDepositTourl, data, auditDepositToResp.text))
            # return auditDepositToResp

        sqlauditDepositTo=gs_wrkflw_log(applyId)[0]

        logging.info("步骤4结束，查询到数据库gs_wrkflw_log,入参{}，结果为{}".format(applyId,sqlauditDepositTo))
        print("步骤4结束，查询到数据库gs_wrkflw_log,入参{}，结果为{}".format(applyId,sqlauditDepositTo))
        return sqlauditDepositTo



if __name__ == "__main__":
    Creat_h5_deposit=Creat_h5_deposit()
    print("步骤1，app提交出金申请",Creat_h5_deposit.H5submit_deposit().text)
    time.sleep(7)
    print("步骤2，第一次提交锁", Creat_h5_deposit.operatingWorkFlowNo().text)
    time.sleep(7)
    print("步骤3，CS2审批通过", Creat_h5_deposit.auditDepositNo().text)
    time.sleep(7)
    print("步骤4，根据状态审核通过", Creat_h5_deposit.get_current_state_deposit())



