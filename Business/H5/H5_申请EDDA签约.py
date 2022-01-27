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


class Creat_h5_eDDAcontract():
    def H5submit_eDDAcontract(self):
        global clientId, tanceAmount,ac_id,H5requests
        #实例化requests
        H5requests = requests.Session()
        #登录获取H5页面token
        tokenh5 = h5_caccessToken()
        #通过文本读取转账交易账号

        com=datahandle(data_read('F:\\python\\EDDID_CDMS\\Data\\unableAcct.txt'))
        clientId = com[0]
        BankHolder=com[4]+' '+com[3]
        ac_id = datahandle(data_read('F:\\python\\EDDID_CDMS\\Data\\unableAcct.txt'))[1]
        #获取账号类型
        tradeAccountType = accountCategory(ac_id)[1]
        #生成开户银行账号
        tanceBankAccount = str(clientId) + "3546"
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
        H5submiteDDAurl = app_base_url + "/open/account/fund/eDDA/application"
        print("H5submitmrktdaturl为：", H5submiteDDAurl)
        data = {
            "tradeAccountNumber":ac_id,
            "bankHolder":BankHolder,
            "idType":"HK_IDENTITY_CARD",
            "bankCode":"012",
            "obverseImgs":[

            ],
            "images":[

            ],
            "tradeAccountType":tradeAccountType,
            "idNumber":IdNumber,
            "terms":"https://middleware-agreement-qa-public.oss-cn-shenzhen.aliyuncs.com/2021-05/a985f2f1-cf05-46f0-828e-5d3a9bbcf9ac",
            "bankType":"OTHER",
            "bankNumber":tanceBankAccount,
            "bankName":"中国银行（香港）有限公司 012",
            "submitSource":"CP_H5",
            "agreement":"AGREE"
        }
        print("data=", data)
        H5submiteDDResp = H5requests.post(url=H5submiteDDAurl, headers=headers, json=data)
        logging.info("步骤1提交接口'{}';请求参数为:{};的响应结果为:'{}'".format(H5submiteDDAurl, data, H5submiteDDResp.text))
        print("步骤1提交接口'{}';请求参数为:{};响应结果为:'{}'".format(H5submiteDDAurl, data, H5submiteDDResp.text))
        return H5submiteDDResp


    #校验数据库状态
    def check_bank_ac_edda_apply(self):
        check_bank_ac_eddaapply=cd_clnt_bank_ac_edda_apply(int(clientId))

        print("数据库cd_clnt_bank_ac_edda_apply查询结果为{}".format(check_bank_ac_eddaapply))

        statcode=check_bank_ac_eddaapply[0][27]
        #如果statcode=BANK_HANDLING要等待，直到流程有状态返回
        b = 20
        while statcode=="BANK_HANDLING":
            time.sleep(20)
            print("当前状态为：待银行处理，流程等待！当前时间为：{},剩余等待{}次！".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), b))
            logging.info(
                "当前状态为：待银行处理，流程等待！当前时间为：{},剩余等待{}次！".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), b))
            #重新传入clientId进行查询
            statcode = cd_clnt_bank_ac_edda_apply(int(clientId))[0][27]
            print("数据库查询到当前流程状态statcode的值为{}".format(statcode))
            b-=1

            if b==0:
                print("系统处理时间过长，不再等待，进程结束！")
                break
        print("当前状态为：系统处理失败，流程继续！")

        if statcode == 'DONE':
            print("当前状态为成功，流程结束！")
            logging.info("当前状态为成功，流程结束！")

        else:
            time.sleep(15)
            webtoken=cdms_获取token()
            eddidhost= url
            eddas=requests.Session()
            applyid=check_bank_ac_eddaapply[0][0]
            headers = {
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Connection": "keep-alive",
                "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + webtoken
            }

            # 系统处理出金返回结果后，首先提交锁
            logging.info("当前token为:{}".format(webtoken))
            print("当前token为:{}".format(webtoken))
            print("headers", headers)
            newOperatingWorkFlowurl = eddidhost + "/api/common/newOperatingWorkFlow"
            print("applyClienturl:", newOperatingWorkFlowurl)
            data = {
                "applyId": applyid,
                "workFlowCode": "EDDA",
                "controlCode": "PASS"
            }
            time.sleep(15)
            aceddaapplyResp=eddas.post(url=newOperatingWorkFlowurl, headers=headers, json=data)
            logging.info("步骤2接口'{}';请求参数为:{};响应结果为：'{}'".format(newOperatingWorkFlowurl, data, aceddaapplyResp.text))
            print("步骤2接口'{}';请求参数为:{};响应结果为：'{}'".format(newOperatingWorkFlowurl, data, aceddaapplyResp.text))

        check_bank_ac_eddaapplynew=cd_clnt_bank_ac_edda_apply(int(clientId))
        logging.info("步骤2结束，查询到数据库cd_clnt_bank_ac_edda_apply,入参{}，结果为{}".format(clientId,check_bank_ac_eddaapplynew))
        print("步骤2结束，查询到数据库cd_clnt_bank_ac_edda_apply,入参{}，结果为{}".format(clientId,check_bank_ac_eddaapplynew))
        return check_bank_ac_eddaapply


if __name__ == "__main__":
    a = 1
    # 实例化Creat_h5_eDDAcontract()
    CreateDDAcontract = Creat_h5_eDDAcontract()
    for i in range(a):
        print("=====================================步骤1：", CreateDDAcontract.H5submit_eDDAcontract().text)
        time.sleep(30)
        print("=====================================步骤2：", CreateDDAcontract.check_bank_ac_edda_apply())
