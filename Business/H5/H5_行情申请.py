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


class Creat_mrktdat_sub():

    # 步骤1,H5页面提交行情管理
    def H5submit_mrktdat(self):
        tokenh5=h5_caccessToken()
        H5requests = requests.Session()
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
        H5submitmrktdaturl = app_base_url + "/open/account/trade/quote-service/application"
        print("H5submitmrktdaturl为：", H5submitmrktdaturl)
        data = {
            "informationStatement":"false",
            "applyContentType":[
                "HK_STOCK"
            ],
            "code":"36541241127390519",
            "agreement":"true",
            "submitSource":"CP_H5",
            "subscribeNumber":1
        }
        print("data=", data)
        H5submit_mrktdatResp = H5requests.post(url=H5submitmrktdaturl, headers=headers, json=data)
        logging.info("步骤1提交接口'{}';请求参数为:{};的响应结果为:'{}'".format(H5submitmrktdaturl, data, H5submit_mrktdatResp.text))
        print("步骤1提交接口'{}';请求参数为:{};响应结果为:'{}'".format(H5submitmrktdaturl, data, H5submit_mrktdatResp.text))
        return H5submit_mrktdatResp


    def operatingWorkFlow提交锁(self):

        global token_web, eddidhost,wbes, cookfront,clnt_id,applyId,headers
        clnt_id=datahandle(data_read('F:\\python\\EDDID_CDMS\\Data\\unableAcct.txt'))

        eddidhost=url
        cookfront = cookfr
        applyId=gs_mrktdat_sub(int(clnt_id[1]))[0][0]
        token_web = cdms_获取token()
        wbes = requests.Session()

        print("根据客户编号clnt_id={}，查询到applyId={}".format(clnt_id[1],applyId))
        logging.info("根据客户编号clnt_id={}，查询到applyId={}".format(clnt_id[1],applyId))

        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": cookfront + token_web
        }
        logging.info("当前token为:{}".format(token_web))
        print("当前token为:{}".format(token_web))
        print("headers", headers)
        operatingWorkFlowturl = eddidhost + "/api/common/operatingWorkFlow"
        print("operatingWorkFlowturl为:", operatingWorkFlowturl)

        data = {
            "applyId": applyId,
            "workFlowCode": "realTimeQuoteSubscriptionApply",
            "controlCode": "LOCK"
        }
        print("data=", data)
        operatingWorkFlowFirstResp = wbes.post(url=operatingWorkFlowturl, headers=headers, json=data)
        logging.info("步骤2提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(operatingWorkFlowturl, data,
                                                                operatingWorkFlowFirstResp.text))
        print("步骤2提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(operatingWorkFlowturl, data,
                                                         operatingWorkFlowFirstResp.text))
        return operatingWorkFlowFirstResp

    def auditRtqSubscptn审批(self):

        auditRtqSubscptnurl = eddidhost + "/api/acct/auditRtqSubscptn"
        print("operatingWorkFlowturl为:", auditRtqSubscptnurl)

        data = {
            "acId":clnt_id[0],
            "applyId":applyId,
            "workFlowCode":"realTimeQuoteSubscriptionApply",
            "controlCode":"PASS"
        }
        print("data=", data)
        auditRtqSubscptnResp = wbes.post(url=auditRtqSubscptnurl, headers=headers, json=data)
        logging.info("步骤3提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(auditRtqSubscptnurl, data,
                                                                auditRtqSubscptnResp.text))
        print("步骤3提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(auditRtqSubscptnurl, data,
                                                     auditRtqSubscptnResp.text))
        return auditRtqSubscptnResp

    #查询数据库
    def check_gs_mrktdat_sub(self):
        time.sleep(4)
        mrktdat_sub=gs_mrktdat_sub(clnt_id[1])
        print("步骤4执行完成，通过clnt='{}'查询gs_mrktdat_sub表的结果为{}".format(clnt_id, mrktdat_sub))
        logging.info("步骤4执行完成，通过clnt='{}'查询gs_mrktdat_sub表的结果为{}".format(clnt_id, mrktdat_sub))
        return mrktdat_sub


if __name__ == "__main__":
    c=Creat_mrktdat_sub()
    print("步骤1，H5行情申请提交", c.H5submit_mrktdat().text)
    time.sleep(4)
    print("步骤2，web提交锁", c.operatingWorkFlow提交锁().text)
    time.sleep(4)
    print("步骤3，web提审核", c.auditRtqSubscptn审批().text)
    time.sleep(4)