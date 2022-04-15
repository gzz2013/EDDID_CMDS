import os
import logging
# import logging.handlers
import datetime

# mysql的数据库的配置
import smtplib

# 邮件配置
sender = "j@wetax.com.cn" # 发送方
# receiver = "jack.ma@wetax.com.cn,martin.lv@wetax.com.cn"        # 接收方,多个收件人以逗号隔开"xx@qq.com,yy@qq.com"
receiver = "jenny.zhang@wetax.com.cn"        # 接收方,多个收件人以逗号隔开"xx@qq.com,yy@qq.com"
emailusername = "jenny.zhang@wetax.com.cn"  # 登录邮箱的用户名
emailpassword = "Zxz123456"             # 登录邮箱的密码,请配置自己的
# server = "smtp.qq.com"  # smtp服务器
server = "smtp.exmail.qq.com"  # smtp服务器
# server = smtplib.SMTP_SSL("smtp.exmail.qq.com",port=465)

#  项目目录
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#获取根目录路径

# 数据目录
datapath = os.path.join(basedir,'data')
file = os.path.join(datapath, '接口测试用例.xlsx')
# file2 = os.path.join(datapath, '区块链电子发票信息采集表2.xlsx')
# 报告目录
reportpath = os.path.join(basedir, 'report')

#  日志配置
logdir = os.path.join(basedir, 'log')
logpath =os.path.join(logdir, 'apiall.log')
error =os.path.join(logdir, 'apierror.log')
logger = logging.getLogger('apitest')
# 打印全部信息
logger.setLevel(logging.DEBUG)

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)#输出到file的log的等级开关

fh = logging.handlers.TimedRotatingFileHandler(logpath, when='D', interval=1, backupCount=5,atTime=datetime.time(0, 0, 0, 0),encoding='utf-8')
# interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
# S 秒
# M 分
# H 小时、
# D 天、
# W 每星期（interval==0时代表星期一）
# midnight 每天凌晨
# fh = logging.FileHandler(logpath, encoding='utf-8')
datafmt = "%Y-%m-%d %H:%M:%S"
fm = logging.Formatter(fmt='%(asctime)s %(name)-s %(module)-s[line:%(lineno)d] %(levelname)-s -- %(message)s',datefmt=datafmt)#
fh.setFormatter(fm)
ch.setFormatter(fm)
logger.addHandler(fh)  #打印到文件
logger.addHandler(ch)  #打印到控制台
logging.getLogger("requests").setLevel(logging.WARNING)

# # 打印错误信息
f_handler = logging.handlers.TimedRotatingFileHandler(error, when='S', interval=1, backupCount=5,atTime=datetime.time(0, 0, 0, 0),encoding='utf-8')#
f_handler.setLevel(logging.ERROR)
datafmt = "%Y-%m-%d %H:%M:%S"
# fm = logging.Formatter(fmt='%(asctime)s %(name)-s %(module)-s[line:%(lineno)d] %(levelname)-s -- %(message)s',datefmt=datafmt)#
f_handler.setFormatter(fm)#
logger.addHandler(f_handler)


#域名
# base_url_sit="http://192.168.57.20:90"
base_url_sit="http://sit-cdms.ynm3k.com/"
#sit  http://192.168.57.22:80
base_url_uat="https://uat-cdms.eddidson.com"
# base_url_stress="http://192.168.57.23/"#压测环境
base_url_stress="http://192.168.57.21"#压测环境
header_uat='GB-SYS-SID-UAT='
header_stress='GB-SYS-SID-STRESS='
header_sit='GB-SYS-SID-SIT='

aos_base_url_sit="https://aos-api-qa.eddid.com.cn:1443"#"https://aos-api-qa.eddid.com.cn:1443"
aos_base_url_uat="https://aos-api-uat.eddid.com.cn:1443"#"https://aos-api-qa.eddid.com.cn:1443"
app_base_url_sit='https://route-service-qa.eddid.com.cn:1443'

# 生成时间戳

# titletimes = datetime.datetime.now().strftime("%Y%m%d%H%M")

if __name__ == "__main__":
    logger.info('this is test')
    # logger.addHandler(fh)
    logger.addHandler(f_handler)
    print("根目录：{}".format(basedir))


