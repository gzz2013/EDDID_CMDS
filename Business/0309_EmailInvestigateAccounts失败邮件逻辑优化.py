# -*- coding:utf-8 -*-
import requests
from Common.random_number import *
from Config.cdms_config import *
from Business.login import cdms_获取token
import logging
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


if __name__ == '__main__':

    emailIn=EmailInvestigateAccounts()
    print("=====================================步骤1：", emailIn.uploadfile().text)
