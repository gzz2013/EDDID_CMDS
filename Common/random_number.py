import datetime
import random
import time
import json
import string
from datetime import date,timedelta

class CreateRanDom():
    def r_string(self):#生成随机字符串
        data="1234567890zxcvbnmlkjhgfdsaqwertyuiop"
        #用时间来做随机播种
        random.seed(time.time())
        #随机选取数据
        sa=[]
        for i in range(5):
            sa.append(random.choice(data))
        salt="gp_"+''.join(sa)
        # print(salt)
        return salt

class Randoms():
    # 获取26个大小写字母
    letters = string.ascii_letters
    # 获取26个小写字母
    Lowercase_letters = string.ascii_lowercase
    # 获取26个大写字母
    Capital = string.ascii_uppercase
    # 获取阿拉伯数字
    digits = string.digits

    #随机code
    def code(self):
        # s是小写字母和数字的集合
        s = Randoms.Lowercase_letters+Randoms.digits
        #生成28位小写和数字的集合，并将列表转字符串
        code=''.join(random.sample(s,28))
        print('随机code:%s'%code)
        return code

    #随机税号
    # def tax_code(self):
    #     list_1=['I','O','Z','S','V']
    #     list_2=[]
    #     #新建容器list_2放置过滤后的数据
    #     #添加过滤条件,数据源不在list_1中，即需要的数据
    #     #将过滤后的数据放进list_2中
    #     for j  in  randoms().Capital:
    #         if j not in list_1:
    #             list_2.append(j)
    #     s =''.join(list_2)  + randoms().digits
    #     #print(s)
    #     tax_code=''.join(random.sample(s,18))
    #     print('随机税号:%s'%tax_code)
    #     return tax_code

    def tax_code(self):  # 生成随机字符串
        data = "1234567890xcbnmlkjhgfdaqwertyup"
        # 用时间来做随机播种
        random.seed(time.time())
        # 随机选取数据
        sa = []
        for i in range(10):
            sa.append(random.choice(data))
        salt_code = "GAPEN" + ''.join(sa)
        # print(salt)
        print('随机税号:%s' % salt_code)
        return salt_code

    def tax_code_c(self):  # 生成重庆地区税号
        data = "1234567890xcbnmlkjhgfdaqwertyup"
        # 用时间来做随机播种
        random.seed(time.time())
        # 随机选取数据
        sa = []

        list=["500000","500100","500101","500102","500103","500104","500105","500106","500107","500108","500109","500110","500111","500112",
              "500113","500114","500115","500116","500117","500118","500119","500120","500151","500152","500153","500154","500200","500228",
              "500229","500230","500231","500232","500233","500235","500236","500237","500238","500240","500241","500242","500243"]
        slice = random.sample(list, 1)
        print("获取到的slice",slice)
        # print(type(slice))
        # print(''.join(slice))
        # print(''.join(sa))
        # print(sa)
        # print(type(sa))

        for i in range(7):
            sa.append(random.choice(data))
        salt_code = "GA" +''.join(slice)+''.join(sa)
        # print(salt)
        print('随机税号:%s' % salt_code)
        return salt_code


    def sub_acc(self):  # 生成随机子账号
        data = "1234567890zxcvbnmlkjhgfdsaqwertyuiop"
        # 用时间来做随机播种
        random.seed(time.time())
        # 随机选取数据
        sa = []
        for i in range(10):
            sa.append(random.choice(data))
        salt_code = "TEST" + ''.join(sa)
        # print(salt)
        print('随机税号:%s' % salt_code)
        return salt_code

    # def email(self):  # 生成随机子账号
    #     data = "1234567890zxcvbnmlkjhgfdsaqwertyuiop"
    #     # 用时间来做随机播种
    #     random.seed(time.time())
    #     # 随机选取数据
    #     sa = []
    #     for i in range(10):
    #         sa.append(random.choice(data))
    #     salt_code = "TEST" + ''.join(sa)
    #     # print(salt)
    #     print('随机税号:%s' % salt_code)
    #     return salt_code

    # def telephone(self):
    #     # 第二位数字
    #     second = [3, 4, 5, 7, 8][random.randint(0, 4)]
    #
    #     # 第三位数字
    #     third = {
    #         3: random.randint(0, 9),
    #         4: [5, 7, 9][random.randint(0, 2)],
    #         5: [i for i in range(10) if i != 4][random.randint(0, 8)],
    #         7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
    #         8: random.randint(0, 9),
    #     }[second]
    #
    #     # 最后八位数字
    #     suffix = random.randint(10000000, 99999999)
    #
    #     # 拼接手机号
    #     telephone="1{}{}{}".format(second, third, suffix)
    #     print('手机号:%s'%telephone)
    #     return telephone

    def telephone(self):#十一位
        second = [1, 2, 6, 9, 0][random.randint(0, 4)]
        suffix = random.randint(100000000, 999999999)

        # 拼接手机号
        telephone="1{}{}".format(second,suffix)
        print('手机号:%s'%telephone)
        return telephone
    def hk_idcard(self):#十一位
        second = [1, 2, 6, 9, 0][random.randint(0, 4)]
        suffix = random.randint(100000000, 999999999)

        # 拼接手机号
        hk_idcard="1{}{}".format(second,suffix)+'(1)'
        print('证件号:%s'%hk_idcard)
        return hk_idcard

    def number(self):
        data = "1234567890"
        # 用时间来做随机播种
        random.seed(time.time())
        # 随机选取数据
        sa = []
        for i in range(8):
            sa.append(random.choice(data))
        salt_num =''.join(sa)
        # print(salt)
        print('随机数字:%s' % salt_num)
        return salt_num

    import random, datetime
    """生成大陆身份证"""
    def ident_generator(self):
        # 身份证号的前两位，省份代号
        sheng = (
        '11', '12', '13', '14', '15', '21', '22', '23', '31', '32', '33', '34', '35', '36', '37', '41', '42', '43',
        '44', '45', '46', '50', '51', '52', '53', '54', '61', '62', '63', '64', '65', '66')
        # 随机选择距离今天在7000到25000的日期作为出生日期（没有特殊要求我就随便设置的，有特殊要求的此处可以完善下）
        birthdate = (datetime.date.today() - datetime.timedelta(days=random.randint(7000, 25000)))
        # 拼接出身份证号的前17位（第3-第6位为市和区的代码，中国太大此处就偷懒了写了定值，有要求的可以做个随机来完善下；第15-第17位为出生的顺序码，随机在100到199中选择）
        ident = sheng[random.randint(0, 31)] + '0101' + birthdate.strftime("%Y%m%d") + str(random.randint(100, 199))
        # 前17位每位需要乘上的系数，用字典表示，比如第一位需要乘上7，最后一位需要乘上2
        coe = {1: 7, 2: 9, 3: 10, 4: 5, 5: 8, 6: 4, 7: 2, 8: 1, 9: 6, 10: 3, 11: 7, 12: 9, 13: 10, 14: 5, 15: 8, 16: 4,17: 2}
        summation = 0
        # for循环计算前17位每位乘上系数之后的和
        for i in range(17):
            summation = summation + int(ident[i:i + 1]) * coe[i + 1]  # ident[i:i+1]使用的是python的切片获得每位数字
        # 前17位每位乘上系数之后的和除以11得到的余数对照表，比如余数是0，那第18位就是1
        key = {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}
        # 拼接得到完整的18位身份证号
        return ident + key[summation % 11]


    #生成随机金额
    def randomAmount(self):
        random.seed(time.time())
        rAmount=float(random.randint(2,10))+float('%.2f'%(random.random()))
        return rAmount

    #生成随机金额
    def randomlargeAmount(self):
        random.seed(time.time())
        rAmount=float(random.randint(10000,19999))+float('%.2f'%(random.random()))
        return rAmount

    #生成随机转股数
    def randomintNumber(self):
        random.seed(time.time())
        rAmount=int(random.randint(10,99))+int(random.randint(1,9))
        return rAmount

    #生成邮箱
    # -*- coding:utf-8 -*-
    def RandomEmail(emailType=None, rang=None):
        __emailtype = ["@qq.com", "@163.com", "@126.com", "@189.com","@gzz.com","@edd.com"]
        # 如果没有指定邮箱类型，默认在 __emailtype中随机一个
        if emailType == None:
            __randomEmail = random.choice(__emailtype)
        else:
            __randomEmail = emailType
        # 如果没有指定邮箱长度，默认在4-10之间随机
        if rang == None:
            __rang = random.randint(8, 10)
        else:
            __rang = int(rang)
        __Number = "0123456789qbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ"
        __randomNumber = "".join(random.choice(__Number) for i in range(__rang))
        _email = __randomNumber + __randomEmail
        return _email

    #生成英文姓氏
    def creat_EFName(self):
        EF = ["Baker", "Cook", "Miller", "Turner", "Smith", "London", "Hall", "Kent", "Mill", "Brook", "Churchill", "Hill",
              "Green", "Wood", "Well", "Brown", "White", "Longman", "Sharp", "Yonng", "Back", "Hand", "Finger", "Brain",
              "Bird", "Bull", "Cotton", "Fox", "Stock", "Cotton", "Reed", "George", "Henry", "David", "Clinton", "Macadam"]
        Number = "0123456789qbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ"
        random.seed(time.time())
        FName = random.choice(EF)+ random.choice(Number)
        return FName

    #生成英文名字
    def creat_ELName(self):
        EL = ["Boyce", "Elvis", "Ziv", "Eudolf", "Steven", "Tyrone", "Owen", "Herman", "Andrew", "Vic", "Miles", "Eonald",
              "Wden", "Will", "Eock", "Owen", "Abbott", "Cornelius", "Dali", "Fallon", "Harsh", "Kirby", "Vvincent"]
        random.seed(time.time())
        LName = random.choice(EL)
        return LName


    #生成中文姓氏
    def creat_CHName(self):
        CF=["李","王","张","刘","陈","杨","赵","冯","于","曹","袁","康","邱","秦","江","崔","白","郝","傅","曹","程","梁","胡","何","赵"]
        CL=["彩绘","浪花","米猪","一手","蜜蜂","菜花","西瓜","油条","大佬","细佬","大山","哦耶","一龙","奶油","大锤","悠悠","清水","白羽","百余","白云","黑土","源","渊","广厦","午后","铃","凰","承","辉"]
        Number = "0123456789qbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ"
        random.seed(time.time())
        FName = random.choice(CF)
        LName = random.choice(CL) + random.choice(Number)
        CHName=FName + LName
        return CHName

    #随机选择性别
    def choice_title(self):
        T=["miss","mr","mrs"]
        random.seed(time.time())
        title = random.choice(T)
        return title

    #随机选择账户类型
    def choice_accts(self):

        T=["securitiesCash","securitiesMargin","futuresMargin","leveragedForeignExchangeAccountMargin","securitiesAyersCash",]
        random.seed(time.time())
        accts = random.choice(T)
        return accts

    #随机选择账户类型
    def choice_accts_nofutures(self):
        T=["securitiesCash","securitiesMargin","leveragedForeignExchangeAccountMargin","securitiesAyersCash",]
        random.seed(time.time())
        accts = random.choice(T)
        return accts

    #随机账户
    def choice_clientId(self):
        T=[11431,12071]
        random.seed(time.time())
        accts = random.choice(T)
        return accts

    def choice_Language(self):
        #"zh-hant"=繁体；"zh-hans"=简体
        T=["zh-hans","zh-hant"]
        random.seed(time.time())
        accts = random.choice(T)
        return accts

    def choice_bankCode(self):
        #"zh-hant"=繁体；"zh-hans"=简体
        Code=['003', '004', '005', '006', '007', '008', '009', '012', '014', '015', '016', '018', '019', '020', '022', '024', '025', '026', '027', '028', '030', '031', '033', '035', '036', '038', '039', '040', '041', '043', '044', '045', '046', '047', '049', '050', '054', '055', '056', '058', '060', '061', '063', '064', '065', '066', '067', '070', '071', '072', '074', '076', '080', '081', '082', '085', '086', '092', '097', '103', '106', '109', '113', '118', '119', '128', '138', '139', '145', '147', '150', '151', '152', '153', '161', '164', '165', '170', '178', '180', '183', '185', '186', '188', '198', '199', '201', '202', '203', '205', '206', '210', '214', '218', '220', '221', '222', '224', '227', '229', '230', '233', '235', '236', '237', '238', '239', '241', '242', '243', '245', '248', '250', '251', '256', '257', '258', '259', '260', '261', '262', '263', '264', '265', '266', '267', '268', '269', '271', '272', '273', '274', '275', '276', '277', '278', '307', '308', '309', '313', '316', '320', '324', '337', '338', '339', '341', '342', '344', '345', '350', '353', '357', '368', '371', '374', '377', '378', '379', '381', '382', '383', '385', '386', '387', '388', '389', '390', '391', '392', '393', '395', '868', '929', '931', '934', '935', '948', '949', '952', '954', '955', '9999', '99999', 'SIB']
        #用时间来做随机播种
        # print(type(Code))
        random.seed(time.time())
        bankCode=random.choice(Code)

        return bankCode





if __name__ == '__main__':
    # Randoms().tax_code()
    # Randoms().code()
    # Randoms().tax_code_c()
    c=CreateRanDom()
    tel=c.r_string()
    print("tel:::",tel)
    # print(tel)
    # print(Randoms().number())

    # # 此处可以完善下，需要大量的身份证号的或者是需要做自动化的可以把身份证号做下去重之后再写进文件
    # for j in range(10):
    #     print(Randoms().ident_generator())

    print(Randoms.RandomEmail())
    print(Randoms().creat_CHName())
    print(Randoms().randomAmount())
    print(Randoms().randomlargeAmount())
    print(Randoms().choice_bankCode())
    nb=Randoms().randomintNumber()
    print("randomintNumber:",type(nb),nb)

# 42 9004 19940327 117 5