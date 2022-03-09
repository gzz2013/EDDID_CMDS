import requests
from Business.login import cdms_获取token
from Config.cdms_config import *
import time

url="http://sit-cdms.ynm3k.com/api/emailInvestigateAccounts"

token = cdms_获取token()
s = requests.Session()

cookfront = cookfr
time.sleep(3)
print("cookfront={},token={}".format(cookfront,token))
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Connection": "keep-alive",
    "Cookie": cookfront+token,
    # "Cookie":"LANGUAGE=zh_CN; GB-SYS-SID-SIT=9CE8C4EBCC8907FF92BF15D85A4757547AC79FFD18F78973",
    # "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryLJxNiwANtIgOXc8F",
    # "Accept-Encoding":"gzip, deflate",
    # "Accept-Language":"zh-CN,zh;q=0.9"
}


# file = {
#     'file': open("C:\\Users\\Administrator\\Desktop\\100861.xlsx","rb"),   # => 用name指定文件
#     'Content-Disposition': "form-data",
#     'Content-Type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
#     'filename':'100861.xlsx'
#     }

file = {'file': ('100861.xlsx', open("C:\\Users\\Administrator\\Desktop\\100861.xlsx","rb"), 'application/vnd.ms-excel')}
time.sleep(2)
ur = s.post(url=url,files=file,headers=headers)  # => 注意这里，参数名是 files
print(ur.json())