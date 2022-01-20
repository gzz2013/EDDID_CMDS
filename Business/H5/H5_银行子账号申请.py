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


class Creat_account_sub():

    # 步骤1,H5页面提交子账号申请
    def H5sub_account(self):
        tokenh5=h5_caccessToken()
        H5requests = requests.Session()
        advanceAmount=Randoms().randomintNumber()
        headers = {
            "accept": "application/json, text/plain, */*",
            "authorization": "Bearer "+ tokenh5,
            "content-type": "application/json;charset=utf-8",
            "accept-encoding": "gzip, deflate, br",
            "content-length": "149"
        }
        print("当前token为:{}".format(tokenh5))
        print("headers", headers)
        # closeAccturl = eddidhost + "/api/acct/closeAcct"
        H5subaccounturl = app_base_url + "/open/account/fund/sub-account/application/new"
        print("H5subaccounturl：", H5subaccounturl)
        data = {
            "advanceAmount":advanceAmount,
            "currency":"HKD",
            "submitSource":"CP_H5",
            "channel":"ICBC",
            "productCategory":"STOCK"
        }
        print("data=", data)
        H5subaccountResp = H5requests.post(url=H5subaccounturl, headers=headers, json=data)
        logging.info("步骤1，子账号申请提交接口'{}';请求参数为:{};的响应结果为:'{}'".format(H5subaccounturl, data, H5subaccountResp.text))
        print("步骤1，子账号申请提交接口'{}';请求参数为:{};响应结果为:'{}'".format(H5subaccounturl, data, H5subaccountResp.text))
        return H5subaccountResp

    #第一次提交锁
    def operatingWorkFlowone提交锁(self):
        global token_web, eddidhost, wbes, cookfront, clnt_id, applyId, headers
        clnt_id = datahandle(data_read('F:\\python\\EDDID_CDMS\\Data\\unableAcct.txt'))

        eddidhost = url
        cookfront = cookfr
        applyId = cd_clnt_bank_sub_acct_apply(int(clnt_id[1]))[0][0]
        token_web = cdms_获取token()
        wbes = requests.Session()

        print("根据客户编号clnt_id={}，查询到applyId={}".format(clnt_id[1], applyId))
        logging.info("根据客户编号clnt_id={}，查询到applyId={}".format(clnt_id[1], applyId))

        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": cookfront + token_web
        }
        logging.info("当前token为:{}".format(token_web))
        print("当前token为:{}".format(token_web))
        print("headers", headers)
        operatingWorkFlowoneurl = eddidhost + "/api/common/operatingWorkFlow"
        print("operatingWorkFlowoneurl:", operatingWorkFlowoneurl)

        data = {
            "applyId": applyId,
            "workFlowCode": "bankSubAccount",
            "controlCode": "LOCK"
        }
        print("data=", data)
        operatingWorkFlowoneResp = wbes.post(url=operatingWorkFlowoneurl, headers=headers, json=data)
        logging.info("步骤2，第一次提交锁接口'{}';请求参数为:{};响应结果为:'{}'".format(operatingWorkFlowoneurl, data,
                                                                operatingWorkFlowoneResp.text))
        print("步骤2，第一次提交锁接口'{}';请求参数为:{};响应结果为:'{}'".format(operatingWorkFlowoneurl, data,
                                                         operatingWorkFlowoneResp.text))
        return operatingWorkFlowoneResp

    #CS2审批通过
    def approvalBankSubAccountCS2审核(self):

        approvalBankSubAccountCS2url = eddidhost + "/api/clientBankSubAccount/approvalBankSubAccount"
        print("approvalBankSubAccountCS2url:", approvalBankSubAccountCS2url)
        data = {
            "applyId":applyId,
            "approvalResult":"PASS",
            "bankCode":"ICBC",
            "subAccountNo":"072"+ clnt_id[1]+"951",
            "subAccountName":"ESFL-Owen StockU",
            "subAcctImgList":[

            ]
        }
        print("data=", data)
        approvalBankSubAccountCS2Resp = wbes.post(url=approvalBankSubAccountCS2url, headers=headers, json=data)
        logging.info("步骤3，CS2提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(approvalBankSubAccountCS2url, data,
                                                                approvalBankSubAccountCS2Resp.text))
        print("步骤3，CS2提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(approvalBankSubAccountCS2url, data,
                                                     approvalBankSubAccountCS2Resp.text))
        return approvalBankSubAccountCS2Resp

    #第二次提交锁
    def operatingWorkFlowtwo提交锁(self):

        operatingWorkFlowtwourl = eddidhost + "/api/common/operatingWorkFlow"
        print("operatingWorkFlowtwourl:", operatingWorkFlowtwourl)
        data = {
            "applyId": applyId,
            "workFlowCode": "bankSubAccount",
            "controlCode": "LOCK"
        }
        print("data=", data)
        operatingWorkFlowtwoResp = wbes.post(url=operatingWorkFlowtwourl, headers=headers, json=data)
        logging.info("步骤4，第二次提交锁接口'{}';请求参数为:{};响应结果为:'{}'".format(operatingWorkFlowtwourl, data,
                                                                operatingWorkFlowtwoResp.text))
        print("步骤4，第二次提交锁接口'{}';请求参数为:{};响应结果为:'{}'".format(operatingWorkFlowtwourl, data,
                                                     operatingWorkFlowtwoResp.text))
        return operatingWorkFlowtwoResp

    #最终审批通过
    def approvalBankSubAccountfinal审批(self):

        approvalBankSubAccountfinalurl = eddidhost + "/api/clientBankSubAccount/approvalBankSubAccount"
        print("approvalBankSubAccountfinalurl:", approvalBankSubAccountfinalurl)
        data = {
            "applyId": applyId,
            "approvalResult": "PASS"
        }
        print("data=", data)
        approvalBankSubAccountfinalResp = wbes.post(url=approvalBankSubAccountfinalurl, headers=headers, json=data)
        logging.info("步骤5，最后一次审批接口'{}';请求参数为:{};响应结果为:'{}'".format(approvalBankSubAccountfinalurl, data,
                                                                approvalBankSubAccountfinalResp.text))
        print("步骤5，最后一次审批接口'{}';请求参数为:{};响应结果为:'{}'".format(approvalBankSubAccountfinalurl, data,
                                                     approvalBankSubAccountfinalResp.text))
        return approvalBankSubAccountfinalResp

    #查询数据库
    def check_cd_clnt_bank_sub_acct(self):
        bank_sub_acct=cd_clnt_bank_sub_acct(clnt_id[1])
        print("步骤6执行完成，通过clnt='{}'查询cd_clnt_bank_sub_acct表的结果为{}".format(clnt_id, bank_sub_acct))
        logging.info("步骤6执行完成，通过clnt='{}'查询cd_clnt_bank_sub_acct表的结果为{}".format(clnt_id, bank_sub_acct))
        return bank_sub_acct

if __name__ == "__main__":
    c=Creat_account_sub()
    print("步骤1，H5页面提交子账号申请", c.H5sub_account().text)
    time.sleep(4)
    print("步骤2，web第一次提交锁", c.operatingWorkFlowone提交锁().text)
    time.sleep(4)
    print("步骤3，CS2审批", c.approvalBankSubAccountCS2审核().text)
    time.sleep(4)
    print("步骤4，第二次提交锁", c.operatingWorkFlowtwo提交锁().text)
    time.sleep(4)
    print("步骤5，最终审批", c.approvalBankSubAccountfinal审批().text)
    time.sleep(4)
    print("步骤6，sql查询结果", c.check_cd_clnt_bank_sub_acct())
    time.sleep(4)