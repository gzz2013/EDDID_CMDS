#2021年12月30日13:56:22
import unittest
from Test_Case.test_用户创建审批后停用 import Test_creatUser新建用户后停用
from Test_Case.test_enableAcct账号开启 import Test_enableAcct停用后开启
from Test_Case.test_创建入金申请单 import Test_CreatEquitiesDeposit入金
from Test_Case.test_创建出金申请单 import Test_CreatEquitiesWithdrawal出金
from Test_Case.test_创建其他类型交易账号 import Test_CreatUser创建其他类型交易账号
from Test_Case.test_创建大额入金申请单 import Test_CreatEquitiesDeposit大额入金
from Test_Case.test_创建换汇申请单 import Test_CreateExchange新建换汇申请单
from Test_Case.test_用户创建全类型交易账户及审批 import Test_creatUser新建用户创建所有类型账户
from Test_Case.test_用户创建审批 import Test_creatUser新建用户
from Test_Case.test_用户创建结构性产品账户及审批 import Test_creatUser没有结构性产品账号及申请结构性产品审批
from Test_Case.test_createClientBankApply import Test_CreateClientBank添加银行卡
from Test_Case.test_closeAcct账号关闭 import Test_closeAcct账号关闭
from Test_Case.test_mrktdat_sub行情申请_1229 import Test_Submit_mrktdat行情提交及审核
from Test_Case.test_h5_deposit入金_1230 import Test_H5_DEPOSIT入金
from Test_Case.test_SwapEquity转股_0106 import Test_SwapEquity转股
from Test_Case.test_updateClientInfo修改客户资料及审批_0111 import Test_UpdateClientInfo修改用户资料及审批
from Test_Case.test_h5_sub银行子账号申请_0119 import Test_sub_account_银行子账号申请及审核
from Test_Case.test_Nen出金申请及审批_0120 import Test_CreatEquitiesWithdrawalNew出金
from Test_Case.test_EDDA签约_0127 import Test_Creat_H5_eDDAcontract
from Test_Case.test_h5_EDDAdeposit入金_0128 import Test_H5_EDDAdeposit入金

def get_suite_creatUser新建用户后停用():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(Test_creatUser新建用户后停用))
    return suite

def get_suite_enableAcct停用后开启():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(Test_enableAcct停用后开启))
    return suite

def get_suite_CreatEquitiesDeposit入金():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(Test_CreatEquitiesDeposit入金))
    return suite

def get_suite_CreatEquitiesWithdrawal出金():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(Test_CreatEquitiesWithdrawal出金))
    return suite

def get_suite_CreatUser创建其他类型交易账号():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(Test_CreatUser创建其他类型交易账号))
    return suite

def get_suite_CreatEquitiesDeposit大额入金():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(Test_CreatEquitiesDeposit大额入金))
    return suite

def get_suite_CreateExchange新建换汇申请单():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(Test_CreateExchange新建换汇申请单))
    return suite

def get_suite_creatUser新建所有类型用户():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(Test_creatUser新建用户创建所有类型账户))
    return suite

def get_suite_creatUser新建用户():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(Test_creatUser新建用户))
    return suite

def get_suite_creatUser没有结构性产品账号及申请结构性产品审批():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(Test_creatUser没有结构性产品账号及申请结构性产品审批))
    return suite

def get_suite_CreateClientBank添加银行卡():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(Test_CreateClientBank添加银行卡))
    return suite

def get_suite_closeAcct账号关闭():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(Test_closeAcct账号关闭))
    return suite

def get_suite_Creat_mrktdat_sub():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(Test_Submit_mrktdat行情提交及审核))
    return suite

def get_suite_Creat_deposit_sub():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(Test_H5_DEPOSIT入金))
    return suite

def get_suite_SwapEquity转股():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(Test_SwapEquity转股))
    return suite


def get_suite_UpdateClientInfo修改用户资料及审批():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(Test_UpdateClientInfo修改用户资料及审批))
    return suite

def get_suite_Subaccount银行子账号申请及审核():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(Test_sub_account_银行子账号申请及审核))
    return suite

def get_suite_CreatEquitiesWithdrawalnew出金():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(Test_CreatEquitiesWithdrawalNew出金))
    return suite

def get_suite_Creat_H5_eDDAcontract():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(Test_Creat_H5_eDDAcontract))
    return suite

def get_suite_Creat_H5_EDDAdeposit入金():
    loader=unittest.TestLoader()
    suite=unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(Test_H5_EDDAdeposit入金))
    return suite