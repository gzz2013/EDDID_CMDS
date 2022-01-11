# -*- coding:utf-8 -*-
import requests
from Common.random_number import *
from Config.cdms_config import *
from Business.login import cdms_获取token
import logging
from Common.com_sql.eddid_data_select import cd_enty,cd_clnt_apply_info,cd_clnt_info_update_apply
from Common.data_文本读写 import *


class updateClientInfo():

    def updateClientInfo(self):

        global token,headers,clientId,accountId,L,s,phone
        updateL=[]
        token = cdms_获取token()
        s = requests.Session()

        cookfront=cookfr
        #三个实参都为用户的真实数据，由于修改时提交的数据量大，不建议用随机的新账号实现该场景；
        clientId=12213
        accountId=122131110
        phone=16666085657
        id = cd_enty(phone)[0][0]
        Randomsemail=Randoms.RandomEmail()
        idCardNo = Randoms().ident_generator()
        applyId_update = cd_clnt_apply_info(phone)[0][0]
        updateL.append(Randomsemail)
        updateL.append(idCardNo)
        data_write('F:\\python\\EDDID_CDMS\\Data\\updateClient.txt', updateL)
        print("记录数据的文件名为：swapequity.txt，写入数据为:{}".format(updateL))
        logging.info("记录数据的文件名为：swapequity.txt，写入数据为:{}".format(updateL))
        headers={
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Connection": "keep-alive",
            "Cookie": cookfront + token
        }
        updateurl= url+"/api/client/updateClientInfo"
        data={
            "infos":[
                {
                    "id":id,
                    "applyNo":"",
                    "title":"mrs",
                    "informationType":"1",
                    "relationshipType":"",
                    "relationshipRemark":"",
                    "firstName":"MillC",
                    "lastName":"Tyrone",
                    "newFirstName":"",
                    "newLastName":"",
                    "chName":"曹一手x",
                    "usedChName":"曹一手x接口自动化创建账号",
                    "usedCnName":"Tyrone16666085657",
                    "email":Randomsemail,
                    "emailBak":"",
                    "phoneAreaCode":"CHN",
                    "phoneAreaCodeBak":"",
                    "phoneNo":phone,
                    "phoneNoBak":"",
                    "houseAddress":"中英街16666085657号",
                    "houseAddressPinYin":"zhon16666085657hao",
                    "postAddress":"接口自动化",
                    "natnlty":"TWN",
                    "idCardType":"1",
                    "idCardNo":idCardNo,
                    "idExpiresDate":"2025-09-30",
                    "otherCardType":"",
                    "otherCardNo":"",
                    "countryIssue":"CHN",
                    "birthday":"1993-11-01",
                    "overCountry":"CHN",
                    "birthdayPlace":"CHN",
                    "employmentStatus":"employed",
                    "employmentRemark":"",
                    "registeredCompany":"",
                    "post":"director&president",
                    "workingYear":"11",
                    "companyName":"大苏打",
                    "businessNature":"wholesale&retail",
                    "businessNatureRemark":"",
                    "officeAddress":"大苏打大苏打",
                    "officeCountry":"",
                    "officePhone":"0258545478",
                    "totalIncomeYear":"gt1000000",
                    "sourceOfIncome":[
                        "selfOperatedBusinessIncome"
                    ],
                    "sourceOfIncomeRemake":"",
                    "totalCapital":"gt8000000",
                    "sourceOfCapital":[
                        "vehicleInvestment",
                        "salary"
                    ],
                    "sourceOfCapitalRemark":"",
                    "sourceOfMoney":[
                        "savings"
                    ],
                    "sourceOfMoneyRemark":"",
                    "securitiesExperience":"gt10Years",
                    "cbbcExperience":"gt10Years",
                    "warrantExperience":"gt10Years",
                    "futuresExperience":"gt10Years",
                    "optionsExperience":"gt10Years",
                    "foreignExchangExperience":"gt10Years",
                    "metalExperience":"gt10Years",
                    "autoTransationExperience":"gt10Years",
                    "otherInvest":"",
                    "otherExperience":"",
                    "withDerivativesKnowledge":"Y",
                    "withDerivativesWoking":"Y",
                    "withDerivativesDeal":"N",
                    "applicationOpenDerivatives":"Y",
                    "understandTheRisks":"Y",
                    "haveDeclaredBankruptcy":"N",
                    "declaredBankruptcyDate":"",
                    "isInternalStaff":"N",
                    "staffNameRelationship":"",
                    "relationshipWithInternalEmployees":"N",
                    "employeesName":"",
                    "isRegisteredPerson":"N",
                    "registeredPersonRemark":"",
                    "isUsPerson":"N",
                    "taxNumber":"",
                    "isUsTaxPerson":"N",
                    "taxNumberTwo":"",
                    "isPepPerson":"N",
                    "pepPersonName":"",
                    "confirmAcctRisk":"",
                    "investmentObjective":[
                        "speculation"
                    ],
                    "riskTolerance":"high",
                    "throughChannels":[
                        "advertising",
                        "lecture"
                    ],
                    "throughChannelRemark":"",
                    "isFinalBeneficiary":"Y",
                    "finalBeneficiaryName":"",
                    "isFinalPrincipal":"Y",
                    "finalPrincipalName":"",
                    "businessAddress":"大苏打大苏打",
                    "isStaff":"false",
                    "address":""
                }
            ],
            "marginAcctS":[

            ],
            "taxs":[

            ],
            "settleAcctS":[

            ],
            "attachs":{
                "acquaintHighLevelInstructionsProve":[

                ],
                "acquaintHighLevelInstructionsProveDel":[

                ],
                "addressVerificationMaterials":[
                    "/dinggg_20210908162349.jpg"
                ],
                "addressVerificationMaterialsDel":[

                ],
                "bankCardMaterials":[
                    "/hzlc_20210908162353.jpg"
                ],
                "bankCardMaterialsDel":[

                ],
                "bankruptcyProve":[

                ],
                "bankruptcyProveDel":[

                ],
                "disclaimerVideo":[

                ],
                "disclaimerVideoDel":[

                ],
                "joinAcquaintHighLevelInstructionsProve":[

                ],
                "joinAcquaintHighLevelInstructionsProveDel":[

                ],
                "joinBankruptcyProve":[

                ],
                "joinBankruptcyProveDel":[

                ],
                "otherInformation":[
                    "/hzlc_20210908162407.jpg"
                ],
                "otherInformationDel":[

                ],
                "passportMaterial":[
                    "/dinggg_20210908162346.jpg"
                ],
                "passportMaterialDel":[

                ],
                "proofOfIncome":[
                    "/dinggg_20210908162404.jpg"
                ],
                "proofOfIncomeDel":[

                ],
                "writtenApplicationMaterials":[
                    "/APP_20200811142432_20210908162403.pdf"
                ],
                "writtenApplicationMaterialsDel":[

                ],
                "signatureMaterial":[

                ],
                "signatureMaterialDel":[

                ],
                "tradingAuthorization":[

                ],
                "tradingAuthorizationDel":[

                ],
                "innerRemarkAttachs":[

                ],
                "riskAssessment":[

                ],
                "eddaCertificates":[

                ],
                "flag":""
            },
            "applyId":applyId_update,
            "clientType":"PERSONAL",
            "openWay":"visitingAccount",
            "bankName":"",
            "bankCardNo":"",
            "elecNo":"",
            "responsible":"ryan.chan",
            "emailLanguage":"zh-hant",
            "caServiceName":"",
            "accts":[
                "securitiesCash"
            ],
            "clientId":clientId,
            "couponCode":"EDAA520",
            "securitiesCashAcct":accountId,
            "securitiesMarginAcct":"",
            "securitiesAyersCashAcct":"",
            "futuresMarginAcct":"",
            "futuresDayTradeMarginAcct":"",
            "eddidProNumber":"",
            "leveragedForeignExchangeAccountMarginAcct":"",
            "applicationOpenDerivatives":"Y",
            "riskTolerance":"high",
            "agreeGreyMarketTrading":"",
            "agreeToTheTerms":"true",
            "personalInfoDeclartion":"true",
            "isStaff":"false"
        }
        updateRespo=s.post(url=updateurl,headers=headers,json=data)
        logging.info("步骤1,资料修改提交，接口：'{}';请求参数为:{};响应结果为：'{}'".format(updateurl, data, updateRespo.text))
        print("步骤1,资料修改提交，接口：'{}';请求参数为:{};响应结果为：'{}'".format(updateurl, data, updateRespo.text))
        return updateRespo

    def operatingWorkFlowonce(self):
        global applyId
        applyId = cd_clnt_info_update_apply(clientId)[0][0]
        logging.info("通过查询数据库查询到applyid为：'{}'".format(applyId))
        print("通过查询数据库查询到applyid为：'{}'".format(applyId))
        data = {
            "applyId": applyId,
            "workFlowCode": "clientInfoUpdateApply",
            "controlCode": "LOCK"
        }
        operatingWorkFlowonceurl = url + "/api/common/operatingWorkFlow"
        operatingWorkFlowonceRespo = s.post(url=operatingWorkFlowonceurl, headers=headers, json=data)
        logging.info("步骤2,第一次提交锁，接口：'{}';请求参数为:{};响应结果为：'{}'".format(operatingWorkFlowonceurl, data,
                                                                     operatingWorkFlowonceRespo.text))
        print("步骤2,第一次提交锁，接口：'{}';请求参数为:{};响应结果为：'{}'".format(operatingWorkFlowonceurl, data,
                                                              operatingWorkFlowonceRespo.text))
        return operatingWorkFlowonceRespo

    def operatingWorkFlowCS2(self):

        data = {
            "applyId":applyId,
            "controlCode":"PASS",
            "workFlowCode":"clientInfoUpdateApply",
            "lockBy":"cliff_RO"
        }
        operatingWorkFlowCS2url = url + "/api/common/operatingWorkFlow"
        operatingWorkFlowCS2Respo = s.post(url=operatingWorkFlowCS2url, headers=headers, json=data)
        logging.info("步骤3,CS2审批通过，接口：'{}';请求参数为:{};响应结果为：'{}'".format(operatingWorkFlowCS2url, data,
                                                                     operatingWorkFlowCS2Respo.text))
        print("步骤3,CS2审批通过，接口：'{}';请求参数为:{};响应结果为：'{}'".format(operatingWorkFlowCS2url, data,
                                                              operatingWorkFlowCS2Respo.text))
        return operatingWorkFlowCS2Respo


    def operatingWorkFlowOR(self):
        time.sleep(3)
        data = {
            "applyId":applyId,
            "controlCode":"PASS",
            "workFlowCode":"clientInfoUpdateApply"
        }
        operatingWorkFlowORurl = url + "/api/common/operatingWorkFlow"
        operatingWorkFlowORRespo = s.post(url=operatingWorkFlowORurl, headers=headers, json=data)
        logging.info("步骤4,OR审批通过，接口：'{}';请求参数为:{};响应结果为：'{}'".format(operatingWorkFlowORurl, data,
                                                                     operatingWorkFlowORRespo.text))
        print("步骤4,OR审批通过，接口：'{}';请求参数为:{};响应结果为：'{}'".format(operatingWorkFlowORurl, data,
                                                              operatingWorkFlowORRespo.text))
        return operatingWorkFlowORRespo

    def operatingWorkFlowtwo(self):
        data = {
            "applyId": applyId,
            "workFlowCode": "clientInfoUpdateApply",
            "controlCode": "LOCK"
        }
        operatingWorkFlowtwourl = url + "/api/common/operatingWorkFlow"
        operatingWorkFlowtwoRespo = s.post(url=operatingWorkFlowtwourl, headers=headers, json=data)
        logging.info("步骤5,第二次提交锁，接口：'{}';请求参数为:{};响应结果为：'{}'".format(operatingWorkFlowtwourl, data,
                                                                     operatingWorkFlowtwoRespo.text))
        print("步骤5,第二次提交锁，接口：'{}';请求参数为:{};响应结果为：'{}'".format(operatingWorkFlowtwourl, data,
                                                              operatingWorkFlowtwoRespo.text))
        return operatingWorkFlowtwoRespo

    def operatingWorkFlowCLER(self):
        data = {
            "applyId":applyId,
            "controlCode":"PASS",
            "workFlowCode":"clientInfoUpdateApply"
        }
        operatingWorkFlowCLERurl = url + "/api/common/operatingWorkFlow"
        operatingWorkFlowCLERRespo = s.post(url=operatingWorkFlowCLERurl, headers=headers, json=data)
        logging.info("步骤6,CLER审批通过，接口：'{}';请求参数为:{};响应结果为：'{}'".format(operatingWorkFlowCLERurl, data,
                                                                     operatingWorkFlowCLERRespo.text))
        print("步骤6,CLER审批通过，接口：'{}';请求参数为:{};响应结果为：'{}'".format(operatingWorkFlowCLERurl, data,
                                                              operatingWorkFlowCLERRespo.text))
        return operatingWorkFlowCLERRespo

    def sql_cd_enty(self):
        cd_entyinfor=cd_enty(phone)
        logging.info("步骤7,通过phone:{}查询数据库cd_enty，查询结果为：'{}'".format(phone,cd_entyinfor))
        print("步骤7,通过phone:{}查询数据库cd_enty，查询结果为：'{}'".format(phone,cd_entyinfor))
        return cd_entyinfor


if __name__=="__main__":
    updateClient=updateClientInfo()
    a=1
    for i in range(a):
        print("=====================================步骤1：", updateClient.updateClientInfo().text)
        time.sleep(10)
        print("=====================================步骤2：", updateClient.operatingWorkFlowonce().text)
        time.sleep(5)
        print("=====================================步骤3：", updateClient.operatingWorkFlowCS2().text)
        time.sleep(5)
        print("=====================================步骤4：", updateClient.operatingWorkFlowOR().text)
        time.sleep(5)
        print("=====================================步骤5：", updateClient.operatingWorkFlowtwo().text)
        time.sleep(5)
        print("=====================================步骤6：", updateClient.operatingWorkFlowCLER().text)
        time.sleep(5)
        print("=====================================步骤7：", updateClient.sql_cd_enty())
        time.sleep(5)