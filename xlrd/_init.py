import xlrd
# 1.读取sheet
data = xlrd.open_workbook("E:/WechatCloudFiles/WeChat Files/wxid_vnje9jot5f7l22/FileStorage/File/2021-04/e316b79bb1f4e734f021dcaafb353ae4_6a2d42f073db8e88cf85513ef5c12a8e_8.xls")#打开当前目录下名为01.xls的文档
#此时data相当于指向该文件的指针
table = data.sheet_by_index(0)#通过索引获取，例如打开第一个sheet表格
print(table)
table = data.sheet_by_name("说明")#通过名称获取，如读取sheet1表单
print(table)
table = data.sheets()[0]#通过索引顺序获取
print(table)
# 以上三个函数都会返回一个xlrd.sheet.Sheet()对象
names = data.sheet_names()    #返回book中所有工作表的sheet名字
print("所有工作表的sheet名字:",names)
# data.sheet_loaded(sheet_name or indx)   # 检查某个sheet是否导入完毕
print("所有工作表的sheet个数",len(names))

# 2.读取sheet中的行
nrows = table.nrows  #获取该sheet中的有效行数
print("sheet中的有效行数",nrows)
# table.row(nrows)  #返回由该行中所有的单元格对象组成的列表
# table.row_slice(nrows)  #返回由该列中所有的单元格对象组成的列表
# table.row_types(nrows, start_colx=0, end_colx=None)  #返回由该行中所有单元格的数据类型组成的列表
# table.row_values(nrows, start_colx=0, end_colx=None)  #返回由该行中所有单元格的数据组成的列表
# table.row_len(nrows) #返回该列的有效单元格长度

# 3.读取sheet中的列
# ncols = table.ncols#获取列表的有效列数
# table.col(ncols, start_rowx=0, end_rowx=None)#返回由该列中所有的单元格对象组成的列表
# table.col_slice(ncols, start_rowx=0, end_rowx=None)#返回由该列中所有的单元格对象组成的列表
# table.col_types(ncols, start_rowx=0, end_rowx=None)#返回由该列中所有单元格的数据类型组成的列表
# table.col_values(ncols, start_rowx=0, end_rowx=None)#返回由该列中所有单元格的数据组成的列表

# table.cell(1, 1)  # 返回单元格对象
# table.cell_type(rowx, colx)  # 返回单元格中的数据类型
value = table.cell_value(0,0)   #返回单元格中的数据
print("单元格中的数据:",value)
