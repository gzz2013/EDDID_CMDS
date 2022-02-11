# from Common.random_number import *
# caccts=Randoms().choice_accts()
from Common.com_sql.eddid_data_select import *

def check_accts(accts):
    if accts=="leveragedForeignExchangeAccountMargin":
        busin_acty_cde="FOREX"
    elif accts=="futuresMargin":
        busin_acty_cde = "FUTURES"
    else:
        busin_acty_cde = "EQUITIES"
    return busin_acty_cde

#查询账号类型
def accountCategory(ac_id):
    try:
        acinfor=cd_ac_id(ac_id)
        busin_acty_cde=acinfor[0][4]
        ac_catg=acinfor[0][5]
    except Exception as e:
        print("交易账号错误，请核实后再提交，查询为空所有值为默认值！", e)
        accountCategoryCode = 'securitiesCash'
        accountCategoryAlias = '香港及环球证券账户(现金)'
        tradeAccountType = 'SECURITIES_CASH'
        EDDACollectionAccount = '783266717'

        return accountCategoryCode,tradeAccountType,accountCategoryAlias,EDDACollectionAccount
    else:
        #ex：501121
        if busin_acty_cde=='EQUITIES' and ac_catg =='CASH':
            accountCategoryCode='securitiesCash'
            accountCategoryAlias='香港及环球证券账户(现金)'
            tradeAccountType = 'SECURITIES_CASH'
            EDDACollectionAccount='783266717'

        #ex："accountId":"5011211210"
        elif busin_acty_cde=='EQUITIES' and ac_catg=='MARGIN':
            accountCategoryCode='securitiesMargin'
            accountCategoryAlias='香港及环球证券账户(保证金)'
            tradeAccountType='SECURITIES_MARGIN'
            EDDACollectionAccount = '783266717'

        #ex："accountId":"5011213210"
        elif busin_acty_cde=='FUTURES' and ac_catg=='MARGIN':
            accountCategoryCode='futuresMargin'
            accountCategoryAlias='香港及环球期货账户(保证金)'
            tradeAccountType = 'FUTURES_MARGIN'
            EDDACollectionAccount = '000265077'

        #ex："accountId": "50112132132"
        elif busin_acty_cde=='EQUITIES' and ac_catg=='CASH':
            accountCategoryCode='securitiesAyersCash'
            accountCategoryAlias='全权委托证券（现金）账户'
            tradeAccountType = 'SECURITIES_AYERS_CASH'
            EDDACollectionAccount = '783266717'

        #ex："accountId":"501121521"
        elif busin_acty_cde=='FUTURES' and ac_catg=='MARGIN':
            accountCategoryCode='futuresDayTradeMargin'
            accountCategoryAlias='香港期货即日买卖账户(保证金)'
            tradeAccountType = 'FUTURES_DAYTRADING_MARGIN'
            EDDACollectionAccount = '000265077'

        #ex："accountId":"5011215216"
        elif busin_acty_cde=='FOREX' and ac_catg=='MARGIN':
            accountCategoryCode='leveragedForeignExchangeAccountMargin'
            accountCategoryAlias='杠杆式外汇账户(保证金)'
            tradeAccountType = 'MT5'
            #EDDA入金和杠杆外汇账号不相关
            EDDACollectionAccount = '783266717'

        return accountCategoryCode,tradeAccountType,accountCategoryAlias,EDDACollectionAccount

#根据账号类型查询收款银行账号,收款的银行账号为指定的收款币种账号
def getbankAccountNumber(ac_id,currency):
    try:
        acinfor=cd_ac_id(ac_id)
        busin_acty_cde=acinfor[0][4]

    except Exception as e:
        print("交易账号错误，请核实后再提交！查询为空所有值为默认值！", e)
        bankAccountNumber='016-478-783313006'
        return bankAccountNumber
    else:
        #ex：501121
        if busin_acty_cde=='EQUITIES':
            if currency=='HKD':
                bankAccountNumber='016-478-783313006'
            elif currency=='USD':
                bankAccountNumber='016-478-000677626'
            elif currency == 'CNY':
                bankAccountNumber = '016-478-000677635'

        elif busin_acty_cde=='FUTURES':
            if currency=='HKD':
                bankAccountNumber='016-478-000324487'
            elif currency=='USD':
                bankAccountNumber='016-478-000677644'
            elif currency == 'CNY':
                bankAccountNumber ='016-478-000677653'
        return bankAccountNumber

if __name__=="__main__":
    # accts="securitiesAyersCash"
    # print("账户类型为：",check_accts(accts))
    ac_id=11431
    accountCode=accountCategory(ac_id)
    print("用户ID：{}；accountCategoryCode为:{}；accountCategoryAlias为:{}。".format(ac_id, accountCode[0],accountCode[1]))

    print(getbankAccountNumber(11431,'CNY'))
