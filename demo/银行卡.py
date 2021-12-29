def data_read(file):
    with open(file, 'r',encoding="utf-8") as data_txt:
        # for text in data_txt.readlines():
        L=[]
        for text in data_txt.readlines():
            L.append(text.strip("\n"))
        return L


def data_write(file,d):
    with open(file,'w',encoding="utf-8") as data_txt:
        # data_txt.write(str(d))
        data_txt.writelines(str(d))
        # data_txt.writelines("d,",{str(d)})



# ac_id_l = (data_read('F:\\python\\EDDID_CDMS\\Data\\unableAcct.txt'))
# q=data_read('C:\\Users\\Administrator\\Desktop\\dasd.txt')
q=(data_read('F:\\python\\EDDID_CDMS\\Data\\dasd.txt'))
# print(ac_id_l)
print(q)
data_write('F:\\python\\EDDID_CDMS\\Data\\news.txt',q)



