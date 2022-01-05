#2021年12月30日13:56:22
import unittest

import HTMLReport
from Business.login import cdms_获取token
from Common.data_文本读写 import *

from Test_Suite.suite_cmds_Summary import *

suite = unittest.TestSuite()
#收集用例之前先把token写到对应文件
# token = cdms_获取token()
# data_write('F:\\python\\EDDID_CDMS\\Data\\token.txt', token)

suite.addTests(get_suite_creatUser新建用户())
suite.addTests(get_suite_CreateExchange新建换汇申请单())
suite.addTests(get_suite_creatUser没有结构性产品账号及申请结构性产品审批())
suite.addTests(get_suite_CreatEquitiesWithdrawal出金())
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
#

if __name__ == '__main__':
    HTMLReport.TestRunner(
        title="EDDID_CDMS项目接口测试",
        description="如有疑问请联系-ganjiexiang",
        report_file_name="EDDID_CDMS项目接口测试",
        # report_file_name字段不能改，关系到Jenkins的配置报告的生成
        thread_count=1
    ).run(suite)
