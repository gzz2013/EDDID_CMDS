import requests
from Business.login import cdms_获取token
from Common.random_number import Randoms
import logging
import time
from Common.com_sql.eddid_data_select import *
from Config.cdms_config import *
from Common.check_accts import *

class CreatEquitiesWithdrawal出金():

    def createWithdrawal创建出金单(self):
        global clientId, withdrawalAmount, eddidhost,token,s
        eddidhost = url
        token = cdms_获取token()
        s = requests.Session()
        clientId=88659
        accountId = 886591280
        Category = accountCategory(accountId)[0]
        print("================================获取到clientId为：{}，accountId为：{}".format(clientId, accountId))
        withdrawalAmount = Randoms().randomAmount()
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        createWithdrawalurl = eddidhost + "/api/funds/createWithdrawal"
        print("createWithdrawalurl:", createWithdrawalurl)
        data={
            "clientId":clientId,
            "actualAmountCurrency":"HKD",
            "withdrawalAmount":withdrawalAmount,
            "accountId":accountId,
            "accountCategory":Category,
            "clientBankAccountId":"1273",
            "withdrawalType":"LOCAL",
            "applySource":4,
            "fileList":[
                "/hzlc_20220106091854.jpg"
            ],
            "serviceCurrency":"HKD",
            "serviceCharge":0,
            "actualAmount":withdrawalAmount,
            "feeList":[

            ]
        }
        createWithdrawalResp = s.post(url=createWithdrawalurl, headers=headers, json=data)
        logging.info("步骤1接口'{}';请求参数为:{};响应结果为：'{}'".format(createWithdrawalurl, data, createWithdrawalResp.text))
        print("步骤1接口'{}';请求参数为:{};响应结果为：'{}'".format(createWithdrawalurl, data, createWithdrawalResp.text))
        return createWithdrawalResp

    def operatingWorkFlowNo(self):
        global applyId
        applyId = cd_withdrawal(clientId, withdrawalAmount)[0][0]
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
        data = {
            "applyId": applyId,
            "workFlowCode": "withdrawalApply",
            "controlCode": "LOCK"
        }
        operatingWorkFlowNoResp = s.post(url=operatingWorkFlowurl, headers=headers, json=data)
        logging.info("步骤2接口'{}';请求参数为:{};响应结果为：'{}'".format(operatingWorkFlowurl, data, operatingWorkFlowNoResp.text))
        print("步骤2接口'{}';请求参数为:{};响应结果为：'{}'".format(operatingWorkFlowurl, data, operatingWorkFlowNoResp.text))
        return operatingWorkFlowNoResp

    def auditWithdrawalNo(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        auditWithdrawalurl = eddidhost + "/api/funds/auditWithdrawal"
        print("applyClienturl:", auditWithdrawalurl)
        # logging.info("提交申请单时注册用户手机号码为：{}".format(clientId))
        data = {
            "applyId": applyId,
            "approvalResult": "CS2_PASS_8",
            "fileList": [
                {
                    "file": "/hzlc_20211025162042.jpg",
                    "type": "user"
                }
            ],
            "statusCode": "CS2_8",
            "clientBankAccountName": "521423"
        }
        auditWithdrawalResp = s.post(url=auditWithdrawalurl, headers=headers, json=data)
        logging.info("步骤3接口'{}';请求参数为:{};响应结果为：'{}'".format(auditWithdrawalurl, data, auditWithdrawalResp.text))
        print("步骤3接口'{}';请求参数为:{};响应结果为：'{}'".format(auditWithdrawalurl, data, auditWithdrawalResp.text))
        return auditWithdrawalResp

    def operatingWorkFlowTO(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        operatingWorkFlowtourl = eddidhost + "/api/common/operatingWorkFlow"
        print("applyClienturl:", operatingWorkFlowtourl)
        # logging.info("提交申请单时注册用户手机号码为：{}".format(clientId))
        data = {
            "applyId": applyId,
            "workFlowCode": "withdrawalApply",
            "controlCode": "LOCK"
        }
        operatingWorkFlowTOResp = s.post(url=operatingWorkFlowtourl, headers=headers, json=data)
        logging.info("步骤4接口'{}';请求参数为:{};响应结果为：'{}'".format(operatingWorkFlowtourl, data, operatingWorkFlowTOResp.text))
        print("步骤4接口'{}';请求参数为:{};响应结果为：'{}'".format(operatingWorkFlowtourl, data, operatingWorkFlowTOResp.text))
        return operatingWorkFlowTOResp

    def auditWithdrawalTo(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        auditWithdrawalTourl = eddidhost + "/api/funds/auditWithdrawal"
        print("applyClienturl:", auditWithdrawalTourl)
        # logging.info("提交申请单时注册用户手机号码为：{}".format(clientId))
        data = {
            "applyId": applyId,
            "approvalResult": "CLER_PASS_8",
            "fileList": [
                {
                    "file": "/hzlc_20211025162042.jpg",
                    "type": "user"
                }
            ],
            "statusCode": "CLER_8",
            "clientBankAccountName": "521423"
        }
        auditWithdrawalToResp = s.post(url=auditWithdrawalTourl, headers=headers, json=data)
        logging.info("步骤5接口'{}';请求参数为:{};响应结果为：'{}'".format(auditWithdrawalTourl, data, auditWithdrawalToResp.text))
        print("步骤5接口'{}';请求参数为:{};响应结果为：'{}'".format(auditWithdrawalTourl, data, auditWithdrawalToResp.text))
        time.sleep(20)
        return auditWithdrawalToResp

    def get_current_state(self):

        cstate = gs_wrkflw_log(applyId)[0][3]
        print("数据库查询到当前流程状态cstate的值为{}".format(cstate))
        b = 20
        while cstate == "SYS_HANDLEING_8":
            time.sleep(20)
            # 获取当前时间时分秒
            # a = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
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

        # 系统处理出金返回结果后，首先提交锁
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        operatingWorkFlowsurl = eddidhost + "/api/common/operatingWorkFlow"
        print("applyClienturl:", operatingWorkFlowsurl)
        dataT = {
            "applyId": applyId,
            "workFlowCode": "withdrawalApply",
            "controlCode": "LOCK"
        }
        s.post(url=operatingWorkFlowsurl, headers=headers, json=dataT)
        time.sleep(10)
        print("系统处理出金返回结果后，首先提交锁++++++++++++++++++++++++++++")

        # 如果返回的是系统处理失败，就审批通过
        if cstate == 'SYS_ERROR_8':
            headers = {
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Connection": "keep-alive",
                "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
            }
            logging.info("当前token为:{}".format(token))
            print("当前token为:{}".format(token))
            print("headers", headers)
            auditWithdrawalErrorPassurl = eddidhost + "/api/funds/auditWithdrawal"
            print("applyClienturl:", auditWithdrawalErrorPassurl)
            # logging.info("提交申请单时注册用户手机号码为：{}".format(clientId))
            data = {
                "applyId": applyId,
                "approvalResult": "SYS_ERROR_PASS_8",
                "fileList": [
                    {
                        "file": "/hzlc_20211025162042.jpg",
                        "type": "user"
                    }
                ],
                "statusCode": "SYS_ERROR_8",
                "clientBankAccountName": "521423"
            }

            time.sleep(15)
            s.post(url=auditWithdrawalErrorPassurl, headers=headers, json=data)

            print("如果返回的是系统处理失败，就审批通过++++++++++++++++++++++++++++")
            # logging.info("步骤5接口'{}';请求参数为:{};响应结果为：'{}'".format(auditWithdrawalErrorPassurl, data,
            #                                                     auditWithdrawalPassResp.text))
            # print("步骤5接口'{}';请求参数为:{};响应结果为：'{}'".format(auditWithdrawalErrorPassurl, data,
            #                                           auditWithdrawalPassResp.text))
            time.sleep(10)
            # 再次锁定
            dataT = {
                "applyId": applyId,
                "workFlowCode": "withdrawalApply",
                "controlCode": "LOCK"
            }
            s.post(url=operatingWorkFlowsurl, headers=headers, json=dataT)

            time.sleep(15)
            auditWithdrawalRoPassurl = eddidhost + "/api/funds/auditWithdrawal"
            print("applyClienturl:", auditWithdrawalRoPassurl)
            # logging.info("提交申请单时注册用户手机号码为：{}".format(clientId))
            data = {
                "applyId": applyId,
                "approvalResult": "RO_PASS_8",
                "fileList": [
                    {
                        "file": "/hzlc_20211025162042.jpg",
                        "type": "user"
                    }
                ],
                "statusCode": "RO_8",
                "clientBankAccountName": "521423"
            }

            print("系统处理失败后，再次成功时，再次提交锁++++++++++++++++++++++++++++")
            auditWithdrawalPassResp = s.post(url=auditWithdrawalRoPassurl, headers=headers, json=data)
            # logging.info(
            #     "步骤5接口'{}';请求参数为:{};响应结果为：'{}'".format(auditWithdrawalRoPassurl, data, auditWithdrawalPassResp.text))
            print("再次锁定接口'{}';请求参数为:{};响应结果为：'{}'".format(auditWithdrawalRoPassurl, data, auditWithdrawalPassResp.text))
        else:
            headers = {
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Connection": "keep-alive",
                "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
            }
            logging.info("当前token为:{}".format(token))
            print("当前token为:{}".format(token))
            print("headers", headers)
            auditWithdrawalRoPassurl = eddidhost + "/api/funds/auditWithdrawal"
            print("applyClienturl:", auditWithdrawalRoPassurl)
            # logging.info("提交申请单时注册用户手机号码为：{}".format(clientId))
            data = {
                "applyId": applyId,
                "approvalResult": "RO_PASS_8",
                "fileList": [
                    {
                        "file": "/hzlc_20211025162042.jpg",
                        "type": "user"
                    }
                ],
                "statusCode": "RO_8",
                "clientBankAccountName": "521423"
            }
            time.sleep(20)
            auditWithdrawalPassResp = s.post(url=auditWithdrawalRoPassurl, headers=headers, json=data)
            print("系统处理成功时到”待RO审批“，审批通过++++++++++++++++++++++++++++")

        logging.info(
            "步骤6接口'{}';请求参数为:{};响应结果为：'{}'".format(auditWithdrawalRoPassurl, data, auditWithdrawalPassResp.text))
        print("步骤6接口'{}';请求参数为:{};响应结果为：'{}'".format(auditWithdrawalRoPassurl, data, auditWithdrawalPassResp.text))
        return auditWithdrawalPassResp

    def operatingWorkFlowThird(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        operatingWorkFlowThirdurl = eddidhost + "/api/common/operatingWorkFlow"
        print("applyClienturl:", operatingWorkFlowThirdurl)
        # logging.info("提交申请单时注册用户手机号码为：{}".format(clientId))
        data = {
            "applyId": applyId,
            "workFlowCode": "withdrawalApply",
            "controlCode": "LOCK"
        }
        operatingWorkFlowThirdResp = s.post(url=operatingWorkFlowThirdurl, headers=headers, json=data)
        logging.info(
            "步骤4接口'{}';请求参数为:{};响应结果为：'{}'".format(operatingWorkFlowThirdurl, data, operatingWorkFlowThirdResp.text))
        print("步骤4接口'{}';请求参数为:{};响应结果为：'{}'".format(operatingWorkFlowThirdurl, data, operatingWorkFlowThirdResp.text))
        return operatingWorkFlowThirdResp

    def auditWithdrawalErrorPass(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        auditWithdrawalErrorPassurl = eddidhost + "/api/funds/auditWithdrawal"
        print("applyClienturl:", auditWithdrawalErrorPassurl)
        # logging.info("提交申请单时注册用户手机号码为：{}".format(clientId))
        data = {
            "applyId": applyId,
            "approvalResult": "SYS_ERROR_PASS_8",
            "fileList": [
                {
                    "file": "/hzlc_20211025162042.jpg",
                    "type": "user"
                }
            ],
            "statusCode": "SYS_ERROR_8",
            "clientBankAccountName": "521423"
        }
        auditWithdrawalErrorPassResp = s.post(url=auditWithdrawalErrorPassurl, headers=headers, json=data)
        logging.info("步骤5接口'{}';请求参数为:{};响应结果为：'{}'".format(auditWithdrawalErrorPassurl, data,
                                                            auditWithdrawalErrorPassResp.text))
        print("步骤5接口'{}';请求参数为:{};响应结果为：'{}'".format(auditWithdrawalErrorPassurl, data,
                                                     auditWithdrawalErrorPassResp.text))
        return auditWithdrawalErrorPassResp

    def auditWithdrawalRoPass(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        auditWithdrawalRoPassurl = eddidhost + "/api/funds/auditWithdrawal"
        print("applyClienturl:", auditWithdrawalRoPassurl)
        # logging.info("提交申请单时注册用户手机号码为：{}".format(clientId))
        data = {
            "applyId": applyId,
            "approvalResult": "RO_PASS_8",
            "fileList": [
                {
                    "file": "/hzlc_20211025162042.jpg",
                    "type": "user"
                }
            ],
            "statusCode": "RO_8",
            "clientBankAccountName": "521423"
        }
        auditWithdrawalRoPassResp = s.post(url=auditWithdrawalRoPassurl, headers=headers, json=data)
        logging.info(
            "步骤5接口'{}';请求参数为:{};响应结果为：'{}'".format(auditWithdrawalRoPassurl, data, auditWithdrawalRoPassResp.text))
        print("步骤5接口'{}';请求参数为:{};响应结果为：'{}'".format(auditWithdrawalRoPassurl, data, auditWithdrawalRoPassResp.text))
        return auditWithdrawalRoPassResp

    def operatingWorkFlowfourth(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        operatingWorkFlowfourthurl = eddidhost + "/api/common/operatingWorkFlow"
        print("applyClienturl:", operatingWorkFlowfourthurl)
        # logging.info("提交申请单时注册用户手机号码为：{}".format(clientId))
        data = {
            "applyId": applyId,
            "workFlowCode": "withdrawalApply",
            "controlCode": "LOCK"
        }
        operatingWorkFlowfourthResp = s.post(url=operatingWorkFlowfourthurl, headers=headers, json=data)
        logging.info(
            "步骤7接口'{}';请求参数为:{};响应结果为：'{}'".format(operatingWorkFlowfourthurl, data, operatingWorkFlowfourthResp.text))
        print(
            "步骤7接口'{}';请求参数为:{};响应结果为：'{}'".format(operatingWorkFlowfourthurl, data, operatingWorkFlowfourthResp.text))
        return operatingWorkFlowfourthResp

    def auditWithdrawalAcctPass(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        auditWithdrawalAcctPassurl = eddidhost + "/api/funds/auditWithdrawal"
        print("applyClienturl:", auditWithdrawalAcctPassurl)
        # logging.info("提交申请单时注册用户手机号码为：{}".format(clientId))
        data = {
            "applyId": applyId,
            "approvalResult": "ACCT_PASS_8",
            "fileList": [
                {
                    "file": "/hzlc_20211025162042.jpg",
                    "type": "user"
                }
            ],
            "statusCode": "ACCT_8",
            "clientBankAccountName": "521423"
        }
        auditWithdrawalAcctPassResp = s.post(url=auditWithdrawalAcctPassurl, headers=headers, json=data)
        logging.info(
            "步骤8接口'{}';请求参数为:{};响应结果为：'{}'".format(auditWithdrawalAcctPassurl, data, auditWithdrawalAcctPassResp.text))
        print(
            "步骤8接口'{}';请求参数为:{};响应结果为：'{}'".format(auditWithdrawalAcctPassurl, data, auditWithdrawalAcctPassResp.text))
        return auditWithdrawalAcctPassResp


if __name__ == "__main__":
    a = 1
    CreatEquitiesWithdrawal = CreatEquitiesWithdrawal出金()
    for i in range(a):
        # 实例化CreatUser
        print("=====================================步骤1：", CreatEquitiesWithdrawal.createWithdrawal创建出金单().text)
        time.sleep(10)
        print("=====================================步骤2：", CreatEquitiesWithdrawal.operatingWorkFlowNo().text)
        time.sleep(10)
        print("=====================================步骤3：", CreatEquitiesWithdrawal.auditWithdrawalNo().text)
        time.sleep(10)
        print("=====================================步骤4：", CreatEquitiesWithdrawal.operatingWorkFlowTO().text)
        time.sleep(10)
        print("=====================================步骤5：", CreatEquitiesWithdrawal.auditWithdrawalTo().text)
        time.sleep(10)
        print("=====================================步骤6：", CreatEquitiesWithdrawal.get_current_state().text)
        time.sleep(10)
        print("=====================================步骤7：", CreatEquitiesWithdrawal.operatingWorkFlowfourth().text)
        time.sleep(10)
        print("=====================================步骤8：", CreatEquitiesWithdrawal.auditWithdrawalAcctPass().text)
        time.sleep(10)
