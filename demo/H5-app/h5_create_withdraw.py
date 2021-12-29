import json

from requests_toolbelt.multipart.encoder import MultipartEncoder#formdata

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from comm.get_msg_cde import get_msg

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from conf.config import *
import unittest
# phoneCode="86"
# phoneNo="19725494746"
# clientId="500286"

# phoneCode="852"
# phoneNo="44654513"
# clientId="11902"

# phoneCode="86"
# phoneNo="14040124971"
# clientId="500356"

# phoneCode="86"
# phoneNo="14040124973"
# clientId="500363"
# phoneCode="86"
# phoneNo="13400002071"
# clientId="500363"
phoneCode='852'
phoneNo='90005709'
app_base_url=app_base_url_sit
class EddidH5(unittest.TestCase):#
    @classmethod
    def setUpClass(cls):
        pass
    def test_1_get_smg(self):
        url=app_base_url_sit+'/open/auth/v2/sms-code?phone={}&device_id=0d56e889be1a3da9516fa297e20841b5&send_type=login'.format(phoneCode+phoneNo)
        header = {"Content-Type": "application/json","authorization":"Basic dGVzdGFwcDI6YWJjZA=="}
        print("获取验证码接口请求",url)
        res=requests.get(url=url,headers=header,verify=False)
        print("获取验证码接口返回",res.text)

    # @unittest.skip("fail")
    #登录获取token
    def test_2_get_token(self):
        url=app_base_url+'/open/auth/v2/token'
        msg = get_msg(phoneNo)
        print("短信验证码：",msg)
        data=MultipartEncoder({
                "scope":"basic",
                "grant_type":"password",
                "login_type":"phone",
                "username":phoneCode+phoneNo,
                "pwd_type":"sms_code",
                "password":msg,
                "device_id":"0d56e889be1a3da9516fa297e20841b5"})
        header={ "Content-Type": data.content_type,"authorization":"Basic dGVzdGFwcDI6YWJjZA=="}
        # data['username']=phoneCode+phoneNo
        res = requests.post(url=url, data=data, headers=header)
        print("登录请求参数",data)
        print(res.json())
        global token
        token=res.json()['data']['access_token']

    @unittest.skip("fail")
    #h5新增出金申请
    def test_3_h5_create_withdraw(self):#本地出金

        url=app_base_url+'/open/account/fund/withdrawal/application/new'
        header = {"Content-Type": "application/json", "authorization":"Bearer "+token}
        data={
            "bankAccount":"55222333",
            "bankCode":"003",
            "bankType":"OTHER",
            "enName":"TETS NAME",
            "submitSource":"CP_H5",
            "tradeAccountNumber":"114311110",
            "tradeAccountType":"SECURITIES_CASH",
            "withdrawalAmount":"225",
            "withdrawalCurrency":"HKD",
            "withdrawalImages":[
                "49150d92-20d4-43c9-a6d9-ff48d264ea05.jpg"
            ],
            "serviceCharge":0,
            "actualAmount":"225",
            "withdrawalType":"LOCAL"
        }

        # data['clientId']=clientId
        # data['tradeAccountNumber']=clientId+'1110'

        data['tradeAccountNumber']=clientId+'1110'

        print("h5创建出金申请请求地址：{}".format(url))
        print("h5创建出金申请请求参数：{}".format(data))
        res = requests.post(url=url, json=data, headers=header)
        print(res.text)

    @unittest.skip("fail")
    def test_4_h5_create_withdraw(self):#海外出金

        url=app_base_url+'/open/account/fund/withdrawal/application/new'
        header = {"Content-Type": "application/json", "authorization":"Bearer "+token}
        data={
                "bankAccount":"5454545",
                "bankCode":"SIB",
                "bankSwiftCode":"VEILPRSJ",
                "bankName":"标准国际银行(SIB)",
                "bankType":"OTHER",
                "enName":"",
                "submitSource":"CP_H5",
                "sibMobile":"1234567890",
                "tradeAccountNumber":"1008611110",
                "tradeAccountType":"SECURITIES_MARGIN",
                "withdrawalAmount":"9995545",
                "withdrawalCurrency":"USD",
                "withdrawalImages":[
                    "4cb51230-3d22-431c-b88e-9a8ee10d1cb0.jpg"
                ],
                "withdrawalType":"SIB",
                "serviceCharge":45,
                "actualAmount":9995500
            }
        # data['clientId']=clientId
        # data['tradeAccountNumber']=clientId+'1110'

        data['tradeAccountNumber']=5001611110#clientId+'1210'

        print("h5创建海外出金申请请求地址：{}".format(url))
        print("h5创建海外申请请求参数：{}".format(data))
        res = requests.post(url=url, json=data, headers=header)
        print(res.text)

    @unittest.skip("fail")
    def test_5_edda_deposit(self):#EDDA入金申请
        url='https://route-service-qa.eddid.com.cn:1443/open/account/fund/deposit/application'
        header = {"Content-Type": "application/json", "authorization":"Bearer "+token}
        #成功
        data1={
                "beneficiaryAccount":"783266717",
                "depositType":"EDDA",
                "remittanceAmount":"1000001",
                "remittanceBankAccount":"12345888",
                "remittanceBankType":"SETTLEMENT_ACCOUNT",
                "remittanceCurrency":"HKD",
                "remittanceBankCode":"024",
                "remittanceBankName":"恒生银行有限公司 024",
                "submitSource":"CP_H5",
                "tradeAccountNumber":"3434343434",
                "tradeAccountType":"SECURITIES_CASH"
            }
        #成功待审核
        data2={
                "beneficiaryAccount":"783266717",
                "depositType":"EDDA",
                "remittanceAmount":"1000001",
                "remittanceBankAccount":"8888888",
                "remittanceBankType":"SETTLEMENT_ACCOUNT",
                "remittanceCurrency":"HKD",
                "remittanceBankCode":"041",
                "remittanceBankName":"创兴银行有限公司 041",
                "submitSource":"CP_H5",
                "tradeAccountNumber":"119021110",
                "tradeAccountType":"SECURITIES_CASH"
            }

        #成功已审核
        data3={
                "beneficiaryAccount":"783266717",
                "depositType":"EDDA",
                "remittanceAmount":"1000000",
                "remittanceBankAccount":"147258369",
                "remittanceBankType":"SETTLEMENT_ACCOUNT",
                "remittanceCurrency":"HKD",
                "remittanceBankCode":"018",
                "remittanceBankName":"中信银行国际有限公司 018",
                "submitSource":"CP_H5",
                "tradeAccountNumber":"119021110",
                "tradeAccountType":"SECURITIES_CASH"
            }
        res = requests.post(url=url, json=data1, headers=header)
        print(res)

    @unittest.skip("fail")
    def test_6_edda_bund(self):
        url="https://route-service-qa.eddid.com.cn:1443/open/account/fund/eDDA/application"
        # header = {"Content-Type": "application/json", "authorization":"Bearer "+token}
        header = {"Content-Type": "application/json", "authorization":"Bearer "+token}

        #
        data1={
            "tradeAccountNumber":"3434343434",
            "bankHolder":"test s",
            "idType":"CHINA_IDENTITY_CARD",
            "bankCode":"392",
            "obverseImgs":[

            ],
            "images":[

            ],
            "tradeAccountType":"SECURITIES_CASH",
            "idNumber":"150101198111161247",
            "terms":"https://middleware-agreement-qa-public.oss-cn-shenzhen.aliyuncs.com/2021-05/a985f2f1-cf05-46f0-828e-5d3a9bbcf9ac",
            "bankType":"SETTLEMENT_ACCOUNT",
            "bankNumber":"123458988",
            "bankName":"平安壹账通银行(香港)有限公司 392",
            "submitSource":"CP_H5",
            "agreement":"AGREE"
        }
        data2={
            "tradeAccountNumber":"119021110",
            "bankHolder":"LI tian",
            "idType":"CHINA_IDENTITY_CARD",
            "bankCode":"024",
            "obverseImgs":[

            ],
            "images":[

            ],
            "tradeAccountType":"SECURITIES_CASH",
            "idNumber":"150101198111161247",
            "terms":"https://middleware-agreement-qa-public.oss-cn-shenzhen.aliyuncs.com/2021-05/a985f2f1-cf05-46f0-828e-5d3a9bbcf9ac",
            "bankType":"SETTLEMENT_ACCOUNT",
            "bankNumber":"1234588899",
            "bankName":"恒生银行有限公司 024",
            "submitSource":"CP_H5",
            "agreement":"AGREE"
        }
        res = requests.post(url=url, json=data2, headers=header)
        print(res)
    #
    # @unittest.skip("fail")
    def test_7_get_update(self):
        url="https://route-service-qa.eddid.com.cn:1443/open/account/eddid/queryAccountInfoNeedUpdated"
        header = {"Content-Type": "application/json", "authorization":"Bearer "+token}

        res = requests.get(url=url, headers=header)
        # print("返回",res.text)
        res_dicts=json.dumps(res.json(),indent=4)
        print(res_dicts)
        # print(res.json())

    @unittest.skip("fail")
    def test_8_update(self):
        url="https://route-service-qa.eddid.com.cn:1443//open/account/eddid/submitAccountInfoNeedUpdated"
        header = {"Content-Type": "application/json", "accept-language":"zh-HK","Authorization":"Bearer "+token}
        # data={
        #     "acquaintHighLevelInstructionsProve": [],
        #     "address": "测试修改",
        #     "business": "",
        #     "cdmsId": "521",
        #     "companyAddress": "",
        #     "companyName": "公司全称测试",
        #     "employmentStatus": "",
        #     "isRegisteredPerson": "",
        #     "job": "",
        #     "listedCompany": "",
        #     "otherBusiness": "",
        #     "passportMaterial": [],
        #     "registeredPersonRemark": ""
        # }
        data={
          "cdmsId": "521",
          "employmentStatus": "employmentStatus",
          "listedCompany": "Y",
          "business": "financial",
          "otherBusiness": "otherBusiness",
          "job": "一般员工",
          "companyName": "艾德",
          "companyAddress": "地址",
          "isRegisteredPerson": "Y",
          "registeredPersonRemark": "xxxx",
          "acquaintHighLevelInstructionsProve": ["111.jpg","112.jpg"],
          "address": "地址",
          "passportMaterial": ["33.jpg","44.jpg"]
        }
        res = requests.post(url=url, json=data, headers=header)

        res_dicts=json.dumps(res.json(),indent=4)
        print(res_dicts)

if __name__=="__main__":
    unittest.main()
    # E=EddidH5()
    # # E.test_1_get_smg()
    # E.test_3_h5_create_withdraw()