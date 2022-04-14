# -*- coding:utf-8 -*-
import requests
from Business.login import cdms_获取token
from Common.random_number import Randoms
import logging
from Common.com_sql.eddid_data_update import *
import time
from Common.com_sql.eddid_data_select import *
from Config.cdms_config import *
from Common.data_文本读写 import *


class CreatUser():
    def SaveApplyClient(self):
        global phone,countryCode
        eddidhost=url
        cookfront = cookfr
        applyClienturl = eddidhost + "/api/corporateClient/saveApplyClient"
        # token=data_read('F:\\python\\EDDID_CDMS\\Data\\token.txt')
        token = cdms_获取token()
        s = requests.Session()
        phone0= Randoms().telephone()
        phone1 = Randoms().telephone()
        phone2 = Randoms().telephone()

        print("_____________________________")
        print("phone0=={}".format(phone0))
        print("phone1=={}".format(phone1))
        print("phone2=={}".format(phone2))
        cantrCode= "CHN"
        # cantrCode = "HKG"
        # cantrCode ="MYS"
        #身份证类型 香港为"1" 大陆为"2"
        idCardT = "2"

        cremail0 = Randoms.RandomEmail()
        cremail1 = Randoms.RandomEmail()
        cremail2 = Randoms.RandomEmail()

        print("_____________________________")
        print("cremail0=={}".format(cremail0))
        print("cremail1=={}".format(cremail1))
        print("cremail2=={}".format(cremail2))
        # cremail="ganjiexiang6@126.com"
        # 英文名firstName
        rfirstName = Randoms().creat_EFName()
        # rfirstName = "Tom"
        # 英文姓lastName
        rlastName = Randoms().creat_ELName()
        # rlastName = "Leung"
        # 中文名chName
        rchName = Randoms().creat_CHName()
        # rchName = "Sheldon Yuen"
        # 生成身份证号
        idCardNo0 = Randoms().ident_generator()
        idCardNo1 = Randoms().ident_generator()
        idCardNo2 = Randoms().ident_generator()

        print("_____________________________")
        print("idCardNo0=={}".format(idCardNo0))
        print("idCardNo1=={}".format(idCardNo1))
        print("idCardNo2=={}".format(idCardNo2))
        # idCardNo="D9625128"

        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": cookfront + token
        }
        data = {
            "infos": [
                {
                    #公司授权人士资料
                    "title": "mr", #称谓
                    "firstName": "dd"+ rfirstName, #名字
                    "lastName": "dd"+ rlastName, #姓氏
                    "chName": rchName, #授权中文
                    "usedCnName": "shouquancy",  #曾用英文姓名
                    "usedChName": "shouquancyz", #曾用中文名
                    "idType": idCardT,  #证件类型
                    "idNumber": idCardNo0,  #证件号码
                    # "idNumber": 6611151123125151515,  #证件号码
                    "countryCode": cantrCode,  #国籍
                    "countryIssue": cantrCode, #签证国家
                    "birthday": "1997-03-01", #出生日期
                    "birthdayPlace": cantrCode,  #出生地点国家
                    "phoneCountry": cantrCode, #电话区号
                    "phone": phone0, #电话号
                    "address": "自动化提交住址"+phone0, #住宅地址
                    "postAddress": "自动化提交邮寄地址"+phone0, #邮寄地址
                    "isUsPerson": "N",  #是否美国公民
                    "socialNumber": "",
                    "isUsTaxPerson": "N",  #是否美国税务人员
                    "usTaxNumber": "",
                    "isOtherResidents": "N", #是否是其他国家纳税人
                    "residencyJurisdiction": "",
                    "jurisdictionTaxNumber": "",
                    "employmentStatus": "employed", #就业情况
                    "post": "seniorManagement", #职位
                    "workingYear": "12", #受雇年限
                    "companyName": "自动化公司名称"+phone0, #目前雇主名称
                    "businessNature": "financial",  #业务性质
                    "businessAddress": "自动化公司地址"+phone0, #办公司地址
                    "businessPhone": "564"+phone0, #办公室电话
                    "type": "ap"
                },
                {
                    #股东资料
                    "firstName": rfirstName, #名字 ？？
                    "lastName": rlastName, #姓氏
                    "chName": rchName, #中文名
                    "address": "gdonggdong"+phone0,  #住宅地址
                    "countryCode": "GLP",  #国籍
                    "idType": idCardT, #身份证类型
                    # "idNumber": 150101195805091331, #证件号
                    "idNumber": idCardNo1, #证件号
                    "birthday": "1994-03-01",
                    "birthdayPlace": "GLP", #出生地
                    "percentageOwnership": "21", #拥有权百分比
                    "type": "shhldr"
                },
                {
                    # 董事资料
                    "name": rfirstName, #？？
                    # "idCard": idCardNo1, #身份证号 ？？
                    # "idCard": 98745645455,  # 身份证号 ？？
                    "birthday": "1988-03-02", #出生日期
                    "birthdayPlace": "MHL", #出生地点
                    "address": "姓氏", #住宅地址
                    "natnlty": "",
                    "firstName": "姓氏",  #姓氏
                    "lastName": "名字", #名字
                    "chName": "中文", #中文姓名
                    "countryCode": "FJI", #国籍
                    "idType": "1", #身份证类型
                    "idNumber": idCardNo1,
                    # "idNumber": 9874521452155,
                    "type": "prsn"
                },

                {
                # 賬戶最終實益擁有人
                     "firstName": "dasdas",  #名字
                    "lastName": "ganj", #姓氏
                    "chName": "撒旦", #中文名
                    "idNumber": "545546461", #证件号码
                    "idType": idCardT,  #证件类型
                    "address": "撒旦撒旦", #住宅地址
                    "countryIssue": "WLF", #签发国家
                    "countryCode": "FJI",  #国籍
                    "phone": phone1, #电话号
                    # "phone":10172370144,
                    "type": "bo"
                }
            ],
            "attachs": {

            },
            "accts": [
                # caccts
                "securitiesCash",
                # 证券现金
                # "securitiesMargin",
                # 证券保证金
                "futuresMargin",
                # 期货保证金
                "leveragedForeignExchangeAccountMargin",
                # 杠杆式外汇账户(保证金)
            ],
            #公司账户资料
            "openWay": "visitingAccount",
            # "openWay": "postal",
            #开户方式：visitingAccount 亲临开户；邮件开户
            "cnName": rfirstName,
            #公司英文名
            "chName": rlastName,
            #公司中文名
            "crpratType": "limitedCompany",
            #公司类型
            "idType": "others",
            #公司注册文书类型
            "idNumber": idCardNo1,
            # 公司注册编号
            "birthdayPlace": "FJI",
            # 成立国家
            "birthday": "2022-03-28",
            "businessNature": "financial",
            # 业务性质
            "phone": phone2,
            # 公司电话
            "fax": "5921233878",
            # 公司传真
            "email": cremail2,
            # "email": "ganjiexiang8@126.com",
            # 公司邮箱
            "ccaInvtorAcctName": phone2,
            # 中央结算投资者户口名称
            "ccaInvtorAcctNumber": phone2,
            # 中央结算投资者户口名称及号码
            "address": "注册"+phone2,
            # 注册地址
            "postAddress": "主要业务地址"+phone2,
            # 主要业务地址

            # 公司账户财务及其他资料
            "netAnnualProfit": "{\"2020\":\"66545\",\"2021\":\"3221\",\"2022\":\"2000\"}", #近三年的税后益利
            "authorizedCapital": "1223", #法定股本
            "totalCapital": "231232",#资产净值
            "paidUpcapital": "31223",#缴足股本
            "liquidAssets": "21", #流动资产
            "investmentObjective": [
                "speculation", #投机
                "hedging", #对冲保值
                "asset", #资产增值
                "income", #利息收益
            ],
            # 投资经验及目标
            "withDerivativesKnowledge": "N",
            "withDerivativesDeal": "N",
            "riskTolerance": "medium",
            "securitiesExperience": "lt1Year",
            "securitiesAvgProtfolio": "11",
            "cbbcExperience": "1To5Years",
            "cbbcAvgProtfolio": "22",
            "warrantExperience": "6To10Years",
            "warrantAvgProtfolio": "33",
            "futuresExperience": "gt10Years",
            "futuresAvgProtfolio": "44",
            "optionsExperience": "lt1Year",
            "optionsAvgProtfolio": "55",
            "foreignExchangExperience": "1To5Years",
            "foreignAvgProtfolio": "66",
            "otherInvest": "lt1Year",
            "otherAvgProtfolio": "77",
            "settleAcctS": [

            ],
            "throughChannels": [
                "advertising",
                "forum"
            ],
            "throughChannelRemark": "",
            "promotionNumber": "ACBB",
            "marginAcctS": [

            ],
            "isFuturesMarketParticipantOrSupervisor": "N",
            "futuresMarketParticipantOrSupervisorS": [
                {
                    "actualOwner": "大厦",
                    "institutionName": "2654",
                    "licenceRegistrationNumber": "56546"
                }
            ],
            "isRelationshipWithEDFuture": "N",
            "relationshipWithEDFutureS": [
                {
                    "actualOwner": "",
                    "relationship": ""
                }
            ],
            "haveEverBeenBankrupt": "N",
            "haveEverBeenBankruptS": [
                {
                    "actualOwner": "",
                    "bankruptcyTime": ""
                }
            ],
            "isPepPerson": "N",
            "pepPersonS": [
                {
                    "actualOwner": "",
                    "positionRelationship": ""
                }
            ],
            "checked1": "true",
            "checked2": "true"
        }
        applyClientResp = s.post(url=applyClienturl, headers=headers, json=data)
        logging.info("步骤1接口'{}';请求参数为:{};响应结果为：'{}'".format(applyClienturl, data, applyClientResp.text))
        print("步骤1接口'{}';请求参数为:{};响应结果为：'{}'".format(applyClienturl, data, applyClientResp.text))
        return applyClientResp

    # 步骤1
    def ApplyClinet资料提交(selt):
        global phone, token, eddidhost, s, cremail, rfirstName, rlastName, rchName, idCardNo, cookfront,sheet


        phone = Randoms().telephone()
        # print("phone数据类型************************************************",type(phone))

        # phone = "18123697991"
        # 生成新邮箱
        cremail = Randoms.RandomEmail()
        # cremail="ganjiexiang6@126.com"
        # 英文名firstName
        rfirstName = Randoms().creat_EFName()
        # rfirstName = "Tom"
        # 英文姓lastName
        rlastName = Randoms().creat_ELName()
        # rlastName = "Leung"
        # 中文名chName
        rchName = Randoms().creat_CHName()
        # rchName = "Sheldon Yuen"
        # 生成身份证号
        idCardNo = Randoms().ident_generator()
        # idCardNo="D9625128"
        # 国籍
        cantrCode = "CHN"
        # cantrCode = "HKG"
        # cantrCode ="MYS"
        #身份证类型 香港为"1" 大陆为"2"
        idCardT = "2"
        # cookies的前缀
        cookfront = cookfr
        # 生成称谓（性别）
        #"miss", "mr", "mrs"
        ctitle = "mr"
        # ctitle = Randoms().choice_title()
        # 获取随机的账户类型
        caccts = Randoms().choice_accts()
        # Language = Randoms().choice_Language()
        # 新列表用来存放用户基本信息
        userinformationList = []
        userinformationList.append(phone)
        userinformationList.append(cremail)
        userinformationList.append(rfirstName)
        userinformationList.append(rlastName)
        userinformationList.append(rchName)
        userinformationList.append(idCardNo)
        userinformationList.append(ctitle)
        userinformationList.append(caccts)
        print("userinformationList:", userinformationList)
        # 将userinformationList写入文本
        data_write('F:\\python\\EDDID_CDMS\\Data\\userdatainf.txt', userinformationList)
        print("记录数据的文件名为：userdatainf.txt，写入数据为:{}".format(userinformationList))
        logging.info("记录数据的文件名为：userdatainf.txt，写入数据为:{}".format(userinformationList))
        # 配置文件cdms_config中引入host
        eddidhost = url
        # token=data_read('F:\\python\\EDDID_CDMS\\Data\\token.txt')
        token = cdms_获取token()
        s = requests.Session()
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": cookfront + token
        }
        logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        applyClienturl = eddidhost + "/api/client/applyClient"
        print("applyClienturl:", applyClienturl)
        logging.info("提交申请单时注册用户手机号码为：{}".format(phone))
        data = {
            "infos": [
                {
                    "title": ctitle,
                    "informationType": 1,
                    "firstName": rfirstName,
                    "lastName": rlastName,
                    "chName": rchName,
                    "usedCnName": rlastName + caccts,
                    "usedChName": rchName + "接口自动化创建账号",
                    "email": cremail,
                    "phoneAreaCode": cantrCode,
                    "phoneNo": phone,
                    "houseAddress": "中英街" + caccts + "号",
                    "houseAddressPinYin": "zhon" + caccts + "hao",
                    "postAddress": "接口自动化",
                    "natnlty": cantrCode,

                    "idCardType": idCardT,
                    "idCardNo": idCardNo,
                    "otherCardType": "",
                    "otherCardNo": "",
                    #国家
                    "countryIssue": cantrCode,
                    "overCountry": cantrCode,
                    "birthday": "1994-08-09",
                    "idExpiresDate": "2023-08-31",
                    "birthdayPlace": cantrCode,
                    "employmentStatus": "self",
                    "post": "businessOwner",
                    "workingYear": "11",
                    #公司名称
                    "companyName": "自动化" + caccts,
                    #职业
                    "businessNature": "financial",
                    # "businessNature": "education",
                    #公司地址
                    "officeAddress": "香港47845512245" + caccts,
                    "officePhone": "0825-" + caccts,
                    "registeredCompany": "Y",
                    "employmentRemark": "",
                    "totalIncomeYear": "gt1000000",
                    "sourceOfIncome": [
                        "selfOperatedBusinessIncome",
                        "salary"
                    ],
                    "sourceOfIncomeRemake": "",
                    "totalCapital": "gt8000000",
                    "sourceOfCapital": [
                        "salary",
                        "savings",
                        "pension"
                    ],
                    "sourceOfCapitalRemark": "",
                    "sourceOfMoney": [
                        "selfOperated"
                    ],
                    "sourceOfMoneyRemark": "",
                    "securitiesExperience": "gt10Years",
                    "cbbcExperience": "gt10Years",
                    "warrantExperience": "gt10Years",
                    "futuresExperience": "gt10Years",
                    "optionsExperience": "gt10Years",
                    "foreignExchangExperience": "gt10Years",
                    "metalExperience": "gt10Years",
                    "autoTransationExperience": "gt10Years",
                    "otherInvest": "",
                    "otherExperience": "",
                    "withDerivativesKnowledge": "Y",
                    "withDerivativesWoking": "Y",
                    "withDerivativesDeal": "Y",
                    "applicationOpenDerivatives": "Y",
                    "understandTheRisks": "Y",
                    "haveDeclaredBankruptcy": "N",
                    "declaredBankruptcyDate": "",
                    "isInternalStaff": "N",
                    "staffNameRelationship": "",
                    "relationshipWithInternalEmployees": "Y",
                    "employeesName": "11212",
                    "isRegisteredPerson": "N",
                    "registeredPersonRemark": "",
                    "isUsPerson": "N",
                    "taxNumber": "",
                    "isUsTaxPerson": "N",
                    "taxNumberTwo": "",
                    "isPepPerson": "N",
                    "pepPersonName": "",
                    "investmentObjective": [
                        "asset",
                        "income"
                    ],
                    "riskTolerance": "high",
                    "throughChannels": [
                        "lecture"
                    ],
                    "throughChannelRemark": "",
                    "isFinalBeneficiary": "Y",
                    "finalBeneficiaryName": "",
                    "isFinalPrincipal": "Y",
                    "finalPrincipalName": "",
                    "businessNatureRemark": ""
                }
            ],
            "marginAcctS": [
            ],
            "taxs": [
                {
                    # 居住地
                    "residencyJurisdiction": "CHN",
                    "taxNumber": "",
                    "resonType": "A",
                    "resonRemark": ""
                }
            ],
            "attachs": {
                "passportMaterial": [
                    "/hzlc_20210819191744.jpg"
                ],
                "addressVerificationMaterials": [
                    "/hzlc_20210819191748.jpg"
                ],
                "bankCardMaterials": [
                    "/hzlc_20210819191751.jpg"
                ],
                "proofOfIncome": [
                    "/hzlc_20210819191759.jpg"
                ],
                "writtenApplicationMaterials": [
                    "/APP_20200811142432_20210819191759.pdf"
                ],
                "otherInformation": [
                    "/dinggg_20210819191801.jpg"
                ],
                "bankruptcyProve": [

                ],
                "acquaintHighLevelInstructionsProve": [

                ],
                "tradingAuthorization": [

                ]
            },
            "settleAcctS": [
            ],
            "clientType": "PERSONAL",
            "openWay": "visitingAccount",
            "bankName": "",
            "bankCardNo": "",
            "elecNo": "",
            "responsible": "kwokwah.wong",
            # "emailLanguage": Language,
            "emailLanguage": "zh-hans",
            # 简体
            # "emailLanguage": "zh-hant",
            # 繁体
            "accts": [
                # caccts
                "securitiesCash",
                # 证券现金
                # "securitiesMargin",
                # 证券保证金
                "futuresMargin",
                # 期货保证金
                # "leveragedForeignExchangeAccountMargin",
                # 杠杆式外汇账户(保证金)
                # "securitiesAyersCash"
                # #全权委托证券（现金）账户
            ],
            "promotionNumber": "EDAC520",
            "agreeToTheTerms": "true",
            "personalInfoDeclartion": "true"
        }
        applyClientResp = s.post(url=applyClienturl, headers=headers, json=data)
        logging.info("步骤1接口'{}';请求参数为:{};响应结果为：'{}'".format(applyClienturl, data, applyClientResp.text))
        print("步骤1接口'{}';请求参数为:{};响应结果为：'{}'".format(applyClienturl, data, applyClientResp.text))
        return applyClientResp

    # 步骤2
    def SubmitAudit提交审核(self):
        print("等待系统录入数据后再修改WorldCheck的状态，等待时间40s")
        logging.info("等待系统录入数据后再修改WorldCheck的状态，等待时间40s")
        time.sleep(30)
        cd_clnt_wc_match(phone)
        print(
            "*******************************************已完成修改WorldCheck的状态为FALSE*******************************************")
        logging.info(
            "*******************************************已完成修改WorldCheck的状态为FALSE*******************************************")
        # 必须要等待修改完成后才能提交审核
        time.sleep(40)
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": cookfront + token
        }
        logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        submitAuditurl = eddidhost + "/api/client/submitAudit"
        print("submitAuditurl为:", submitAuditurl)
        logging.info("提交审核获取到的手机号为：{}".format(phone))
        global applyId
        applyId = cd_clnt_apply_info(phone)[0][0]
        print("查询数据库cd_clnt_apply_info查询到applyId的值为：{}".format(applyId))
        data = {
            "applyId": applyId,
            "clientSource": "CDMS",
            "workFlowCode": "openClient"
        }
        print("data=", data)
        SubmitAuditResp = s.post(url=submitAuditurl, headers=headers, json=data)
        logging.info("步骤2提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(submitAuditurl, data, SubmitAuditResp.text))
        print("步骤2提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(submitAuditurl, data, SubmitAuditResp.text))
        return SubmitAuditResp

    # 步骤3
    def operatingWorkFlowFirst提交锁(self):
        time.sleep(35)
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": cookfront + token
        }
        logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        operatingWorkFlowFirsturl = eddidhost + "/api/common/operatingWorkFlow"
        print("submitAuditurl为:", operatingWorkFlowFirsturl)
        logging.info("提交审核获取到的手机号为：{}".format(phone))
        # global applyId
        # applyId = cd_clnt_apply_info(phone)[0][0]
        print("查询数据库cd_clnt_apply_info查询到applyId的值为：{}".format(applyId))
        data = {
            "applyId": applyId,
            "workFlowCode": "openClient",
            "controlCode": "LOCK"
        }
        print("data=", data)
        operatingWorkFlowFirstResp = s.post(url=operatingWorkFlowFirsturl, headers=headers, json=data)
        logging.info("步骤3提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(operatingWorkFlowFirsturl, data,
                                                                operatingWorkFlowFirstResp.text))
        print("步骤3提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(operatingWorkFlowFirsturl, data,
                                                         operatingWorkFlowFirstResp.text))
        return operatingWorkFlowFirstResp

    # 步骤4
    def saveRiskAssessment风控评估提交(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": cookfront + token
        }
        # logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        saveRiskAssessmenturl = eddidhost + "/api/client/saveRiskAssessment"
        print("submitAuditurl为:", saveRiskAssessmenturl)
        logging.info("当前applyId为：{}".format(applyId))
        data = {
            "applyId": applyId,
            "riskAssessmentInfoDTO": {
                "isAmlOrCft": "true",
                "isPeb": None,
                "isPolice": None,
                "isIcac": None,
                "isHighRiskBusiness": None,
                "isJfiu": None,
                "isCorruption": None,
                "isOtherInformation": None,
                "nonFaceToFace": None,
                "isUnemployed": None,
                "isNonFatf": None,
                "isNonFinancial": None,
                "isTemporaryAddr": None,
                "residence": "新西兰",
                "otherInformation": "",
                "riskAssessmentLevel": "TERMINATE"
            }
        }
        print("data=", data)
        saveRiskAssessmentResp = s.post(url=saveRiskAssessmenturl, headers=headers, json=data)
        logging.info(
            "步骤4提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(saveRiskAssessmenturl, data, saveRiskAssessmentResp.text))
        print("步骤4提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(saveRiskAssessmenturl, data, saveRiskAssessmentResp.text))
        return saveRiskAssessmentResp

    # 步骤5
    def operatingWorkFlow内部人员审核(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": cookfront + token
        }
        logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        operatingWorkFlowturl = eddidhost + "/api/common/operatingWorkFlow"

        print("submitAuditurl为:", operatingWorkFlowturl)
        print("当前的applyId的值为：{}".format(applyId))
        data = {
            "applyId": applyId,
            "checkItemList": [
                {
                    "itemId": "1",
                    "itemCde": "Application Form",
                    "itemDesc": "Application Form",
                    "cscheckFlag": "true",
                    "rocheckFlag": "false",
                    "opscheckFlag": "false"
                },
                {
                    "itemId": "2",
                    "itemCde": "Fee schedule",
                    "itemDesc": "Fee schedule",
                    "cscheckFlag": "true",
                    "rocheckFlag": "false",
                    "opscheckFlag": "false"
                },
                {
                    "itemId": "3",
                    "itemCde": "ID card Copy",
                    "itemDesc": "ID card Copy",
                    "cscheckFlag": "true",
                    "rocheckFlag": "false",
                    "opscheckFlag": "false"
                },
                {
                    "itemId": "4",
                    "itemCde": "SFC search",
                    "itemDesc": "SFC search",
                    "cscheckFlag": "true",
                    "rocheckFlag": "false",
                    "opscheckFlag": "false"
                },
                {
                    "itemId": "5",
                    "itemCde": "Worldcheck",
                    "itemDesc": "Worldcheck",
                    "cscheckFlag": "false",
                    "rocheckFlag": "false",
                    "opscheckFlag": "false"
                },
                {
                    "itemId": "6",
                    "itemCde": "Address Proof (if any)",
                    "itemDesc": "Address Proof (if any)",
                    "cscheckFlag": "false",
                    "rocheckFlag": "false",
                    "opscheckFlag": "false"
                },
                {
                    "itemId": "7",
                    "itemCde": "Bank proof (if any)",
                    "itemDesc": "Bank proof (if any)",
                    "cscheckFlag": "false",
                    "rocheckFlag": "false",
                    "opscheckFlag": "false"
                },
                {
                    "itemId": "8",
                    "itemCde": "Source of Fund (if any)",
                    "itemDesc": "Source of Fund (if any)",
                    "cscheckFlag": "false",
                    "rocheckFlag": "false",
                    "opscheckFlag": "false"
                },
                {
                    "itemId": "9",
                    "itemCde": "Source of Wealth (if any)",
                    "itemDesc": "Source of Wealth (if any)",
                    "cscheckFlag": "false",
                    "rocheckFlag": "false",
                    "opscheckFlag": "false"
                },
                {
                    "itemId": "10",
                    "itemCde": "Other",
                    "itemDesc": "Other",
                    "cscheckFlag": "false",
                    "rocheckFlag": "false",
                    "opscheckFlag": "false"
                }
            ],
            "workFlowCode": "openClient",
            "controlCode": "PASS",
            "isStaff": "false",
            "lockBy": "ED_RO",
            "licensedPersonSign": ""
        }
        print("data=", data)
        operatingWorkFlowResp = s.post(url=operatingWorkFlowturl, headers=headers, json=data)
        logging.info(
            "步骤5提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(operatingWorkFlowturl, data, operatingWorkFlowResp.text))
        print("步骤5提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(operatingWorkFlowturl, data, operatingWorkFlowResp.text))
        return operatingWorkFlowResp

    # 步骤6
    def operatingWorkFlowNo不用锁定审核通过(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": cookfront + token
        }
        logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        operatingWorkFlowNourl = eddidhost + "/api/common/operatingWorkFlow"

        print("submitAuditurl为:", operatingWorkFlowNourl)
        logging.info("提交审核获取到的手机号为：{}".format(phone))
        # global applyId
        # applyId = cd_clnt_apply_info(phone)
        logging.info("当前applyId为：{}".format(applyId))
        data = {
            "applyId": applyId,
            "checkItemList": [
                {
                    "itemId": "1",
                    "itemCde": "Application Form",
                    "itemDesc": "Application Form",
                    "cscheckFlag": "true",
                    "rocheckFlag": "true",
                    "opscheckFlag": "false"
                },
                {
                    "itemId": "2",
                    "itemCde": "Fee schedule",
                    "itemDesc": "Fee schedule",
                    "cscheckFlag": "true",
                    "rocheckFlag": "true",
                    "opscheckFlag": "false"
                },
                {
                    "itemId": "3",
                    "itemCde": "ID card Copy",
                    "itemDesc": "ID card Copy",
                    "cscheckFlag": "true",
                    "rocheckFlag": "true",
                    "opscheckFlag": "false"
                },
                {
                    "itemId": "4",
                    "itemCde": "SFC search",
                    "itemDesc": "SFC search",
                    "cscheckFlag": "true",
                    "rocheckFlag": "true",
                    "opscheckFlag": "false"
                },
                {
                    "itemId": "5",
                    "itemCde": "Worldcheck",
                    "itemDesc": "Worldcheck",
                    "cscheckFlag": "false",
                    "rocheckFlag": "false",
                    "opscheckFlag": "false"
                },
                {
                    "itemId": "6",
                    "itemCde": "Address Proof (if any)",
                    "itemDesc": "Address Proof (if any)",
                    "cscheckFlag": "false",
                    "rocheckFlag": "false",
                    "opscheckFlag": "false"
                },
                {
                    "itemId": "7",
                    "itemCde": "Bank proof (if any)",
                    "itemDesc": "Bank proof (if any)",
                    "cscheckFlag": "false",
                    "rocheckFlag": "false",
                    "opscheckFlag": "false"
                },
                {
                    "itemId": "8",
                    "itemCde": "Source of Fund (if any)",
                    "itemDesc": "Source of Fund (if any)",
                    "cscheckFlag": "false",
                    "rocheckFlag": "false",
                    "opscheckFlag": "false"
                },
                {
                    "itemId": "9",
                    "itemCde": "Source of Wealth (if any)",
                    "itemDesc": "Source of Wealth (if any)",
                    "cscheckFlag": "false",
                    "rocheckFlag": "false",
                    "opscheckFlag": "false"
                },
                {
                    "itemId": "10",
                    "itemCde": "Other",
                    "itemDesc": "Other",
                    "cscheckFlag": "false",
                    "rocheckFlag": "false",
                    "opscheckFlag": "false"
                }
            ],
            "workFlowCode": "openClient",
            "controlCode": "PASS"
        }
        print("data=", data)
        operatingWorkFlowNoResp = s.post(url=operatingWorkFlowNourl, headers=headers, json=data)
        logging.info(
            "步骤6提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(operatingWorkFlowNourl, data, operatingWorkFlowNoResp.text))
        print("步骤6提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(operatingWorkFlowNourl, data, operatingWorkFlowNoResp.text))
        return operatingWorkFlowNoResp

    # 步骤7
    def operatingWorkFlowAgain提交锁(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": cookfront + token
        }
        # logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        operatingWorkFlowAgainturl = eddidhost + "/api/common/operatingWorkFlow"

        print("submitAuditurl为:", operatingWorkFlowAgainturl)
        logging.info("提交审核获取到的手机号为：{}".format(phone))
        # global applyId
        # applyId = cd_clnt_apply_info(phone)
        print("查询数据库cd_clnt_apply_info查询到applyId的值为：{}".format(applyId))
        data = {
            "applyId": applyId,
            "workFlowCode": "openClient",
            "controlCode": "LOCK"
        }
        print("data=", data)
        operatingWorkFlowAgaintResp = s.post(url=operatingWorkFlowAgainturl, headers=headers, json=data)
        logging.info(
            "提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(operatingWorkFlowAgainturl, data, operatingWorkFlowAgaintResp.text))
        print(
            "提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(operatingWorkFlowAgainturl, data, operatingWorkFlowAgaintResp.text))
        return operatingWorkFlowAgaintResp

    # 步骤8
    def batchOperatingWorkFlow批量生成账号确定(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": cookfront + token
        }
        print("当前token为:{}".format(token))
        print("headers", headers)
        batchOperatingWorkFlowurl = eddidhost + "/api/common/batchOperatingWorkFlow"

        print("submitAuditurl为:", batchOperatingWorkFlowurl)
        # global applyId
        # applyId = cd_clnt_apply_info(phone)
        print("查询数据库cd_clnt_apply_info查询到applyId的值为：{}".format(applyId))
        data = {
            "applyIds": [
                applyId
            ],
            "workFlowCode": "openClient",
            "controlCode": "GENERATEACCTNO",
            "workFlowOperatingDTOList": [
                {
                    "applyId": applyId
                }
            ]
        }
        print("data=", data)
        batchOperatingWorkFlowResp = s.post(url=batchOperatingWorkFlowurl, headers=headers, json=data)
        logging.info(
            "提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(batchOperatingWorkFlowurl, data, batchOperatingWorkFlowResp.text))
        print("提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(batchOperatingWorkFlowurl, data, batchOperatingWorkFlowResp.text))
        return batchOperatingWorkFlowResp

    # 步骤9
    def operatingWorkFlowThird提交锁(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": cookfront + token
        }
        # logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        operatingWorkFlowThirdurl = eddidhost + "/api/common/operatingWorkFlow"
        print("submitAuditurl为:", operatingWorkFlowThirdurl)
        logging.info("提交审核获取到的手机号为：{}".format(phone))
        print("提交审核获取到的手机号为：{}".format(phone))
        # global applyId
        # applyId = cd_clnt_apply_info(phone)
        logging.info("当前applyId为：{}".format(applyId))
        data = {
            "applyId": applyId,
            "workFlowCode": "openClient",
            "controlCode": "LOCK"
        }
        print("data=", data)
        operatingWorkFlowThirdResp = s.post(url=operatingWorkFlowThirdurl, headers=headers, json=data)
        logging.info(
            "提交审核接口'{}',请求参数为：{},的响应结果为:'{}'".format(operatingWorkFlowThirdurl, data, operatingWorkFlowThirdResp.text))
        print("步骤9提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(operatingWorkFlowThirdurl, data,
                                                         operatingWorkFlowThirdResp.text))
        return operatingWorkFlowThirdResp

    # 步骤10
    def batchOperatingWorkFlowEnd批量确认(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": cookfront + token
        }
        # logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        batchOperatingWorkFlowEndurl = eddidhost + "/api/common/batchOperatingWorkFlow"
        logging.info("提交审核获取到的手机号为：{}".format(phone))
        print("提交审核获取到的手机号为：{}".format(phone))
        # global applyId
        # applyId = cd_clnt_apply_info(phone)
        logging.info("当前applyId为：{}".format(applyId))
        data = {
            "applyIds": [
                applyId
            ],
            "workFlowCode": "openClient",
            "controlCode": "PASS",
            "workFlowOperatingDTOList": [
                {
                    "applyId": applyId
                }
            ]
        }
        print("data=", data)
        batchOperatingWorkFlowEndResp = s.post(url=batchOperatingWorkFlowEndurl, headers=headers, json=data)
        logging.info("提交审核接口'{}';请求参数为:{};的响应结果为:'{}'".format(batchOperatingWorkFlowEndurl, data,
                                                              batchOperatingWorkFlowEndResp.text))
        print("步骤10提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(batchOperatingWorkFlowEndurl, data,
                                                          batchOperatingWorkFlowEndResp.text))
        return batchOperatingWorkFlowEndResp

    def SQLCheckUser(self):
        time.sleep(10)
        # 通过直接调用cd_enty表查询
        CheckUsers = cd_enty(phone)
        print("通过phone='{}'查询cd_enty表的结果为{}".format(phone, CheckUsers))
        logging.info("通过'{}'查询cd_enty表的结果为{}".format(phone, CheckUsers))
        return CheckUsers


# ”if __name__=="__main__":“的作用在当前文件run时会执行下面的代码，如果时外部调用就不会执行if里面的代码
if __name__ == "__main__":
    # 以行数确定轮询次数
    a = 1
    CreatUser = CreatUser()
    # token = cdms_获取token()
    # # 将token写入文本
    # data_write('F:\\python\\EDDID_CDMS\\Data\\token.txt', token)
    for i in range(a):
        # 实例化CreatUser
        print("=====================================步骤1：", CreatUser.SaveApplyClient().text)
        time.sleep(2)
        # print("=====================================步骤1：", CreatUser.ApplyClinet资料提交().text)
        # time.sleep(30)
        # print("=====================================步骤2：", CreatUser.SubmitAudit提交审核().text)
        # time.sleep(40)
        # print("=====================================步骤3：", CreatUser.operatingWorkFlowFirst提交锁().text)
        # time.sleep(4)
        # print("=====================================步骤4：", CreatUser.saveRiskAssessment风控评估提交().text)
        # time.sleep(4)
        # print("=====================================步骤5：", CreatUser.operatingWorkFlow内部人员审核().text)
        # time.sleep(4)
        # print("=====================================步骤6：", CreatUser.operatingWorkFlowNo不用锁定审核通过().text)
        # time.sleep(4)
        # print("=====================================步骤7：", CreatUser.operatingWorkFlowAgain提交锁().text)
        # time.sleep(4)
        # print("=====================================步骤8：", CreatUser.batchOperatingWorkFlow批量生成账号确定().text)
        # time.sleep(4)
        # print("=====================================步骤9：", CreatUser.operatingWorkFlowThird提交锁().text)
        # time.sleep(4)
        # print("=====================================步骤10：", CreatUser.batchOperatingWorkFlowEnd批量确认().text)
        # time.sleep(4)
        # print("=====================================步骤11：", CreatUser.SQLCheckUser())
        # time.sleep(4)
