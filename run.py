#2021年12月30日13:56:22
import unittest

import HTMLReport
from Business.login import cdms_获取token
from Common.data_文本读写 import *
# import datetime
from Config.cdms_config import *
from Test_Suite.suite_cmds_Summary import *

suite = unittest.TestSuite()
#收集用例之前先把token写到对应文件
# token = cdms_获取token()
# data_write('F:\\python\\EDDID_CDMS\\Data\\token.txt', token)
#
suite.addTests(get_suite_creatUser新建用户())
suite.addTests(get_suite_CreateExchange新建换汇申请单())
suite.addTests(get_suite_creatUser没有结构性产品账号及申请结构性产品审批())
suite.addTests(get_suite_CreatEquitiesDeposit入金())
suite.addTests(get_suite_CreatEquitiesDeposit大额入金())
suite.addTests(get_suite_creatUser新建所有类型用户())
suite.addTests(get_suite_creatUser新建用户后停用())
suite.addTests(get_suite_enableAcct停用后开启())
suite.addTests(get_suite_closeAcct账号关闭())
suite.addTests(get_suite_CreatUser创建其他类型交易账号())
suite.addTests(get_suite_CreateClientBank添加银行卡())
suite.addTests(get_suite_Creat_mrktdat_sub())
suite.addTests(get_suite_Creat_deposit_sub())
suite.addTests(get_suite_UpdateClientInfo修改用户资料及审批())
suite.addTests(get_suite_Subaccount银行子账号申请及审核())
suite.addTests(get_suite_Creat_H5_eDDAcontract())
suite.addTests(get_suite_Creat_H5_EDDAdeposit入金())

#####出金流程已变动
# suite.addTests(get_suite_CreatEquitiesWithdrawal出金())
##调用第三方接口'获取股票信息异常'
# suite.addTests(get_suite_SwapEquity转股())
#####出金流程调试中
# suite.addTests(get_suite_CreatEquitiesWithdrawalnew出金())



if __name__ == '__main__':
    # title_time = titletimes
    # title_time=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    HTMLReport.TestRunner(
        title="EDDID_CDMS项目接口测试"+str(local_times),
        description="如有疑问请联系-ganjiexiang",
        report_file_name="EDDID_CDMS项目接口测试",
        # report_file_name字段不能改，关系到Jenkins的配置报告的生成
        thread_count=1
    ).run(suite)

