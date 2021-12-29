import sys
import time
import os,sys
"""添加工程目录，否则jenkins会报错找不到XXX model"""
# sys.path.extend(['D:\\My\\Interface-修改', 'D:/My/Interface-修改'])#工程目录
basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))#获取工程目录
sys.path.extend([basedir])
import requests
import unittest

import requests
import unittest
from comm.check import *
from comm.get_msg_cde import get_msg
from comm.random_number import CreateRanDom, Randoms
from comm.check import *

C = Check()
from conf.config import *
from util.HTMLTestRunner import HTMLTestRunner

x_token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhb3NoNSIsImV4cCI6MTYxMTkyNTg1OSwic3ViIjoiNzAyZTg1MTQtMTlmZS00NjNjLWIwZDItZDlmY2M1MGI5NGNjIiwic2NvcGUiOiJiYXNpYyJ9.tPKBUnD8nhXd-_WGZ_XAhNODgV3-vVmvwNqJmCce3pm1P47Fg1tmUthGh_ouO01EtR_YuHe_sEZWUqiXjDRuPZQS7hwJTJM00W9Ly5c0U0F3dySj9HMLSo1moUhIS4c7-TAWzJzd5nTOMx6JY0-Yic8b6RtQZ5ACqVPEDb193z6DBCtRIutgs3cuYTfVcE6JI6EhvvS3YfVq5_jTS113bKV3d6X5FC3lci82pHHZ5VuyOewUv9mGtJUtGrxiUakuEHVUsx6u9CTh2AcAmNayxUqK-q0MwdWg41RyrY6EuS4DegTa_lkg3jPKppR4RsbutJhOV4mo6FbaPMOx9GNxgQ"
token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhb3NoNSIsImV4cCI6MTYxMjY5OTE1MCwic3ViIjoiNGVlYTgzMDctOTk4YS00MTMxLThjZjItOWZiYTQzM2JhOTU1Iiwic2NvcGUiOiJiYXNpYyJ9.sbeceK_1pEuuSvwsAJm9nTo_PNnFRdKiN7fHVPcQEWk8ZKuLuaMx_jHnugcSy4PFkSxVgfakXfS5GfymIvbG3hNCLPYAUnF6n6br90nC6axwR57uqKdW3uSzqUnOHMVxmwYeQfbUiAffi0aHXWnSQi2CPCqf6aT3Uib-Tj4o9WlgozxgaEo_m0ZNU6lc1Xp-AvJ_LZ2oFfqmAMUv9hE_4gIDmf_Ya0yG8_h3YYGudfgpxXnNLFOxMqRwwcYnkFGVa2ZzHSet46vlR2kDyIVUtLmLEWVSthtYO-Cb5ctlJT83tRewpnPIPWRPUzvkwVB0B9Ko50Wrs3zyO4GOn-lnVA"
aos_base_url=aos_base_url_sit
C=Check()
phoneCode="852"
phoneNo=Randoms().number()
# phoneNo='70617789'
idNumber=Randoms().telephone()

