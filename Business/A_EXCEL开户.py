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
import xlrd

class CreatUser():
    # 步骤1
    def ApplyClinet资料提交(self,i):
        global phone, token, eddidhost, s, cremail, rfirstName, rlastName, rchName, idCardNo, cookfront,sheet

        sheet=xlrd.open_workbook("C:\\Users\\Administrator\\Desktop\\userinformation.xls").sheets()[0]
        #电话
        # print("第一行第二列：%s" % sheet.cell_value(1, 0))
        print("phone：%s" % sheet.cell_value(1, 1))
        print("email：%s" % sheet.cell_value(1, 2))
        print("idCardNo：%s" % sheet.cell_value(1, 3))
        print("ch_name：%s" % sheet.cell_value(1, 4))
        print("frist_name：%s" % sheet.cell_value(1, 5))
        print("last_name：%s" % sheet.cell_value(1, 6))
        print("title：%s" % sheet.cell_value(1, 7))
        print("id_typ：%s" % sheet.cell_value(1, 8))
        print("cntry_issu：%s" % sheet.cell_value(1, 9))

        # 获取电话号,如果获取到表格数据为空，就去随机生成的值
        if sheet.cell_value(i, 1)!='':
            # phone = "18123697991"
            phone=sheet.cell_value(i, 1)
        else:
            phone=Randoms().telephone()

        # 获取邮箱
        if sheet.cell_value(i, 2)!='':
            #cremail="ganjiexiang6@126.com"
            cremail=sheet.cell_value(i, 2)
        else:
            cremail=Randoms.RandomEmail()

        # 获取身份证号
        if sheet.cell_value(i, 3)!='':
            #idCardNo="D9625128"
            idCardNo=sheet.cell_value(i, 3)
        else:
            idCardNo = Randoms().ident_generator()

        # 获取中文名
        if sheet.cell_value(i, 4)!='':
            #rchName="黄大蛋"
            rchName=sheet.cell_value(i, 4)
        else:
            rchName = Randoms().creat_CHName()

        # 英文名firstName
        if sheet.cell_value(i, 5)!='':
            #rfirstName="Nsad"
            rfirstName=sheet.cell_value(i, 5)
        else:
            rfirstName = Randoms().creat_EFName()


        # 英文名lastName
        if sheet.cell_value(i, 6)!='':
            #lastName="Nsad"
            rlastName=sheet.cell_value(i, 6)
        else:
            rlastName = Randoms().creat_ELName()

        # 国籍
        if sheet.cell_value(i, 9)!='':
            # cantrCode = "CHN"
            # cantrCode = "HKG"
            # cantrCode ="MYS"
            cantrCode=sheet.cell_value(i, 9)
        else:
            cantrCode = "CHN"

        #身份证类型 香港为"1" 大陆为"2"
        if sheet.cell_value(i, 8)!='':
            # idCardT = "1"
            # idCardT = "2"
            idCardT=sheet.cell_value(i, 8)
        else:
            idCardT = "2"

        # cookies的前缀
        cookfront = cookfr

        #"miss", "mr", "mrs"
        if sheet.cell_value(i, 7)!='':
            # ctitle = "miss"
            ctitle=sheet.cell_value(i, 7)
        else:
            ctitle = "mr"

        #选择简体繁体zh-hans简体；zh-hant繁体
        if sheet.cell_value(i,10)!='':
            # Language="zh-hans"
            Language=sheet.cell_value(i, 10)
        else:
            Language = Randoms().choice_Language()

        # 获取随机的账户类型
        caccts=Randoms().choice_accts()
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
            "emailLanguage": Language,
            # "emailLanguage": "zh-hans",
            # 简体
            # "emailLanguage": Language,
            # 繁体
            "accts": [
                # caccts
                "securitiesCash",
                # 证券现金
                # "securitiesMargin",
                # 证券保证金
                # "futuresMargin",
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
    sheet=xlrd.open_workbook("C:\\Users\\Administrator\\Desktop\\userinformation.xls").sheets()[0]
    rows=sheet.nrows
    print(rows)
    # a = 1
    CreatUser = CreatUser()
    # token = cdms_获取token()
    # # 将token写入文本
    # data_write('F:\\python\\EDDID_CDMS\\Data\\token.txt', token)
    for i in range(1,rows):
        # 实例化CreatUser
        print("=====================================步骤1：", CreatUser.ApplyClinet资料提交(i).text)
        time.sleep(30)
        print("=====================================步骤2：", CreatUser.SubmitAudit提交审核().text)
        time.sleep(40)
        print("=====================================步骤3：", CreatUser.operatingWorkFlowFirst提交锁().text)
        time.sleep(4)
        print("=====================================步骤4：", CreatUser.saveRiskAssessment风控评估提交().text)
        time.sleep(4)
        print("=====================================步骤5：", CreatUser.operatingWorkFlow内部人员审核().text)
        time.sleep(4)
        print("=====================================步骤6：", CreatUser.operatingWorkFlowNo不用锁定审核通过().text)
        time.sleep(4)
        print("=====================================步骤7：", CreatUser.operatingWorkFlowAgain提交锁().text)
        time.sleep(4)
        print("=====================================步骤8：", CreatUser.batchOperatingWorkFlow批量生成账号确定().text)
        time.sleep(4)
        print("=====================================步骤9：", CreatUser.operatingWorkFlowThird提交锁().text)
        time.sleep(4)
        print("=====================================步骤10：", CreatUser.batchOperatingWorkFlowEnd批量确认().text)
        time.sleep(4)
        print("=====================================步骤11：", CreatUser.SQLCheckUser())
        time.sleep(4)
