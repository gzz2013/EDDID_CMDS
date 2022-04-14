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


# Randoms=Randoms()
class CreatUser无结构性产品用户创建():
    # 步骤1
    def ApplyClinet资料提交(self):
        global phone, token, eddidhost, s, cremail, rfirstName, rlastName, rchName, idCardNo

        # 生成电话号
        phone = Randoms().telephone()

        # 生成新邮箱
        cremail = Randoms.RandomEmail()

        # 英文名firstName
        rfirstName = Randoms().creat_EFName()

        # 英文名lastName
        rlastName = Randoms().creat_ELName()

        # 中文名chName
        rchName = Randoms().creat_CHName()

        # 生成身份证号
        idCardNo = Randoms().ident_generator()

        # 生成称谓（性别）
        ctitle = Randoms().choice_title()
        # 新列表用来存放用户基本信息
        userinformationList = []
        userinformationList.append(phone)
        userinformationList.append(cremail)
        userinformationList.append(rfirstName)
        userinformationList.append(rlastName)
        userinformationList.append(rchName)
        userinformationList.append(idCardNo)
        userinformationList.append(ctitle)
        print("userdatainf_1.txt:", userinformationList)

        # 将userinformationList写入文本
        data_write('F:\\python\\EDDID_CDMS\\Data\\userdatainf_1.txt', userinformationList)
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
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
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
                    "usedCnName": rlastName + phone,
                    "usedChName": rchName + "接口自动化创建账号",
                    "email": cremail,
                    "phoneAreaCode": "CHN",
                    "phoneNo": phone,
                    "houseAddress": "中英街" + phone + "号",
                    "houseAddressPinYin": "zhon" + phone + "hao",
                    "postAddress": "接口自动化",
                    "natnlty": "TWN",
                    "idCardType": "1",
                    "idCardNo": idCardNo,
                    "otherCardType": "",
                    "otherCardNo": "",
                    "countryIssue": "CHN",
                    "overCountry": "CHN",
                    "birthday": "1993-11-01",
                    "idExpiresDate": "2025-09-30",
                    "birthdayPlace": "CHN",
                    "employmentStatus": "employed",
                    "post": "director&president",
                    "workingYear": "11",
                    "companyName": "大苏打",
                    "businessNature": "wholesale&retail",
                    "officeAddress": "大苏打大苏打",
                    "officePhone": "0258545478",
                    "registeredCompany": "",
                    "employmentRemark": "",
                    "totalIncomeYear": "gt1000000",
                    "sourceOfIncome": [
                        "selfOperatedBusinessIncome"
                    ],
                    "sourceOfIncomeRemake": "",
                    "totalCapital": "gt8000000",
                    "sourceOfCapital": [
                        "vehicleInvestment",
                        "salary"
                    ],
                    "sourceOfCapitalRemark": "",
                    "sourceOfMoney": [
                        "savings"
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
                    "withDerivativesDeal": "N",
                    "applicationOpenDerivatives": "N",
                    "understandTheRisks": "",
                    "haveDeclaredBankruptcy": "N",
                    "declaredBankruptcyDate": "",
                    "isInternalStaff": "N",
                    "staffNameRelationship": "",
                    "relationshipWithInternalEmployees": "N",
                    "employeesName": "",
                    "isRegisteredPerson": "N",
                    "registeredPersonRemark": "",
                    "isUsPerson": "N",
                    "taxNumber": "",
                    "isUsTaxPerson": "N",
                    "taxNumberTwo": "",
                    "isPepPerson": "N",
                    "pepPersonName": "",
                    "investmentObjective": [
                        "speculation"
                    ],
                    "riskTolerance": "high",
                    "throughChannels": [
                        "advertising",
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

            ],
            "attachs": {
                "passportMaterial": [
                    "/dinggg_20210908162346.jpg"
                ],
                "addressVerificationMaterials": [
                    "/dinggg_20210908162349.jpg"
                ],
                "bankCardMaterials": [
                    "/hzlc_20210908162353.jpg"
                ],
                "writtenApplicationMaterials": [
                    "/APP_20200811142432_20210908162403.pdf"
                ],
                "proofOfIncome": [
                    "/dinggg_20210908162404.jpg"
                ],
                "otherInformation": [
                    "/hzlc_20210908162407.jpg"
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
            "responsible": "ryan.chan",
            "emailLanguage": "zh-hans",
            # 简体
            # "emailLanguage": "zh-hant",
            # 繁体
            "accts": [
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
            "promotionNumber": "EDAA520",
            "agreeToTheTerms": "true",
            "personalInfoDeclartion": "true"
        }

        applyClientResp = s.post(url=applyClienturl, headers=headers, json=data)
        logging.info("步骤1接口'{}';请求参数为:{};响应结果为：'{}'".format(applyClienturl, data, applyClientResp.text))
        print("步骤1接口'{}';请求参数为:{};响应结果为：'{}'".format(applyClienturl, data, applyClientResp.text))
        return applyClientResp

    # 步骤2
    def SubmitAudit提交审核(self):
        print("等待系统录入数据后再修改WorldCheck的状态，等待时间20s")
        logging.info("等待系统录入数据后再修改WorldCheck的状态，等待时间20s")
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
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
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
        time.sleep(30)
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("当前token为:{}".format(token))

        print("当前token为:{}".format(token))
        print("headers", headers)
        operatingWorkFlowFirsturl = eddidhost + "/api/common/operatingWorkFlow"

        print("submitAuditurl为:", operatingWorkFlowFirsturl)

        logging.info("提交审核获取到的手机号为：{}".format(phone))
        # global applyId
        # applyId = cd_clnt_apply_info(phone)
        print("提交审核获取到的手机号为：{}".format(phone))
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
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
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
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
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
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        operatingWorkFlowNourl = eddidhost + "/api/common/operatingWorkFlow"

        print("submitAuditurl为:", operatingWorkFlowNourl)
        logging.info("提交审核获取到的手机号为：{}".format(phone))
        print("提交审核获取到的手机号为：{}".format(phone))
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
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        # logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        operatingWorkFlowAgainturl = eddidhost + "/api/common/operatingWorkFlow"

        print("submitAuditurl为:", operatingWorkFlowAgainturl)
        logging.info("提交审核获取到的手机号为：{}".format(phone))
        print("提交审核获取到的手机号为：{}".format(phone))
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
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
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
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        # logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        operatingWorkFlowThirdurl = eddidhost + "/api/common/operatingWorkFlow"
        print("submitAuditurl为:", operatingWorkFlowThirdurl)
        logging.info("提交审核获取到的手机号为：{}".format(phone))
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
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
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

    # 步骤11
    def SQLCheckUser(self):
        time.sleep(10)
        # 通过直接调用cd_enty表查询
        CheckUsers = cd_enty(phone)
        print("通过phone='{}'查询cd_enty表的结果为{}".format(phone, CheckUsers))
        logging.info("通过'{}'查询cd_enty表的结果为{}".format(phone, CheckUsers))
        return CheckUsers

    # 步骤12
    def addAccountStructure增加结构性产品(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        # logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        addAccountStructureurl = eddidhost + "/api/cdms/struc/addAccountStructure"
        logging.info("提交审核获取到的手机号为：{}".format(phone))
        print("提交审核获取到的手机号为：{}".format(phone))
        # global applyId
        # clnt_id = cd_clnt_apply_info(phone)[0][0]
        global clnt_id, accountId, eddidId

        clnt_id = cd_clnt_joint_enty(cd_enty(phone)[0][0])[0][1]

        accountId = cd_ac(clnt_id)[0][0]

        eddidId = cd_clnt(clnt_id)[0][3]

        logging.info("获取到结构性产品的客户编号clnt_id为：{}，交易账户accountId为：{}，eddidId为：{}".format(clnt_id, accountId, eddidId))
        print("获取到结构性产品的客户编号clnt_id为：{}，交易账户accountId为：{}，eddidId为：{}".format(clnt_id, accountId, eddidId))

        data = {
            "accountId": accountId,
            "firstName": None,
            "lastName": None,
            "chineseName": rchName,
            "eddidId": eddidId,
            "accountCash": accountId,
            "accountMargin": None,
            "idUrlList": [
                "/dinggg_20210908162346.jpg"
            ],
            "isOpenFuturesAcc": "false",
            "cbbcExperience": "gt10Years",
            "warrantExperience": "gt10Years",
            "futuresExperience": "gt10Years",
            "optionsExperience": "gt10Years",
            "securitiesExperience": "gt10Years",
            "otherInvest": "",
            "otherExperience": "",
            "isDerivativesKnowledge": "Y",
            "isDerivativesWork": "Y",
            "isDerivativesDeal": "N",
            "exchInvestTargetList": [
                "speculation"
            ],
            "exchRiskAppetite": "high",
            "clientId": clnt_id,
            "isStruc": "Y",
            "isOpenClnt": "Y",
            "applySource": "4"
        }

        print("data=", data)
        addAccountStructureResp = s.post(url=addAccountStructureurl, headers=headers, json=data)
        logging.info("提交审核接口'{}';请求参数为:{};的响应结果为:'{}'".format(addAccountStructureurl, data,
                                                              addAccountStructureResp.text))
        print("步骤11提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(addAccountStructureurl, data,
                                                          addAccountStructureResp.text))
        return addAccountStructureResp

    # 步骤13
    def addAccountStructure第一次审批(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }
        # logging.info("当前token为:{}".format(token))
        print("当前token为:{}".format(token))
        print("headers", headers)
        auditAccountStructureurl = eddidhost + "/api/cdms/struc/auditAccountStructure"
        logging.info("提交审核获取到的手机号为：{}".format(phone))
        print("提交审核获取到的手机号为：{}".format(phone))
        global Structureapplyid

        Structureapplyid = cd_ac_struc_appl(clnt_id)[0][0]

        logging.info("获取到结构性产品的申请单编号为：{}".format(Structureapplyid))
        print("获取到结构性产品的申请单编号为：{}".format(Structureapplyid))

        data = {
            "id": Structureapplyid,
            "approvalResult": "PASS",
            "attachUrlList": [
            ]
        }
        print("data=", data)
        addAccountStructureResp = s.post(url=auditAccountStructureurl, headers=headers, json=data)
        logging.info("提交审核接口'{}';请求参数为:{};的响应结果为:'{}'".format(auditAccountStructureurl, data,
                                                              addAccountStructureResp.text))
        print("步骤11提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(auditAccountStructureurl, data,
                                                          addAccountStructureResp.text))
        return addAccountStructureResp

    # 步骤14
    def addAccountStructure第二次审批(self):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": "LANGUAGE=zh_CN;GB-SYS-SID-SIT=" + token
        }

        print("当前token为:{}".format(token))
        print("headers", headers)
        auditAccountStructureurl = eddidhost + "/api/cdms/struc/auditAccountStructure"
        logging.info("提交审核获取到的手机号为：{}".format(phone))
        print("提交审核获取到的手机号为：{}".format(phone))
        Structureapplyid = cd_ac_struc_appl(clnt_id)[0][0]

        logging.info("获取到结构性产品的申请单编号为：{}".format(Structureapplyid))
        print("获取到结构性产品的申请单编号为：{}".format(Structureapplyid))
        data = {
            "id": Structureapplyid,
            "approvalResult": "PASS",
            "attachUrlList": [

            ]
        }
        print("data=", data)
        addAccountStructuresResp = s.post(url=auditAccountStructureurl, headers=headers, json=data)
        logging.info("提交审核接口'{}';请求参数为:{};的响应结果为:'{}'".format(auditAccountStructureurl, data,
                                                              addAccountStructuresResp.text))
        print("步骤11提交审核接口'{}';请求参数为:{};响应结果为:'{}'".format(auditAccountStructureurl, data,
                                                          addAccountStructuresResp.text))
        return addAccountStructuresResp

    # 步骤15
    def SQLCheckcd_ac_struc_appl(self):
        time.sleep(8)
        # 通过直接调用cd_enty表查询
        Checkcd_ac_struc_appl = cd_ac_struc_appl(clnt_id)
        print("Structureapplyid='{}'查询cd_ac_struc_appl表的结果为{}".format(clnt_id, Checkcd_ac_struc_appl))
        logging.info("通过'{}'查询cd_ac_struc_appl表的结果为{}".format(clnt_id, Checkcd_ac_struc_appl))
        return Checkcd_ac_struc_appl


# ”if __name__=="__main__":“的作用在当前文件run时会执行下面的代码，如果时外部调用就不会执行if里面的代码
if __name__ == "__main__":
    a = 1
    CreatUser = CreatUser无结构性产品用户创建()
    for i in range(a):
        # 实例化CreatUser
        print("=====================================步骤1：", CreatUser.ApplyClinet资料提交().text)
        time.sleep(10)
        print("=====================================步骤2：", CreatUser.SubmitAudit提交审核().text)
        time.sleep(10)
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
        time.sleep(10)
        print("=====================================步骤11：", CreatUser.addAccountStructure增加结构性产品().text)
        # time.sleep(4)
        # print("=====================================步骤12：", CreatUser.addAccountStructure第一次审批().text)
        # time.sleep(4)
        # print("=====================================步骤13：", CreatUser.addAccountStructure第二次审批().text)

        # time.sleep(4)
        # print("步骤11：", CreatUser.SQLCheckUser())
        # time.sleep(4)

# if __name__=="__main__":
#     CreatUser = CreatUser()
#     # 实例化CreatUser
#     print("步骤1：", CreatUser.ApplyClinet资料提交().text)
#     time.sleep(4)
#     print("步骤2：", CreatUser.SubmitAudit提交审核().text)
#     time.sleep(4)
#     print("步骤3：", CreatUser.operatingWorkFlowFirst提交锁().text)
#     time.sleep(4)
#     print("步骤4：", CreatUser.saveRiskAssessment风控评估提交().text)
#     time.sleep(4)
#     print("步骤5：", CreatUser.operatingWorkFlow内部人员审核().text)
#     time.sleep(4)
#     print("步骤6：", CreatUser.operatingWorkFlowNo不用锁定审核通过().text)
#     time.sleep(4)
#     print("步骤7：", CreatUser.operatingWorkFlowAgain提交锁().text)
#     time.sleep(4)
#     print("步骤8：", CreatUser.batchOperatingWorkFlow批量生成账号确定().text)
#     time.sleep(4)
#     print("步骤9：", CreatUser.operatingWorkFlowThird提交锁().text)
#     time.sleep(4)
#     print("步骤10：", CreatUser.batchOperatingWorkFlowEnd批量确认().text)
#     time.sleep(4)
