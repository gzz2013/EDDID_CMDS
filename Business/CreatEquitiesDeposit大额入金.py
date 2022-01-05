import requests
from Business.login import cdms_获取token
from Common.random_number import Randoms
import logging
import time
from Common.com_sql.eddid_data_select import *
from Config.cdms_config import *
from Common.check_accts import *

class CreatEquitiesDeposit大额入金():

    def createDeposit创建入金单(self):
        global clientId, depositAmount, eddidhost, token, s,accountCategory
        eddidhost = url
        token = cdms_获取token()
        s = requests.Session()
        # Randoms实例化
        #客户账号
        clientId = 11431
        #客户交易账号
        accountId=int(str(clientId)+'1110')
        # print("accountId",type(accountId),accountId)
        #根据交易账号查询账号类型
        Category=accountCategory(accountId)[0]
        depositAmount = Randoms().randomlargeAmount()
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        createDepositurl = eddidhost + "/api/funds/createDeposit"
        print("createWithdrawalurl:", createDepositurl)
        # logging.info("提交出金申请单时{}".format(createWithdrawalurl))
        data = {
            "clientId": clientId,
            "depositType": "online_bank_deposit",
            "remittanceBankName": "渣打银行(香港)有限公司 003",
            "remittanceBankCard": "32323232",
            "sibMobile": 'null',
            "depositAmount": depositAmount,
            "accountId": accountId,
            "accountCategory": Category,
            "remittanceBankCode": "003",
            "beneficiaryBankCode": "012",
            "beneficiaryBankName": "中国银行（香港）有限公司",
            "beneficiaryBankCard": "012-873-2-002063-5",
            "depositCurrency": "HKD",
            "applySource": 4,
            "fileList": [
                "/hzlc_20211101100818.jpg"
            ]
        }
        createDepositResp = s.post(url=createDepositurl, headers=headers, json=data)
        logging.info("步骤1接口'{}';请求参数为:{};响应结果为：'{}'".format(createDepositurl, data, createDepositResp.text))
        print("步骤1接口'{}';请求参数为:{};响应结果为：'{}'".format(createDepositurl, data, createDepositResp.text))
        return createDepositResp

    def operatingWorkFlowNo(self):
        global applyId
        applyId = cd_deposit(clientId, depositAmount)[0][0]
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
            "realAmount": depositAmount,
            # 提交前填写的银行卡号
            "realBankCard": "016-478-783313006",
            "realBankCode": "016",
            # 提交前选到的币种
            "realCurrency": "HKD",
            "valueDate": crvalueDate
        }
        auditDepositNoResp = s.post(url=auditDepositNourl, headers=headers, json=data)
        logging.info("步骤3接口'{}';请求参数为:{};响应结果为：'{}'".format(auditDepositNourl, data, auditDepositNoResp.text))
        print("步骤3接口'{}';请求参数为:{};响应结果为：'{}'".format(auditDepositNourl, data, auditDepositNoResp.text))
        return auditDepositNoResp

    def operatingWorkFlowTo(self):
        # global applyId
        # applyId = cd_deposit(clientId,depositAmount)[0][0]
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        operatingWorkFlowTourl = eddidhost + "/api/common/operatingWorkFlow"
        print("applyClienturl:", operatingWorkFlowTourl)
        # logging.info("提交申请单时注册用户手机号码为：{}".format(clientId))
        data = {
            "applyId": applyId,
            "workFlowCode": "depositApply",
            "controlCode": "LOCK"
        }
        operatingWorkFlowToResp = s.post(url=operatingWorkFlowTourl, headers=headers, json=data)
        logging.info("步骤4接口'{}';请求参数为:{};响应结果为：'{}'".format(operatingWorkFlowTourl, data, operatingWorkFlowToResp.text))
        print("步骤4接口'{}';请求参数为:{};响应结果为：'{}'".format(operatingWorkFlowTourl, data, operatingWorkFlowToResp.text))
        return operatingWorkFlowToResp

    def auditDeposit_comp_p(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        auditDeposit_comp_purl = eddidhost + "/api/funds/auditDeposit"
        print("applyClienturl:", auditDeposit_comp_purl)
        # logging.info("提交申请单时注册用户手机号码为：{}".format(clientId))
        # crvalueDate=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        data = {
            "applyId": applyId,
            "approvalResult": "COMP_PASS_7",
            "statusCode": "COMP_7",
            "fileList": [
                {
                    "file": "/hzlc_20211102180038.jpg",
                    "type": "user"
                }
            ],
            "depositType": "bank_transfer_deposit"
        }
        auditDeposit_comp_pResp = s.post(url=auditDeposit_comp_purl, headers=headers, json=data)
        logging.info("步骤5接口'{}';请求参数为:{};响应结果为：'{}'".format(auditDeposit_comp_purl, data, auditDeposit_comp_pResp.text))
        print("步骤5接口'{}';请求参数为:{};响应结果为：'{}'".format(auditDeposit_comp_purl, data, auditDeposit_comp_pResp.text))
        return auditDeposit_comp_pResp

    def get_current_state_deposit(self):

        cstate = gs_wrkflw_log(applyId)[0][3]
        print("数据库查询到当前流程状态cstate的值为{}".format(cstate))
        b = 20
        while cstate == "SYS_HANDLEING_7":
            time.sleep(20)
            # 获取当前时间时分秒
            # a = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print("当前状态为：系统处理中，流程等待！当前时间为：{},剩余等待{}次！".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), b))
            logging.info("当前状态为：系统处理中，流程等待！当前时间为：{},剩余等待{}次！".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), b))
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
        else:
            time.sleep(30)
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
    a = 1
    CreatDeposit = CreatEquitiesDeposit大额入金()
    for i in range(a):
        # 实例化CreatUser
        print("=====================================步骤1：", CreatDeposit.createDeposit创建入金单().text)
        time.sleep(10)
        print("=====================================步骤2：", CreatDeposit.operatingWorkFlowNo().text)
        time.sleep(10)
        print("=====================================步骤3：", CreatDeposit.auditDepositNo().text)
        time.sleep(10)
        print("=====================================步骤4：", CreatDeposit.get_current_state_deposit())