# phoneCode="86"
# phoneNo="19725494746"
"""邮寄方式"""
class Eddid(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    # @unittest.skip("fail")
    def test_01_getmsg(self):
        url = aos_base_url + "/api/v2/users/public/smscode?phone={}&deviceId=c3d8e6c83dadfd743bd2a1dd6837c83e".format(phoneCode+phoneNo)
        header = {"Content-Type": "application/json", "x-token": x_token}
        print("获取验证码接口请求",url)
        res=requests.get(url=url,headers=header)
        print("01获取验证码接口返回",res.json())

    # @classmethod
    # @unittest.skip("fail")
    def test_02_login(self):#登录获取token
        url=aos_base_url+"/api/v2/users/public/login"
        data={
            "phone":"6679992",
            "password":"",
            "vcode":"923610",
            "deviceId":"c3d8e6c83dadfd743bd2a1dd6837c83e",
            "referralCode":"",
            "learnHowCode":"",#EDAA5
            "phoneAreaCode":"+852",
            "customerSource":"H5",
            "isOverseas":None,
            "referrerUrl":"",
            "locationUrl":"https://aos-hk-qa.eddid.com.cn:1443/"
        }
        data['vcode']=get_msg(phoneNo)
        data['phone'] =phoneNo
        data['phoneAreaCode']="+"+phoneCode

        header = {"Content-Type": "application/json", "x-token":x_token}
        print("02请求地址{},请求数据{}".format(url,data))
        res=requests.post(url=url,json=data,headers=header)
        print("02",res.text)
        global token
        token=res.json()["data"]["access_token"]

        # print("9999")
        # print(token)
        # print(type(token))
        # return token

    # @unittest.skip("fail")
    def test_03_token(self):#登录获取token
        url=aos_base_url+"/api/v2/users/public/token"
        data={
        "token":token,
        "password":"",
        "vcode":"483679",
        "deviceId":"c3d8e6c83dadfd743bd2a1dd6837c83e",
        "referralCode":"",
        "learnHowCode":"GLAA",#EDAA
        "phoneAreaCode":"+852",
        "customerSource":"H5",
        "isOverseas":None,
        "referrerUrl":"",
        "locationUrl":"https://aos-hk-qa.eddid.com.cn:1443/",
        "currentStep":"/choose-account-type"
    }

        header = {"Content-Type": "application/json", "x-token": token}

        res=requests.post(url=url,json=data,headers=header)
        global applyCode
        applyCode=res.json()['data']['applyCode']#申请编号
        print("申请编号为：",applyCode)
        print("03",res.json())

    # @unittest.skip("fail")
    def test_04_overseas_step(self):
        url = aos_base_url+"/api/v2/profiles/overseas-step"#
        # headers={"Cookie: LANGUAGE=zh_CN; GB-SYS-SID-SIT=75D56AB91FBBE7B7BAB3DB47763B12C47AC79FFD18F78973"}
        header = {"Content-Type": "application/json", "x-token":token}
        data={"area":"HKG","isOverseas":True,"currentStep":"/overseas-identity-verification"}

        res = requests.put(url=url, json=data, headers=header)
        print("04overseas step",res.json())

    """填写身份信息"""
    # @unittest.skip("fail")
    def test_05_overseas_identity(self):
        url = aos_base_url+"/api/v2/profiles/overseas-identity"#
        # headers={"Cookie: LANGUAGE=zh_CN; GB-SYS-SID-SIT=75D56AB91FBBE7B7BAB3DB47763B12C47AC79FFD18F78973"}
        header = {"Content-Type": "application/json", "x-token":token}
        """香港（非永久）"""
        data={
            "area":"HKG",
            "idCardFrontImg":"sync/aos/299bac8e-e5b5-437b-9b40-b2e77828670a.jpg",
            "idCardReverseImg":"",
            "chineseName":"韩梅梅",
            "pinyinLastName":"LI",#wong   zhou    zhou  xuan
            "pinyinFirstName":"tian",#heng(不要动我账号!!!)   jie
            "idNumber":"649943441(1)",
            "idCardIssuedBy":"HKG",#澳门  台湾TWN
            "email":"z99836711@16.com",
            "birthday":65246400000,
            "country":"HKG",
            "gender":0,
            "idType":"5",
            "otherPersonalID":[
                "sync/aos/07b1c5e7-e983-4fc2-bb3f-e84027619213.jpg",
                "sync/aos/6ddc4b3b-906a-4f69-8002-58ee78fbe6a6.jpg"
            ],
            "currentStep":"/personal-information"
        }
        """香港（永久）"""
        data5={
            "area":"HKG",
            "idCardFrontImg":"sync/aos/5dd53cc7-5f8a-416c-9c95-e4e91eb7c13d.jpg",
            "idCardReverseImg":"",
            "chineseName":"邮件",
            "pinyinLastName":"test",
            "pinyinFirstName":"mail",
            "idNumber":"5452435422(5)",
            "idCardIssuedBy":"HKG",
            "email":"zhangxiaozeng24356@126.com",
            "birthday":860904000000,
            "country":"HKG",
            "gender":0,
            "idType":"1",
            "otherPersonalID":[

            ],
            "currentStep":"/personal-information"
        }
        """澳门身份证（非永久）"""
        data1={
            "area":"MAC",
            "idCardFrontImg":"sync/aos/299bac8e-e5b5-437b-9b40-b2e77828670a.jpg",
            "idCardReverseImg":"sync/aos/82c049e8-85f4-4441-b823-e046d1bb9877.jpg",
            "chineseName":"澳门",
            "pinyinLastName":"Kary",
            "pinyinFirstName":"test267",
            "idNumber":"6499434641(11)",
            "idCardIssuedBy":"MAC",
            "email":"z9983616711@16.com",
            "birthday":65246400000,
            "country":"MAC",
            "gender":0,
            "idType":"7",
            "otherPersonalID":[
                "sync/aos/dad48504-a18a-4438-bc1c-6e9601a0e654.jpg"
            ],
            "currentStep":"/personal-information"
        }
        """澳门身份证（永久）"""
        data2={
                "area":"MAC",
                "idCardFrontImg":"sync/aos/299bac8e-e5b5-437b-9b40-b2e77828670a.jpg",
                "idCardReverseImg":"sync/aos/f38d46cc-58cf-4c85-941c-20780aca2bf3.jpg",
                "chineseName":"陈飞",
                "pinyinLastName":"li",
                "pinyinFirstName":"tian",
                "idNumber":"6499434641(11)",
                "idCardIssuedBy":"MAC",
                "email":"z9983616711@16.com",
                "birthday":65246400000,
                "country":"MAC",
                "gender":0,
                "idType":"6",
                "otherPersonalID":[

                ],
                "currentStep":"/personal-information"
            }
        """护照"""
        data3={
            "area":"MAC",
            "idCardFrontImg":"sync/aos/fac7f359-ba39-4288-a0a1-9288fa2c2f3e.jpg",
            "idCardReverseImg":"",
            "chineseName":"护照",
            "pinyinLastName":"tets",
            "pinyinFirstName":"expir",
            "idNumber":"767667376(7)",
            "idCardIssuedBy":"TWN",
            "email":"2232@11.com",
            "birthday":-430603200000,
            "country":"TWN",
            "gender":0,
            "idType":"3",
            "otherPersonalID":[

            ],
            "idCardExpireAt":"2029/05/11",
            "currentStep":"/personal-information"
        }
        data['idNumber']=idNumber
        # data['idNumber']='test13400003009'

        data['email'] = data['idNumber']+'@1631.com'
        # data['email']='zhangxiaozeng240@126.com'

        # header = {"Content-Type": "application/json", "x-token": token}
        res = requests.put(url=url, json=data, headers=header)
        print("tt")
        print("05",res.text)
    """填写资料--个人信息"""
    # @unittest.skip("fail")
    def test_06_personal_information(self):
        url = aos_base_url+"/api/v2/profiles/personal-information"#
        # headers={"Cookie: LANGUAGE=zh_CN; GB-SYS-SID-SIT=75D56AB91FBBE7B7BAB3DB47763B12C47AC79FFD18F78973"}
        header = {"Content-Type": "application/json", "x-token":token}
        #无业
        data1={
            "employment":"unemployed",
            "occupation":"",
            "isRegisteredCompany":"",
            "employer":"",
            "businessTypeOther":"",
            "businessAddress":"",
            "residentialAddress":"656655",
            "resideAddrSameAsIdAddr":False,
            "proofOfResideAddr":[
                "sync/aos/14cfe354-1cdf-4ec5-8b25-9f92d2f36417.jpg"
            ],
            "currentStep":"/investment-financial"
        }

        data={
        "employment":"employed",
        "occupation":"cesces职位",
        "overCountry":"HKG",#居住国
        "isRegisteredCompany":"",
        "employer":"公司全称",
        "businessTypeOpt":"financial&bank",#financial&bank   governmentalAgencies
        "businessTypeOther":"",
        "businessAddress":"Macao办公室地址",
        "residentialAddress":"ces",
        "resideAddrSameAsIdAddr":False,
        "proofOfResideAddr":[
            "sync/aos/c21c2866-0881-4df4-84f1-2762c1bffcef.jpg"
        ],
        "currentStep":"/investment-financial"
    }
        res = requests.put(url=url, json=data, headers=header)
        print("06",res.json())

    """填写资料--投资及财务状况"""
    # @unittest.skip("fail")
    def test_07_financials(self):
        url = aos_base_url+"/api/v2/profiles/financials"#
        # headers={"Cookie: LANGUAGE=zh_CN; GB-SYS-SID-SIT=75D56AB91FBBE7B7BAB3DB47763B12C47AC79FFD18F78973"}
        header = {"Content-Type": "application/json", "x-token":token}
        data={
            "totalAnnualCustomerRevenueHK":"lt200000",
            "customerNetAssetValueHK":"lt1000000",
            "riskTolerance":"high",
            "securities":"1To5Years",
            "CBBC":"lt1Year",
            "warrants":"lt1Year",
            "futures":"1To5Years",
            "options":"lt1Year",
            "currentStep":"/tax-information",
            "totalAnnualCustomerRevenueHKSource":[

            ],
            "totalAnnualCustomerRevenueHKImg":"",
            "customerNetAssetValueHKSource":[

            ],
            "customerNetAssetValueHKImg":"",
            "sourceOfWealth":[
                "savings"
            ],
            "purposeOfInvestment":[
                "speculation",
                "hedging",
                "asset"
            ]
        }
        res = requests.put(url=url, json=data, headers=header)
        print("07",res.json())

    """填写资料--税务信息"""
    # @unittest.skip("fail")
    def test_08_overseas_taxinfo(self):
        url = aos_base_url+"/api/v2/profiles/overseas-taxinfo"#
        # headers={"Cookie: LANGUAGE=zh_CN; GB-SYS-SID-SIT=75D56AB91FBBE7B7BAB3DB47763B12C47AC79FFD18F78973"}
        header = {"Content-Type": "application/json", "x-token":token}
        data={"taxInfo":[{"country":"HKG","hasTaxNo":"Y","taxNo":"1223(1)","noTaxOption":"","noTaxReason":""}],"currentStep":"/account-information"}
        data["taxInfo"][0]["taxNo"] = idNumber
        res = requests.put(url=url, json=data, headers=header)
        print("08",res.json())

    """账户信息--选择开户账户"""
    # @unittest.skip("fail")
    def test_09_account_information(self):
        url = aos_base_url+"/api/v2/profiles/account-information"#
        # headers={"Cookie: LANGUAGE=zh_CN; GB-SYS-SID-SIT=75D56AB91FBBE7B7BAB3DB47763B12C47AC79FFD18F78973"}
        header = {"Content-Type": "application/json", "x-token":token}
        data={
            "accountType":[
                "securitiesMargin"
            ],#["securitiesMargin"：证券保证金 "futuresMargin":期货]
            "isMarginAccount":"N",
            "marginAccountName":"",
            "marginAccountNumber":"",
            "isDiscretion":"N",
            "discretionName":"",
            "discretionNumber":"",
            "isCompanyAccounts":"N",
            "companyAccountsName":"",
            "companyAccountsNumber":"",
            "isApplyToOpenTradingStructure":"Y",
            "tradingStructureRiskChecked":"Y",
            "isLearnAboutProducts":"Y",
            "isStocks":"Y",
            "isIndustryExperience":"N",
            "currentStep":"/customer-statement"
        }
        res = requests.put(url=url, json=data, headers=header)
        print("09",res.json())

    """协议披露--背景资料"""
    # @unittest.skip("fail")
    def test_10_customer_statement(self):
        url = aos_base_url+"/api/v2/profiles/customer-statement"#
        # headers={"Cookie: LANGUAGE=zh_CN; GB-SYS-SID-SIT=75D56AB91FBBE7B7BAB3DB47763B12C47AC79FFD18F78973"}
        header = {"Content-Type": "application/json", "x-token":token}
        data={
        "currentStep":"/risk-disclosure",
        "isBeneficiary":"Y",
        "isOrders":"Y",
        "isBankruptcy":"N",
        "isInAgtJobs":"N",
        "isBondFuturesClientsConnected":"N",
        "isAcquaintHighLevel":"N",
        "isAmericanResidents":"N",
        "isAmericanResidentsb":"N",
        "isPoliticalFigure":"N",
        "salesAgreed":"Y",
        "isSeventyYearsAgree":""#是否七十岁
    }
        res = requests.put(url=url, json=data, headers=header)
        print("10",res.json())

    """协议披露--风险披露"""
    # @unittest.skip("fail")
    def test_11_risk_disclosure(self):
        url = aos_base_url+"/api/v2/profiles/risk-disclosure"#
        # headers={"Cookie: LANGUAGE=zh_CN; GB-SYS-SID-SIT=75D56AB91FBBE7B7BAB3DB47763B12C47AC79FFD18F78973"}
        header = {"Content-Type": "application/json", "x-token":token}
        data={
            "riskDisclosureChecked":"Y",
            "signatureChecked":"Y",
            "voiceListened":False,
            "currentStep":"/signature"
        }
        res = requests.put(url=url, json=data, headers=header)
        print("11",res.json())

    """协议披露--签署"""
    # @unittest.skip("fail")
    def test_12_get_signature(self):
        url = aos_base_url+"/api/v2/profiles/signature"#
        # headers={"Cookie: LANGUAGE=zh_CN; GB-SYS-SID-SIT=75D56AB91FBBE7B7BAB3DB47763B12C47AC79FFD18F78973"}
        header = {"Content-Type": "application/json", "x-token":token}
        res = requests.get(url=url,  headers=header)
        print("12",res.json())
    # @unittest.skip("fail")
    def test_13_signature(self):
        url = aos_base_url+"/api/v2/profiles/signature"#
        # headers={"Cookie: LANGUAGE=zh_CN; GB-SYS-SID-SIT=75D56AB91FBBE7B7BAB3DB47763B12C47AC79FFD18F78973"}
        header = {"Content-Type": "application/json", "x-token":token}
        # data={"base64":"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","json":"[{\"color\":\"black\",\"points\":[{\"time\":1611995016355,\"x\":91.57142639160156,\"y\":226.02040100097656},{\"time\":1611995016394,\"x\":99.73469543457031,\"y\":229.08163452148438},{\"time\":1611995016427,\"x\":115.04081726074219,\"y\":238.26528930664062},{\"time\":1611995016449,\"x\":133.4081573486328,\"y\":247.448974609375},{\"time\":1611995016479,\"x\":142.59182739257812,\"y\":255.61224365234375},{\"time\":1611995016514,\"x\":145.65306091308594,\"y\":260.71429443359375},{\"time\":1611995016565,\"x\":141.57142639160156,\"y\":269.89794921875},{\"time\":1611995016598,\"x\":129.32652282714844,\"y\":280.10205078125},{\"time\":1611995016619,\"x\":110.95918273925781,\"y\":287.2449035644531},{\"time\":1611995016636,\"x\":89.53060913085938,\"y\":294.38775634765625},{\"time\":1611995016669,\"x\":82.38775634765625,\"y\":298.4693908691406},{\"time\":1611995016919,\"x\":90.551025390625,\"y\":305.61224365234375},{\"time\":1611995016946,\"x\":106.87754821777344,\"y\":313.7755126953125},{\"time\":1611995016966,\"x\":126.26530456542969,\"y\":321.93878173828125},{\"time\":1611995016990,\"x\":133.4081573486328,\"y\":327.0408020019531},{\"time\":1611995017071,\"x\":126.26530456542969,\"y\":337.2449035644531},{\"time\":1611995017088,\"x\":122.18367004394531,\"y\":341.3265380859375},{\"time\":1611995017105,\"x\":109.93876647949219,\"y\":352.551025390625},{\"time\":1611995017122,\"x\":99.73469543457031,\"y\":357.6530456542969},{\"time\":1611995017139,\"x\":91.57142639160156,\"y\":361.73468017578125},{\"time\":1611995017167,\"x\":87.48979187011719,\"y\":364.7959289550781},{\"time\":1611995017184,\"x\":82.38775634765625,\"y\":369.89794921875},{\"time\":1611995017218,\"x\":76.26530456542969,\"y\":372.95916748046875},{\"time\":1611995017356,\"x\":72.18367004394531,\"y\":376.0204162597656}]}]","currentStep":"/identity-prove"}
        data={"base64":"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","json":"[{\"color\":\"black\",\"points\":[{\"time\":1627988193046,\"x\":95,\"y\":262},{\"time\":1627988193064,\"x\":105,\"y\":267},{\"time\":1627988193080,\"x\":114,\"y\":271},{\"time\":1627988193096,\"x\":124,\"y\":279},{\"time\":1627988193112,\"x\":130,\"y\":288},{\"time\":1627988193128,\"x\":132,\"y\":300},{\"time\":1627988193161,\"x\":127,\"y\":324},{\"time\":1627988193179,\"x\":119,\"y\":333},{\"time\":1627988193197,\"x\":109,\"y\":340},{\"time\":1627988193214,\"x\":99,\"y\":345},{\"time\":1627988193232,\"x\":92,\"y\":346},{\"time\":1627988193250,\"x\":86,\"y\":347},{\"time\":1627988193330,\"x\":83,\"y\":340},{\"time\":1627988193346,\"x\":88,\"y\":334},{\"time\":1627988193363,\"x\":95,\"y\":331},{\"time\":1627988193380,\"x\":108,\"y\":328},{\"time\":1627988193397,\"x\":120,\"y\":328},{\"time\":1627988193415,\"x\":130,\"y\":328},{\"time\":1627988193432,\"x\":135,\"y\":330},{\"time\":1627988193448,\"x\":140,\"y\":336},{\"time\":1627988193464,\"x\":142,\"y\":341},{\"time\":1627988193480,\"x\":145,\"y\":349},{\"time\":1627988193512,\"x\":145,\"y\":359},{\"time\":1627988193528,\"x\":144,\"y\":365},{\"time\":1627988193544,\"x\":140,\"y\":372},{\"time\":1627988193560,\"x\":135,\"y\":379},{\"time\":1627988193594,\"x\":126,\"y\":386},{\"time\":1627988193610,\"x\":121,\"y\":391},{\"time\":1627988193642,\"x\":116,\"y\":395},{\"time\":1627988193672,\"x\":110,\"y\":399}]}]","currentStep":"/identity-prove"}
        res = requests.put(url=url, json=data, headers=header)
        print("13",res.json())
    """网上见证"""
    # @unittest.skip("fail")
    def test_14_overseas_witness_mail(self):
        url = aos_base_url+"/api/v2/profiles/overseas-witness"#
        # headers={"Cookie: LANGUAGE=zh_CN; GB-SYS-SID-SIT=75D56AB91FBBE7B7BAB3DB47763B12C47AC79FFD18F78973"}
        header = {"Content-Type": "application/json", "x-token":token}
        data={"accountOpeningWay":"mailing","currentStep":"/account-opening-status"}
        res = requests.put(url=url, json=data, headers=header)
        print("提交开户申请")
        print("14",res.json())
    """亲临"""
    # @unittest.skip("fail")
    def test_15_overseas_witness_visitingAccount(self):
        url = aos_base_url+"/api/v2/profiles/overseas-witness"#
        # headers={"Cookie: LANGUAGE=zh_CN; GB-SYS-SID-SIT=75D56AB91FBBE7B7BAB3DB47763B12C47AC79FFD18F78973"}
        header = {"Content-Type": "application/json", "x-token":token}
        data={"accountOpeningWay":"visitingAccount","currentStep":"/account-opening-status"}
        res = requests.put(url=url, json=data, headers=header)
        print("提交开户申请")
        print("15",res.json())
    """fps"""
    # @unittest.skip("fail")
    def test_16_overseas_witness_fps(self):
        url = aos_base_url+"/api/v2/profiles/overseas-witness"#
        # headers={"Cookie: LANGUAGE=zh_CN; GB-SYS-SID-SIT=75D56AB91FBBE7B7BAB3DB47763B12C47AC79FFD18F78973"}
        header = {"Content-Type": "application/json", "x-token":token}
        # data={"accountOpeningWay":"fps","currentStep":"/bind-bank"}
        data={"accountOpeningWay":"fps","currentStep":"/bind-bank"}
        res = requests.put(url=url, json=data, headers=header)
        print("提交开户申请")
        print("15",res.json())

    # @unittest.skip("fail")
    def test_17_overseas_bank_fps(self):
        url = aos_base_url+"/api/v2/profiles/overseas-bank"#
        # headers={"Cookie: LANGUAGE=zh_CN; GB-SYS-SID-SIT=75D56AB91FBBE7B7BAB3DB47763B12C47AC79FFD18F78973"}
        header = {"Content-Type": "application/json", "x-token":token}
        data={
                "currentStep":"/transfer",
                "bankAccount":[
                    {
                        "name":"004",
                        "nameText":"香港上海匯豐銀行有限公司 004",
                        "number":"565666",
                        "holder":"Kary test245",
                        "bankCertificates":[

                        ]
                    }
                ]
            }
        res = requests.put(url=url, json=data, headers=header)
        print("17 overseas-bank", res.json())

    # @unittest.skip("fail")
    def test_18_overseas_deposit(self):
        url = aos_base_url+"/api/v2/profiles/overseas-deposit"#
        # headers={"Cookie: LANGUAGE=zh_CN; GB-SYS-SID-SIT=75D56AB91FBBE7B7BAB3DB47763B12C47AC79FFD18F78973"}
        header = {"Content-Type": "application/json", "x-token":token}
        data={
            "currentStep":"/account-opening-status",
            "depositType":"fps_deposit",
            "eddidBankName":"FPSstock",
            "eddidBank":"7853658",
            "exchangedAmount":4554,#金额
            "exchangedCurrency":"HKD",
            "depositCertificate":[
                "sync/aos/c31bd811-3b3c-4eb8-aa01-cd4ce1d94867.jpg"
            ],
            "bankAccount":[
                {
                    "name":"004",
                    "nameText":"香港上海匯豐銀行有限公司 004",
                    "number":"565666",
                    "holder":"Kary test245",
                    "bankCertificates":[
                        "sync/aos/559a4d31-8ba8-4792-90f7-bd53ad1a1be6.jpg"
                    ]
                }
            ]
        }
        res = requests.put(url=url, json=data, headers=header)
        print("18", res.json())


    """CS2锁定"""
    # @unittest.skip("fail")
    def test_19_lock(self):
        global apply_id
        apply_id=C.get_cdmsdb_con(database="eddid_gfss_sit",sql="select apply_id from cd_clnt_apply_basisinfo where apply_no='{}'".format(applyCode))
        print("申请编号：{},applyId：{}".format(applyCode,apply_id))

        print("申请编号：{},applyId：{}".format(applyCode,apply_id))
        url=base_url+"/api/common/operatingWorkFlow"
        header = {"Content-Type": "application/json", "Cookie": "GB-SYS-SID-SIT=" + token}
        data={"applyId":apply_id,"workFlowCode":"openClient","controlCode":"LOCK"}
        print("CS2锁定请求参数：{}".format(data))
        res = requests.post(url=url, json=data, headers=header)
        print(res.json())

    """CS2审核"""
    # @unittest.skip("fail")
    def test_4_operatingWorkFlow(self):
        url=base_url+"/api/common/operatingWorkFlow"
        header = {"Content-Type": "application/json", "Cookie": "GB-SYS-SID-SIT=" + token}
        data={
        "applyId":apply_id,
        "checkItemList":[
            {
                "itemId":"1",
                "itemCde":"Application Form",
                "itemDesc":"Application Form",
                "cscheckFlag":True,
                "rocheckFlag":False,
                "opscheckFlag":False
            },
            {
                "itemId":"2",
                "itemCde":"Fee schedule",
                "itemDesc":"Fee schedule",
                "cscheckFlag":True,
                "rocheckFlag":False,
                "opscheckFlag":False
            },
            {
                "itemId":"3",
                "itemCde":"ID card Copy",
                "itemDesc":"ID card Copy",
                "cscheckFlag":True,
                "rocheckFlag":False,
                "opscheckFlag":False
            },
            {
                "itemId":"4",
                "itemCde":"SFC search",
                "itemDesc":"SFC search",
                "cscheckFlag":True,
                "rocheckFlag":False,
                "opscheckFlag":False
            },
            {
                "itemId":"5",
                "itemCde":"Worldcheck",
                "itemDesc":"Worldcheck",
                "cscheckFlag":False,
                "rocheckFlag":False,
                "opscheckFlag":False
            },
            {
                "itemId":"6",
                "itemCde":"Address Proof (if any)",
                "itemDesc":"Address Proof (if any)",
                "cscheckFlag":False,
                "rocheckFlag":False,
                "opscheckFlag":False
            },
            {
                "itemId":"7",
                "itemCde":"Bank proof (if any)",
                "itemDesc":"Bank proof (if any)",
                "cscheckFlag":False,
                "rocheckFlag":False,
                "opscheckFlag":False
            },
            {
                "itemId":"8",
                "itemCde":"Source of Fund (if any)",
                "itemDesc":"Source of Fund (if any)",
                "cscheckFlag":False,
                "rocheckFlag":False,
                "opscheckFlag":False
            },
            {
                "itemId":"9",
                "itemCde":"Source of Wealth (if any)",
                "itemDesc":"Source of Wealth (if any)",
                "cscheckFlag":False,
                "rocheckFlag":False,
                "opscheckFlag":False
            },
            {
                "itemId":"10",
                "itemCde":"Other",
                "itemDesc":"Other",
                "cscheckFlag":False,
                "rocheckFlag":False,
                "opscheckFlag":False
            }
        ],
        "workFlowCode":"openClient",
        "controlCode":"PASS",
        "lockBy":"ED_RO",
        "licensedPersonSign":""
    }
        print("CS2审核请求参数：{}".format(data))
        res = requests.post(url=url, json=data, headers=header)
        print(res.json())
        # apply_id=res.json()['apply_id']
        try:
            self.stat_cde = C.get_cdmsdb_con(database="eddid_gfss_sit",sql="SELECT stat_cde FROM gs_apply_work_flow WHERE apply_id ={} AND wrkflw_cde='openClient';".format(apply_id))[0][0]
            print(self.stat_cde)
        except:
            print("没有找到对应的审核流程")
        stat_cde_except="RO_HANDLEING"#RO_HANDLEING
        self.assertEqual(self.stat_cde,stat_cde_except)
        print("CS2审核之后状态应该为:{},实际结果为：{}".format(stat_cde_except,self.stat_cde))





# if __name__=="__main__":
#     unittest.main()

if __name__=="__main__":
    basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 获取工程目录
    sys.path.extend([basedir])
    print(basedir)
    test_dir=basedir+"\\casesuit\\CDMS"
    # suiteTest=unittest.defaultTestLoader.discover(basedir,pattern='create_client.py')
    # now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # fp = open('F:\\Interface_test\\result\\' + now + '开户审核状态' + '.html', 'wb')  # 测试报告命名
    # runner = HTMLTestRunner(stream=fp, title="python test result",
    #                                   description='this is the result:')
    # runner.run(suiteTest)
    # print ("result is ok")
    # time.sleep(3)
    # fp.close()

    testcases_mail=[Eddid("test_01_getmsg"),Eddid("test_02_login"),Eddid("test_03_token"),Eddid("test_04_overseas_step"),Eddid("test_05_overseas_identity")
               ,Eddid("test_06_personal_information"),Eddid("test_07_financials"),Eddid("test_08_overseas_taxinfo"),Eddid("test_09_account_information")
               ,Eddid("test_10_customer_statement"),Eddid("test_11_risk_disclosure"),Eddid("test_12_get_signature"),Eddid("test_13_signature")
                ,Eddid("test_14_overseas_witness_mail")]

    testcases_fps=[Eddid("test_01_getmsg"),Eddid("test_02_login"),Eddid("test_03_token"),Eddid("test_04_overseas_step"),Eddid("test_05_overseas_identity")
               ,Eddid("test_06_personal_information"),Eddid("test_07_financials"),Eddid("test_08_overseas_taxinfo"),Eddid("test_09_account_information")
               ,Eddid("test_10_customer_statement"),Eddid("test_11_risk_disclosure"),Eddid("test_12_get_signature"),Eddid("test_13_signature")
                ,Eddid("test_16_overseas_witness_fps"),Eddid("test_17_overseas_bank_fps"),Eddid("test_18_overseas_deposit")]

    testcases_vA=[Eddid("test_01_getmsg"),Eddid("test_02_login"),Eddid("test_03_token"),Eddid("test_04_overseas_step"),Eddid("test_05_overseas_identity")
               ,Eddid("test_06_personal_information"),Eddid("test_07_financials"),Eddid("test_08_overseas_taxinfo"),Eddid("test_09_account_information")
               ,Eddid("test_10_customer_statement"),Eddid("test_11_risk_disclosure"),Eddid("test_12_get_signature"),Eddid("test_13_signature")
                ,Eddid("test_15_overseas_witness_visitingAccount")]


    testcases_te=[Eddid("test_01_getmsg"),Eddid("test_02_login"),Eddid("test_03_token")]
    suite = unittest.TestSuite()
    # suite.addTests(testcases_mail)#testcases_fps:fps、testcases_vA：亲临、testcases_mail：邮寄方式
    # suite.addTests(testcases_fps)#fps方式
    suite.addTests(testcases_vA)#亲临方式
    # suite.addTests(testcases_te)#调试
    # 执行测试
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


# class ChoiceRegi():
#     def through_mail(self):
#         testcases_mail = [Eddid("test_01_getmsg"), Eddid("test_02_login"), Eddid("test_03_token"),
#                           Eddid("test_04_overseas_step"), Eddid("test_05_overseas_identity")
#             , Eddid("test_06_personal_information"), Eddid("test_07_financials"), Eddid("test_08_overseas_taxinfo"),
#                           Eddid("test_09_account_information")
#             , Eddid("test_10_customer_statement"), Eddid("test_11_risk_disclosure"), Eddid("test_12_get_signature"),
#                           Eddid("test_13_signature")
#             , Eddid("test_14_overseas_witness_mail")]
#         suite = unittest.TestSuite()
#         suite.addTests(testcases_mail)  # mail方式
#         runner = unittest.TextTestRunner(verbosity=2)
#         runner.run(suite)
#
# if __name__=="__main__":
#     CR=ChoiceRegi()
#     CR.through_mail()
