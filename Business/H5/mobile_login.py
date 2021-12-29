import requests
from Common.MD5加密 import MD5_Encrypt
from Config.cdms_config import *
from requests_toolbelt.multipart.encoder import MultipartEncoder
from Common.com_sql.h5_sql import *
from Common.data_文本读写 import *
import time

# 普通用户登录获取token
def h5_caccessToken():
    #登录依赖于账号停用的手机号
    phone = datahandle(data_read('F:\\python\\EDDID_CDMS\\Data\\unableAcct.txt'))[2]
    print("获取到的phone为",phone)
    url = app_base_url + '/open/auth/v2/token'
    url2=app_base_url+'/open/auth/v2/sms-code?phone=86'+str(phone)+'&device_id=7ae22fab33e4de39566b90aecb98c8a3&send_type=login'
    headers0 = {
        "accept": "application/json, text/plain, */*",
        "authorization": "Basic dGVzdGFwcDI6YWJjZA==",
        "content-type": "application/json;charset=utf-8"
    }
    # 点击获取验证码，数据库才会新增最新验证码
    r=requests.get(url=url2, headers=headers0)
    print(r.text,"已发送验证码，等到5秒")
    time.sleep(5)

    msg = get_code(phone)
    print("短信验证码：", msg)
    data = MultipartEncoder({
        "scope": "basic",
        "grant_type": "password",
        "login_type": "phone",
        "username": "86"+ str(phone),
        "pwd_type": "sms_code",
        "password": msg,
        "device_id": "7ae22fab33e4de39566b90aecb98c8a3"})
    header1 = {"Content-Type": data.content_type, "authorization": "Basic dGVzdGFwcDI6YWJjZA=="}

    res = requests.post(url=url, data=data, headers=header1)
    print("登录请求参数", data)
    print(res.json())
    global token
    token = res.json()['data']['access_token']
    # token=res.json().get("data").get("access_token")
    return token

if __name__ == "__main__":
    # create_sms_code()
    print("token=", h5_caccessToken())
