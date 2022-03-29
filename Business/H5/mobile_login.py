import requests
from Common.MD5加密 import MD5_Encrypt
from Config.cdms_config import *
from requests_toolbelt.multipart.encoder import MultipartEncoder
from Common.com_sql.h5_sql import *
from Common.data_文本读写 import *
import time

# 普通用户登录获取token
def h5_caccessToken(phone):
    #登录依赖于账号停用的手机号

    #如果phone不传值，就读取文本的号码
    if phone=='':
        get_phone = datahandle(data_read('F:\\python\\EDDID_CDMS\\Data\\unableAcct.txt'))[2]
    else:
        get_phone=phone

    print("获取到的phone为",phone)
    url = app_base_url + '/open/auth/v2/token'
    url2=app_base_url+'/open/auth/v2/sms-code?phone=86'+str(get_phone)+'&device_id=b20c0b8120addd6ebdd92d0269a2cfdb&send_type=login'
    headers0 = {
        "accept": "application/json, text/plain, */*",
        "authorization": "Basic dGVzdGFwcDI6YWJjZA==",
        "content-type": "application/json;charset=utf-8"
    }
    # 点击获取验证码，数据库才会新增最新验证码
    r=requests.get(url=url2, headers=headers0)
    print(r.text,"已发送验证码，等到5秒")
    time.sleep(5)

    msg = get_code(get_phone)
    print("短信验证码：", msg)
    data = MultipartEncoder({
        "scope": "basic",
        "grant_type": "password",
        "login_type": "phone",
        "username": "86"+ str(get_phone),
        "pwd_type": "sms_code",
        "password": msg,
        "device_id": "b20c0b8120addd6ebdd92d0269a2cfdb"})
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
