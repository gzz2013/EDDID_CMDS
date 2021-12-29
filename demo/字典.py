# # -*- coding: utf-8 -*-
#
# s = "name=lyy&age=3&sex=women&boyfriend=czt"
# d = {}
# s1 = s.split("&")
# print("s1",s1)
# # print s1
# for i in range(4):
#     s2 = s1[i]
#     #  print s2
#     s3 = s2.split("=")
#     print("s3",s3)
#     key1 = s3[0]
#     value2 = s3[1]
#     d[key1] = value2
# print(d)
#
# print("###############################################")
Y="AAASDASDSAHHHGSDGEHRJFHJhhhhjhjdsadas"
# l=eval(Y)
# print("eval",p,type(p))
L1=[]
E={}
for i in Y:
    if i in L1:
        continue
    L1.append(i)

for n in range(len(L1)):
    key=n+1
    value=L1[n]
    E[key] = value
print("字符串Y=",Y)
print("字符串去重后得到列表L1=",L1)
print("列表长度：",len(L1))
print("字典E=",E)
print("字典E=",E.items())
# print("###############################################")
for i in range(1,5):
    print(i)








