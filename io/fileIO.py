# 读文件
with open('./io/text.txt','r',encoding='utf8',errors='ignore') as f:
    #小文件-一次性读取
    # print(f.read())
    #大文件一行一行读取
    for line in f.readlines():
        print(line.strip())

#写文件
with open('./io/text2.txt','w') as f:
    f.write('text')
    f.close()