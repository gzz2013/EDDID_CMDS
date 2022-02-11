# -*- coding:utf-8 -*-
import requests
from Business.H5.mobile_login import h5_caccessToken
from Business.login import cdms_获取token
from Common.random_number import Randoms
import logging
from Common.com_sql.eddid_data_select import *
import time
from Common.com_sql.eddid_data_select import *
from Config.cdms_config import *
from Common.data_文本读写 import *
from Common.check_accts import *


class Creat_h5_EDDAdeposit入金():


    #H5页面提交EDDA入金
    def H5_submit_EDDAdeposit(self):
        global clientId, tanceAmount,ac_id,H5requests
        #实例化requests
        H5requests = requests.Session()
        #登录获取H5页面token
        tokenh5 = h5_caccessToken()
        #通过文本读取转账交易账号,需要EDDA签约完成后才能操作EDDA入金

        com=datahandle(data_read('F:\\python\\EDDID_CDMS\\Data\\unableAcct.txt'))
        clientId = com[0]
        BankHolder=com[4]+' '+com[3]
        ac_id = datahandle(data_read('F:\\python\\EDDID_CDMS\\Data\\unableAcct.txt'))[1]
        #获取账号类型
        tradeAccountType = accountCategory(ac_id)[1]
        beneficiaryAccount = accountCategory(ac_id)[3]
        #生成开户银行账号
        tanceBankAccount = str(ac_id) + "3546"
        IdNumber=com[5]
        #随机生成转出金额
        tanceAmount = Randoms().randomAmount()
        #指定币种
        Currency='HKD'
        #根据币种和交易账户确定艾德收款银行账号
        bankAccountNumber=getbankAccountNumber(ac_id,Currency)
        print("获取到的收款银行账号为:{}".format(bankAccountNumber))
        headers = {
            "accept": "application/json, text/plain, */*",
            "authorization": "Bearer " + tokenh5,
            "content-type": "application/json;charset=utf-8",
            "accept-encoding": "gzip, deflate, br",
        }
        print("当前token为:{}".format(tokenh5))
        print("headers", headers)
        # closeAccturl = eddidhost + "/api/acct/closeAcct"
        H5submit_EDDADepositurl = app_base_url + "/open/account/fund/deposit/application"
        print("H5submit_EDDADepositurl为：", H5submit_EDDADepositurl)
        data = {
            "beneficiaryAccount":beneficiaryAccount,
            "depositType":"EDDA",
            "remittanceAmount":tanceAmount,
            "remittanceBankAccount":tanceBankAccount,
            "remittanceBankType":"SETTLEMENT_ACCOUNT",
            "remittanceCurrency":"HKD",
            "remittanceBankCode":"012",
            "remittanceBankName":"中国银行（香港）有限公司 012",
            "submitSource":"CP_H5",
            "tradeAccountNumber":ac_id,
            "tradeAccountType":tradeAccountType
        }
        print("data=", data)
        H5submit_EDDADepositesp = H5requests.post(url=H5submit_EDDADepositurl, headers=headers, json=data)
        logging.info("步骤1，EDDA入金提交接口'{}';请求参数为:{};的响应结果为:'{}'".format(H5submit_EDDADepositurl, data, H5submit_EDDADepositesp.text))
        print("步骤1，EDDA入金提交接口'{}';请求参数为:{};响应结果为:'{}'".format(H5submit_EDDADepositurl, data, H5submit_EDDADepositesp.text))
        return H5submit_EDDADepositesp

    def get_current_state_EDDAdeposit(self):
        global applyId
        s=requests.Session()
        eddidhost=url
        token = cdms_获取token()
        applyId = cd_deposit(clientId, tanceAmount)[0][0]
        statcde = gs_apply_work_flow(applyId)[0][3]
        print("gs_apply_work_flow数据库查询{},当前流程状态stat_cde的值为{}".format(applyId,statcde))
        # 如果系统处理中，一直循环不中断
        b = 20
        while statcde == "SYS_HANDLEING_7" or statcde == "SYS_HANDLEING_EDDA_7":
            time.sleep(20)
            print("当前状态为：系统处理中，流程等待！当前时间为：{},剩余等待{}次！".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), b))
            logging.info(
                "当前状态为：系统处理中，流程等待！当前时间为：{},剩余等待{}次！".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), b))
            statcde = gs_apply_work_flow(applyId)[0][3]
            print("数据库gs_apply_work_flow查询到当前流程状态stat_cde的值为{}".format(statcde))
            logging.info("数据库查询到当前流程状态stat_cde的值为{}".format(statcde))
            b -= 1
            if b < 0:
                print("系统处理时间过长，不再等待，进程结束！")
                break
        print("当前状态为：系统处理失败，流程继续！")

        # 如果当前状态为成功，不做任何操作，流程结束！
        if statcde == 'DONE_7':
            print("当前状态为成功，流程结束！")
            logging.info("当前状态为成功，流程结束！")
        # 如果返回的是系统处理失败，就再次锁定推进

        # 如果是系统处理失败，提交成功
        elif statcde == 'SYS_ERROR_7':
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
            operatingWorkFlowNourl = eddidhost + "/api/common/operatingWorkFlow"
            print("operatingWorkFlowNourl:", operatingWorkFlowNourl)
            data = {
                "applyId": applyId,
                "workFlowCode": "depositApply",
                "controlCode": "LOCK"
            }
            # 提交锁

            # 等待系统处理
            time.sleep(15)
            s.post(url=operatingWorkFlowNourl, headers=headers, json=data)
            print("####################################################已提第一次交锁！！")
            auditDepositTourl = eddidhost + "/api/funds/auditDeposit"
            print("applyClienturl:", auditDepositTourl)
            data = {
                "applyId":applyId,
                "approvalResult":"SYS_ERROR_PASS_7",
                "statusCode":"SYS_ERROR_7",
                "fileList":[

                ],
                "depositType":"edda"
            }
            operatingWorkFlowNoResp = s.post(url=auditDepositTourl, headers=headers, json=data)
            logging.info("步骤2接口'{}';请求参数为:{};响应结果为：'{}'".format(operatingWorkFlowNourl, data, operatingWorkFlowNoResp.text))
            print("步骤2接口'{}';请求参数为:{};响应结果为：'{}'".format(operatingWorkFlowNourl, data, operatingWorkFlowNoResp.text))

        # 如果是其他结果
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

        # 对于任意一种请求都不再校验接口请求结果，直接查询数据库进行校验
        sqlauditDepositNo = gs_apply_work_flow(applyId)

        logging.info("步骤2结束，查询到数据库gs_apply_work_flow,入参{}，结果为{}".format(applyId, sqlauditDepositNo))
        print("步骤2结束，查询到数据库gs_apply_work_flow,入参{}，结果为{}".format(applyId, sqlauditDepositNo))
        return sqlauditDepositNo

    def get_EDDAdeposit(self):

        EDDAdeposit = cd_deposit(clientId, tanceAmount)
        logging.info("步骤3结束，查询到数据库cd_deposit,入参clientId:{}，结果为{}".format(clientId, EDDAdeposit))
        print("步骤3结束，查询到数据库cd_deposit,入参clientId:{}，结果为{}".format(clientId, EDDAdeposit))
        return EDDAdeposit



if __name__ == "__main__":
    a = 1
    # 实例化Creat_h5_EDDADeposit入金()
    CreateEDDADeposit = Creat_h5_EDDAdeposit入金()
    for i in range(a):
        print("=====================================步骤1：", CreateEDDADeposit.H5_submit_EDDAdeposit().text)
        time.sleep(10)
        print("=====================================步骤2：", CreateEDDADeposit.get_current_state_EDDAdeposit())
