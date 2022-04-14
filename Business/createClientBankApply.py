import requests
from Business.login import cdms_获取token
import logging
import time
from Common.com_sql.eddid_data_select import *
from Config.cdms_config import *
from Common.data_文本读写 import *
from Common.random_number import Randoms


#依赖于停用账号关闭账号用例的用到账号
class CreateClientBank():

    #步骤1 提交银行申请资料
    def createClientBankApply(self):
        global clnt_id,cookfront, token, eddidhost, s, phone
        bankCode=Randoms().choice_bankCode()
        s = requests.session()
        token = cdms_获取token()
        cookfront = cookfr
        eddidhost = url
        ac_id_l = datahandle(data_read('F:\\python\\EDDID_CDMS\\Data\\unableAcct.txt'))
        clnt_id = ac_id_l[1]
        phone = ac_id_l[2]
        rfirstName = ac_id_l[3]
        rlastName = ac_id_l[4]
        print("clnt_id888887777777:", clnt_id)
        # eddid_id = cd_clnt(clnt_id)[0][3]
        # print("eddid_id:", eddid_id)

        bankCardinformation=[]
        bankCardinformation.append(clnt_id)
        bankCardinformation.append(phone)
        bankCardinformation.append(bankCode)
        bankCardinformation.append(rlastName + rfirstName)
        #把对应数据写入文本
        data_write('F:\\python\\EDDID_CDMS\\Data\\bankCardinformation.txt', bankCardinformation)
        print("记录数据的文件名为：bankCardinformation.txt，写入数据为:{}".format(bankCardinformation))

        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": cookfront + token
        }
        # logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        createClientBankApplyurl = eddidhost + "/api/clientBankApply/createClientBankApply"
        logging.info("获取到的客户id为：{}".format(clnt_id))
        print("获取到的客户id为：{}".format(clnt_id))
        # global applyId
        data = {
            "bankCode":bankCode,
            "bankAccountNumber":phone,
            "bankAccountName":rlastName + rfirstName,
            "currencyList":[
                "USD",
                "HKD",
                "CNY"
            ],
            "bankCertificatesList":[
                "/hzlc_20211216153155.jpg"
            ],
            "clientId":clnt_id
        }
        print("data=", data)
        createClientBankApplyResp = s.post(url=createClientBankApplyurl, headers=headers, json=data)
        logging.info("资料提交，步骤01提交审核接口'{}';请求参数为:{};的响应结果为:'{}'".format(createClientBankApplyurl, data,
                                                                  createClientBankApplyResp.text))
        print("资料提交，步骤01提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(createClientBankApplyurl, data,
                                                          createClientBankApplyResp.text))
        return createClientBankApplyResp

    def approvalClientBankApply(self):
        global applyId
        applyId = cd_clnt_bank_ac_apply(clnt_id)[0][0]
        print("当前applyId为：{}".format(applyId))
        logging.info("当前applyId为：{}".format(applyId))
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": cookfront + token
        }
        # logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        approvalClientBankApplyurl = eddidhost + "/api/clientBankApply/approvalClientBankApply"

        data = {
            "applyId":applyId,
            "approvalResult":"PASS",
            "assignUser":"ED_RO"
        }
        print("data=", data)
        approvalClientBankApplyResp = s.post(url=approvalClientBankApplyurl, headers=headers, json=data)
        logging.info("CS2审批，步骤02提交审核接口'{}';请求参数为:{};的响应结果为:'{}'".format(approvalClientBankApplyurl, data,
                                                              approvalClientBankApplyResp.text))
        print("CS2审批，步骤02提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(approvalClientBankApplyurl, data,
                                                          approvalClientBankApplyResp.text))
        return approvalClientBankApplyResp


    def approvalClientBankApplytwo(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": cookfront + token
        }
        # logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        approvalClientBankApplytwourl = eddidhost + "/api/clientBankApply/approvalClientBankApply"

        data = {
            "applyId":applyId,
            "approvalResult":"PASS",
        }
        print("data=", data)
        approvalClientBankApplytwoResp = s.post(url=approvalClientBankApplytwourl, headers=headers, json=data)
        logging.info("OR审批，步骤03提交审核接口'{}';请求参数为:{};的响应结果为:'{}'".format(approvalClientBankApplytwourl, data,
                                                              approvalClientBankApplytwoResp.text))
        print("OR审批，步骤03提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(approvalClientBankApplytwourl, data,
                                                          approvalClientBankApplytwoResp.text))
        return approvalClientBankApplytwoResp

    def sql_check_BankCard(self):
        time.sleep(10)
        # 通过直接调用cd_enty表查询
        sql_check_BankCard = cd_clnt_bank_ac(clnt_id)
        print("查询数据库，步骤04通过clnt_id='{}'查询cd_clnt_bank_ac表的结果为{}".format(clnt_id, sql_check_BankCard))
        logging.info("查询数据库，步骤04通过clnt_id='{}'查询cd_clnt_bank_ac表的结果为{}".format(clnt_id, sql_check_BankCard))
        return sql_check_BankCard


if __name__ == "__main__":
    a = 1
    CreateClientBank = CreateClientBank()
    for i in range(a):
        # 实例化CreateClientBank
        print("=====================================步骤1：", CreateClientBank.createClientBankApply().text)
        time.sleep(4)
        # print("=====================================步骤2：", CreateClientBank.approvalClientBankApply().text)
        time.sleep(4)
        # print("=====================================步骤3：", CreateClientBank.approvalClientBankApplytwo().text)
        time.sleep(4)
        # print("=====================================步骤4：", CreateClientBank.sql_check_BankCard())
        time.sleep(4)

