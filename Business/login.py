import requests
from Common.MD5加密 import MD5_Encrypt
from Config.cdms_config import *


# from Common.token_写入 import tk_写入

# 运营人员登录获取token
def cdms_获取token():

    logins = requests.Session()
    # 登录访问的接口
    loginurl = url + "/api/auth/login"
    account = cdmsuser
    password = cdmsuserp
    # 账号密码
    data = {"account": account, "password": password}
    data['password'] = MD5_Encrypt(str=password)
    print("data=", data)
    res = logins.post(url=loginurl, data=data)
    token = res.json()["data"]["token"]
    return token


if __name__ == "__main__":
    print("token=", cdms_获取token())
