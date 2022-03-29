# -*- coding:utf-8 -*-
import requests
from Common.random_number import *
from Config.cdms_config import *
from Business.login import cdms_获取token
from Business.H5.mobile_login import h5_caccessToken
import logging

from Common.data_文本读写 import *
from Common.com_sql.eddid_data_select import cd_enty,cd_clnt_apply_info,cd_clnt_info_update_apply
from Common.data_文本读写 import *


class EmailInvestigateAccounts():

    def uploadfile(self):

        global token,headers,clientId,accountId,L,s,phone
        token = cdms_获取token()
        s = requests.Session()
        eddidhost = url
        uploadurl=eddidhost+"/api/emailInvestigateAccounts"
        cookfront=cookfr
        #注意headers不要加"Content-Type"参数，暂时不知道原因
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": cookfront + token,
        }
        file = {'file': ('88295.xlsx', open("F:\\python\\EDDID_CDMS\\Data\\88295.xlsx", "rb"), 'application/vnd.ms-excel')}
        time.sleep(2)
        uploadfilerep = s.post(url=uploadurl, files=file, headers=headers)
        logging.info("步骤1,文件上传接口：'{}';请求参数为:{};响应结果为：'{}'".format(uploadurl, file, uploadfilerep.text))
        print("步骤1,文件上传接口：'{}';请求参数为:{};响应结果为：'{}'".format(uploadurl, file, uploadfilerep.text))
        return uploadfilerep

class APPoperation():
    def VerifyEmail_response_P1(self):
        global clientId, tanceAmount,ac_id,H5requests
        #实例化requests
        H5requests = requests.Session()
        #登录获取H5页面token
        tokenh5 = h5_caccessToken(10236428098)
        sumbiturl="https://route-service-qa.eddid.com.cn:1443/open/account/popout/sumbit/verifyEmail";
        headers = {
            "accept": "application/json, text/plain, */*",
            "authorization": "Bearer " + tokenh5,
            "content-type": "application/json;charset=utf-8",
            "accept-encoding": "gzip, deflate, br",
        }
        data = {
            "deviceId": "23fef48fb542a375a90f2f97a43b4fed3",
          # "deviceId": "7ae22fab33e4de39566b90aecb98c8a3"
            "email": "ganjiexiang7@126.com",
            "submitSource": "CP_H5",
            "type": "P1",
        }
        print("data=", data)
        verifyEmailrep = H5requests.post(url=sumbiturl, headers=headers, json=data)
        logging.info("步骤1，确认邮箱提交接口'{}';请求参数为:{};的响应结果为:'{}'".format(sumbiturl, data, verifyEmailrep.text))
        print("步骤1，确认邮箱提交接口'{}';请求参数为:{};响应结果为:'{}'".format(sumbiturl, data, verifyEmailrep.text))
        return verifyEmailrep


if __name__ == '__main__':

    emailIn=EmailInvestigateAccounts()
    verifyEmail=APPoperation()
    print("=====================================步骤1：", emailIn.uploadfile().text)
    time.sleep(10)
    print("=====================================步骤1：", verifyEmail.VerifyEmail_response_P1().text)
