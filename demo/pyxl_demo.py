# -*- coding: utf-8 -*-
import xlrd
import xlwt
from datetime import date,datetime
import openpyxl
import  sys

# workbook = xlrd.open_workbook("test.xlsx", formatting_info=False)
# 获取有的sheet

# workbook = xlrd.open_workbook("E:\\test.xlsx")
workbook = xlrd.open_workbook("C:\\Users\\Administrator\\Desktop\\ecxl_demo.xls")

print("所有的工作表：", workbook.sheet_names())

# sheet1的名称、行数、列数
sheet1=workbook.sheets()[0]
print("工作表名称：%s，行数：%d，列数：%d" % (sheet1.name, sheet1.nrows, sheet1.ncols))

# 打印出所有合并的单元格
# merged_cells(a,b,c,d) 单元格合并函数
# a 单元格的起始行
# b 单元格的结束行
# c 从单元格的起始列
# d 单元格的结束列
# 注：单元格的列号和行号都是从0开始计
print(sheet1.merged_cells)
for (row, row_range, col, col_range) in sheet1.merged_cells:
    print(row, row_range, col, col_range)
    print(sheet1.cell_value(row, col))
    # print(sheet1.cell_value(row_range, col_range))

# 获取整行和整列的值
row = sheet1.row_values(0)
col = sheet1.col_values(3)
print("第2行的值：%s" % row)
print("第4列的值：%s" % col)

# 获取单元格的内容
print("第一行第一列：%s" % sheet1.cell(0, 0).value)
print("第一行第二列：%s" % sheet1.cell_value(0, 0))
print("第一行第三列：%s" % sheet1.row(0)[2])

49


def set_style(name, height, bold=False):

    """设置单元格样式"""



    style = xlwt.XFStyle()  # 初始化样式

    font = xlwt.Font()  # 为样式创建字体

    font.name = name  # 设置字体名字对应系统内字体

    font.bold = bold  # 是否加粗

    font.color_index = 5  # 设置字体颜色

    font.height = height  # 设置字体大小

      # 设置边框的大小
    borders = xlwt.Borders()

    borders.left = 6

    borders.right = 6

    borders.top = 6

    borders.bottom = 6

    style.font = font  # 为样式设置字体

    style.borders = borders

    return style

def write_excel(xname):
     # """写入excel"""
    writeexcel = xlwt.Workbook()    # 创建工作表
    sheet1 = writeexcel.add_sheet(u"Sheet1", cell_overwrite_ok = True)    # 创建sheet
    row0 = ["编号", "姓名", "性别", "年龄", "生日", "学历"]
    num = [1, 2, 3, 4, 5, 6, 7, 8]
    column0 = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8"]
    education = ["小学", "初中", "高中", "大学"]

    # 生成合并单元格
    i,j = 1,0
    while i < 2*len(education) and j < len(education):
        #write_merge(a,b,c,d,e,f)：将第a行到第b行，第c列到第d列，就行合并；插入e的内容；用f样式；e和f可以不传
        sheet1.write_merge(i, i+1, 5, 8)
        i += 2
        j += 1

    # 生成第一行
    for i in range(0, 6):
        sheet1.write(0, i, row0[i])

    # 生成前两列
    for i in range(1, 9):
        # a=num[i-1]
        b=column0[i-1]
        sheet1.write(i, 0, i)
        sheet1.write(i, 1, b)
    # 添加超链接
    n = "HYPERLINK"
    sheet1.write_merge(9,9,0,5,xlwt.Formula(n + '("https://www.baidu.com")'))
    # 保存文件
    # xname=A+".xls"
    writeexcel.save(xname)

if __name__ == '__main__':
    xname="C:\\Users\\Administrator\\Desktop\\ecxl_demo5.xls"
    write_excel(xname)
