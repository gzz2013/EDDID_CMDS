# -*- coding: utf-8 -*-
import requests
import re
import random
def Login_art():
     l = '''  
 _                       _         
| |                     (_)        
| |       ___     __ _   _   _ __  
| |      / _ \   / _` | | | | '_ \ 
| |____ | (_) | | (_| | | | | | | |
\_____/  \___/   \__, | |_| |_| |_|
                  __/ |            
                 |___/             
                      by: xxxx
    '''
     print(l)

# 定义user_agent
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


# 获取token值
def get_token(url):
    # 使用session
    session = requests.session()
    session_res = session.get(url=url, headers={'User-Agent': user_agent()}, timeout=2)
    # 看当前的url是否能够访问成功，状态码是否正常
    if session_res.status_code == 200:
        print('[+] info: current url status code 200, continue...')
        # 状态码正常之后，需要匹配当前的token
        # print(get_login_res.text)
        try:
            user_token = re.findall("name='user_token' value='(.*?)' />", session_res.text)[0]
            if user_token != []:
                print('[+] user_token:', user_token)
                return user_token, session
            else:
                print("[-] info: get user_token error")
        except Exception as e:
            print(e)  # 打印出错误
    else:
        print('[-] info: sorry, current url invalid')


# 登录测试
def login(url, user_token, session):
    # 封装登录数据包并登录
    data = {
        'username': 'admin',
        'password': 'password',
        'Login': 'Login',
        'user_token': user_token
    }
    try:
        response_headers = session.post(url=url, headers={'User-Agent': user_agent()}, data=data, allow_redirects=True, timeout=2)
        # print(response_headers.status_code)
        # print(response_headers.text)
        # 判断当前是否登录成功
        if 'Welcome to Damn Vulnerable Web Application!' in response_headers.text:
            print('[+] info: login success!')
            # print('[] session', session.cookies)
            # PHPSESSID=7g2tri35g6jomor1islep0l2l7; security=impossible
            # 获得cookie值，这里的cookie值只需要一部分，因为后面需要对security的值进行修改
            no_security_cookie = 'PHPSESSID=' + session.cookies['PHPSESSID']
            print('[+] no_security_cookie:', no_security_cookie)
            return no_security_cookie, session
    except Exception as e:
        print(e)

def Login(url):
    # try:
    token, session = get_token(url)
    # 使用token和session进行登录操作，最后返回token
    no_security_cookie, session = login(url, token, session)
    # print(type(no_security_cookie))
    login_token = no_security_cookie + '; security=low'
    print('[+] login_cookies:', login_token)
    return no_security_cookie, login_token, session
    # except Exception as e:
    #     pass

if __name__ == '__main__':
    # url = "http://127.0.0.1:666/login.php"
    url = input('[+] please input your login url: ')
    url = str(url)
    # Login_art()
    # 先获取token
    Login(url)


