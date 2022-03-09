import requests
import re
import random

#生成随机数
def ranstr(num):
    H = 'abcdefghijklmnopqrstuvwxyz0123456789'
    salt = ''
    for i in range(num):
        salt += random.choice(H)
    return salt

def user_agent():
    user_agent_list = [
             'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 ',
             'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
             'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
             'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
             'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
             'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
             'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrow 20 ser/2.0 Safari/536.11',
             'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET',
             'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',
             'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36'
         ]
    return random.choice(user_agent_list)



def dvwa_login():

    # 生成随机PHPSESSID，全部设置为全局变量
    global phpsessid,host,token
    s =requests.session()
    host="http://192.168.222.128/dvwa/"
    url=host+"login.php"
    # 生成随机phpsessid
    phpsessid=ranstr(24)
    headers = {
        "Accept-Encoding": "gzip, deflate",
        "Connection": "close",
        # "Cookie": "security=impossible;PHPSESSID="+phpsessid,
        # "Cookie": "security=impossible;PHPSESSID="+phpsessid,
        # "Upgrade-Insecure-Requests": "1"
    }
    #进入登录首页获取token
    r1=s.get(url=url, headers=headers, timeout=2)
    t=r1.text
    print(t)
    # <input type='hidden' name='user_token' value='6d71d89f9775ada265dfbb0144cca63a' />
    # user_token = re.findall("name='user_token' value='(.*?)' />", session_res.text)[0]

    res = r'(?<=value=\').*?(?=\' />)'
    token = re.findall(res, r1.text)[0]
    no_security_cookie= s.cookies['PHPSESSID']

    #获取token后输入账号密码登录
    data = {
        "username": "admin",
        "password": "password",
        "Login": "Login",
        "user_token": token,
    }
    headers = {
        "Accept-Encoding": "gzip, deflate",
        "Connection": "close",
        # "Cookie": "security=impossible;PHPSESSID="+phpsessid,
        "Cookie": "security=impossible;PHPSESSID="+ no_security_cookie,
        # "Upgrade-Insecure-Requests": "1"
    }

    print("+++++++++++++++++++++登录前的phpsessid为：",phpsessid)
    print("++++++++++++++++++++++登录前的token为：",token)

    r2=s.post(url=url, headers=headers, data=data,allow_redirects=True)
    print("status_code",r2.status_code)
    # reditList = r2.history
    # print("____________________reditList", reditList)
    # print("____________________reditList[-1].headers", reditList[0].headers)
    #拼接重定向url
    # loct=r2.history[0].headers["Location"]
    # url1=host+loct
    # print("____________________重定向地址拼接完成url1={}，headers={}".format(url1,headers))
    # r3 = s.get(url=url1, headers=headers)
    return r2.text

if __name__ == "__main__":
    r=dvwa_login()
    print("==============================================dvwa_login:{},响应报文长度:{}".format(r,len(r)))
