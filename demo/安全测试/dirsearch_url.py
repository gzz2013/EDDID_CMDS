#2022年3月22日16:33:25
import time
import  requests
url="http://192.168.175.129/"
# mulu=["readme.txt","reae.txt","images","index.html"]
#
# for i in  mulu:
#     print(i)
#     print(url+i)
#     time.sleep(2)
#     res=requests.get(url+i)
#     print(res.status_code)

mulu="readme.txt","reae.txt","images","index.html"



for i in  mulu:
    print(i)
    print(url+i)
    time.sleep(2)
    res=requests.get(url+i)
    print(res.status_code)