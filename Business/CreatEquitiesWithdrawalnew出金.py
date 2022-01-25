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
        global clientId, withdrawalAmount, eddidhost,token,s,headersw
        eddidhost = url
        token = cdms_获取token()
        s = requests.Session()
        # clientId=88659
        # accountId = 886591280
        clientId=11431
        accountId =114313210
        Category = accountCategory(accountId)[0]
        print("================================获取到clientId为：{}，accountId为：{}".format(clientId, accountId))
        withdrawalAmount = Randoms().randomAmount()
        headersw = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headersw)
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
        createWithdrawalResp = s.post(url=createWithdrawalurl, headers=headersw, json=data)
        logging.info("步骤1，出金申请单提交接口'{}';请求参数为:{};响应结果为：'{}'".format(createWithdrawalurl, data, createWithdrawalResp.text))
        print("步骤1，出金申请单提交接口接口'{}';请求参数为:{};响应结果为：'{}'".format(createWithdrawalurl, data, createWithdrawalResp.text))
        return createWithdrawalResp

    def get_current_state(self):
        global applyId
        applyId = cd_withdrawal(clientId, withdrawalAmount)[0][0]
        cstate = gs_apply_work_flow(applyId)[0][3]
        print("数据库查询到当前流程状态cstate的值为{}".format(cstate))
        b = 20
        while cstate == "SYS_HANDLEING_8":
            time.sleep(20)
            print("当前状态为：系统处理中，流程等待！当前时间为：{},剩余等待{}次！".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), b))
            logging.info(
                "当前状态为：系统处理中，流程等待！当前时间为：{},剩余等待{}次！".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), b))
            cstate = gs_apply_work_flow(applyId)[0][3]
            print("数据库查询到当前流程状态cstate的值为{}".format(cstate))
            logging.info("数据库查询到当前流程状态cstate的值为{}".format(cstate))
            b -= 1
            if b < 0:
                print("系统处理时间过长，不再等待，进程结束！")
                break
        # 系统处理出金返回结果后，首先提交锁
        time.sleep(10)
        # 如果返回的是系统处理失败，就审批通过
        if cstate == 'SYS_ERROR_8':
            logging.info("当前token为:{}".format(token))
            print("当前token为:{}".format(token))
            print("headers", headersw)
            time.sleep(15)

            dataone = {
                "applyId": applyId,
                "workFlowCode": "withdrawalApply",
                "controlCode": "LOCK"
            }
            operatingWorkFlowsurl = eddidhost + "/api/common/operatingWorkFlow"
            s.post(url=operatingWorkFlowsurl, headers=headersw, json=dataone)
            print("返回失败后，提交提交锁完成++++++++++++++++++++++++++++")
            time.sleep(15)
            auditWithdrawalERRORPassurl = eddidhost + "/api/funds/auditWithdrawal"
            print("auditWithdrawalERRORPassurl:", auditWithdrawalERRORPassurl)
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


            s.post(url=auditWithdrawalERRORPassurl, headers=headersw, json=data)
            print("系统处理失败后，审批通过++++++++++++++++++++++++++++")

            time.sleep(10)
            operatingWorkFlowstwo=s.post(url=operatingWorkFlowsurl, headers=headersw, json=dataone)
            print("审批通过后，再次提交锁++++++++++++++++++++++++++++")
            print("再次锁定接口'{}';请求参数为:{};响应结果为：'{}'".format(operatingWorkFlowsurl, data, operatingWorkFlowstwo.text))
        else:
            dataone = {
                "applyId": applyId,
                "workFlowCode": "withdrawalApply",
                "controlCode": "LOCK"
            }
            operatingWorkFlowsurl = eddidhost + "/api/common/operatingWorkFlow"
            time.sleep(10)
            operatingWorkFlowstwo = s.post(url=operatingWorkFlowsurl, headers=headersw, json=dataone)
            print("系统处理成功，直接提交锁++++++++++++++++++++++++++++")

        logging.info(
            "步骤2，接口'{}';请求参数为:{};响应结果为：'{}'".format(operatingWorkFlowsurl, dataone, operatingWorkFlowstwo.text))
        print("步骤2接口'{}';请求参数为:{};响应结果为：'{}'".format(operatingWorkFlowsurl, dataone, operatingWorkFlowstwo.text))
        return operatingWorkFlowstwo

    def auditWithdrawalAcctPass(self):
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
        auditWithdrawalAcctPassResp = s.post(url=auditWithdrawalAcctPassurl, headers=headersw, json=data)
        logging.info(
            "步骤3，Acct审批通过接口'{}';请求参数为:{};响应结果为：'{}'".format(auditWithdrawalAcctPassurl, data, auditWithdrawalAcctPassResp.text))
        print(
            "步骤3，Acct审批通过接口'{}';请求参数为:{};响应结果为：'{}'".format(auditWithdrawalAcctPassurl, data, auditWithdrawalAcctPassResp.text))
        return auditWithdrawalAcctPassResp

    def get_current_state_final(self):
        statefinal=gs_apply_work_flow(applyId)
        print("步骤4执行完成，通过applyId='{}'查询gs_apply_work_flow表的结果为{}".format(applyId, gs_apply_work_flow))
        logging.info("步骤4执行完成，通过applyId='{}'查询gs_apply_work_flow表的结果为{}".format(applyId, gs_apply_work_flow))
        return statefinal


if __name__ == "__main__":
    a = 1
    CreatEquitiesWithdrawal = CreatEquitiesWithdrawal出金()
    for i in range(a):
        # 实例化CreatUser
        print("=====================================步骤1：", CreatEquitiesWithdrawal.createWithdrawal创建出金单().text)
        time.sleep(10)
        print("=====================================步骤2：", CreatEquitiesWithdrawal.get_current_state().text)
        time.sleep(10)
        print("=====================================步骤3：", CreatEquitiesWithdrawal.auditWithdrawalAcctPass().text)
        time.sleep(10)
