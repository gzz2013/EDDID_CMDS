import requests
import re


def dvwa_login():
    s =requests.session()
    url="http://192.168.222.128/dvwa/login.php"

    headers = {
        "Accept-Encoding": "gzip, deflate",
        "Connection": "close",
        # 'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
        # "Cookie": "security=impossible;PHPSESSID="+phpsessid,
        # "Upgrade-Insecure-Requests": "1"
    }
    #进入登录首页获取token
    r=s.get(url=url, headers=headers)
    # <input type='hidden' name='user_token' value='6d71d89f9775ada265dfbb0144cca63a' />
    # user_token = re.findall("name='user_token' value='(.*?)' />", session_res.text)[0]
    print(r.text)
    res = r'(?<=value=\').*?(?=\' />)'
    token = re.findall(res, r.text)[0]
    phpsessid= s.cookies['PHPSESSID']
    print("进入登录页面获取到的token={}，获取到的phpsessid={}".format(token,phpsessid))
    data = {
        "username": "admin",
        "password": "password",
        "Login": "Login",
        "user_token": token,
    }
    headers1 = {
        "Accept-Encoding": "gzip,deflate",
        "Connection": "close",
        "Cookie": "security=impossible;PHPSESSID="+ phpsessid,
    }
    print("++++++++++++++++++++++输入密码的路时的token={},headers={}".format(token,headers1))

    # 获取到token和cookie后，输入账号密码登录
    r2=s.post(url=url, headers=headers1, data=data,allow_redirects=True)
    print("status_code",r2.status_code)
    return r2.text

if __name__ == "__main__":
    r=dvwa_login()
    print("==============================================dvwa_login:{},响应报文长度:{}".format(r,len(r)))
