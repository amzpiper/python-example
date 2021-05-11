import xlrd

tableNameCol = 0
dataNameCol = 1
dataTypeCol = 3
dataDescriptCol = 2
isNotNullCol = 6
primaryCol =4
startSheet = 1
filePath = "E:/WechatCloudFiles/WeChat Files/wxid_vnje9jot5f7l22/FileStorage/File/2021-04/e316b79bb1f4e734f021dcaafb353ae4_6a2d42f073db8e88cf85513ef5c12a8e_8.xls"

# 初始化数据：sheet个数、sheet名
excel = xlrd.open_workbook(filePath)
sheetNames = excel.sheet_names()    #返回book中所有工作表的sheet名字
sheetNamesLen = len(sheetNames)
print("所有工作表的sheet个数:",sheetNamesLen)

# 处理sheet：有效行、有效列
arrysCreateTable = []
for index in range(startSheet,sheetNamesLen):
    sheet = excel.sheet_by_name(sheetNames[index])
    nrows = sheet.nrows
    ncols = sheet.ncols
    print("nrows:",nrows)
    print("ncols:",ncols)

    # 获取excel中表字段信息
    tableName = sheet.cell_value(1,tableNameCol)
    print("表名",index,":",tableName)
    strCreateTable = 'CREATE TABLE %s (' % tableName

    PrimaryColumn = ""
    for num in range(1,nrows-1):
        rowIndex = num-1
        dataName = sheet.cell_value(num,dataNameCol)
        strCreateTable=strCreateTable + " " + dataName

        dataType = sheet.cell_value(num,dataTypeCol)
        strCreateTable=strCreateTable + " " + dataType

        isNotNull = sheet.cell_value(num,isNotNullCol)
        print("isNotNull:",isNotNull)
        if isNotNull == "YES":
            strCreateTable=strCreateTable + " NULL"
        else:
            strCreateTable=strCreateTable + " NOT NULL"

        # 添加描述
        dataDescript = sheet.cell_value(num,dataDescriptCol)
        # strCreateTable=strCreateTable + " --" + dataDescript.replace(" ","")

        # 添加主键
        if sheet.cell_value(num,primaryCol) != "":
            PrimaryColumn = sheet.cell_value(num,dataNameCol)

        if rowIndex != nrows-3:
            strCreateTable = strCreateTable+" ,"

        print("num:",num)
        print("rowIndex:",rowIndex)
        print("(",num,",",dataNameCol,")","字段",num,":",dataName)
        print("(",num,",",dataTypeCol,")","字段类型",num,":",dataType)
        print("(",num,",",dataDescriptCol,")","字段描述",num,":",dataDescript)
        print("(",num,",",isNotNullCol,")","字段是否为空",rowIndex,":",isNotNull)
        print("(",num,",",primaryCol,")","字段",num,"是否Primary:",sheet.cell_value(rowIndex,primaryCol))

    if PrimaryColumn != "":
        strCreateTable = strCreateTable + " ," + "PRIMARY KEY ("+PrimaryColumn+")"
    strCreateTable = strCreateTable+" )"
    arrysCreateTable.append(strCreateTable)

for item in arrysCreateTable:
    print(item+"\n")

#写文件
with open('./createTable.sql','a') as f:
    for item in arrysCreateTable:
        f.write(item+"\n")
    f.close()
