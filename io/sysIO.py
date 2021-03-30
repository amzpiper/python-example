import time

#操作文件和目录
import os
print('操作系统类型：os.name:',os.name)
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
# print('详细操作系统类型：os.uname:',os.uname())
# window没有uname()

print('os.environ:\n',os.environ)
print('os.environ.PATH:\n',os.environ.get('PATH'))
print('os.environ.x:\n',os.environ.get('x','default'))


# 查看当前目录的绝对路径:
print(os.path.abspath('.'))
# 创建目录
os.path.join(os.path.abspath('.'),'/io/createFolder')
os.mkdir(os.path.abspath('.')+'/io/createFolder')
time.sleep(1)
os.rmdir(os.path.abspath('.')+'/io/createFolder')

# 拆分路径
print("拆分路径",os.path.split('./io/text.txt'))
# 拆分扩展名
print("拆分扩展名",os.path.splitext('./io/text.txt'))

# 更改名
os.rename('./io/text.txt','./io/text3.txt')
time.sleep(1)
os.rename('./io/text3.txt','./io/text.txt')
# 删除当前目录下文件
# os.remove('./io/text2.txt')

# 复制文件
# shutil模块提供了copyfile()的函数
import shutil
shutil.copyfile('./io/dump.txt','./io/dump Copy.txt')

# 列举目录下所有文件
x = [x for x in os.listdir('.') if os.path.isfile(x)]
print("列举目录下所有文件:",x)
# 列举目录下所有目录
x = [x for x in os.listdir('.') if os.path.isdir(x)]
print("列举目录下所有目录:",x)
# 列举目录下所有.gitignore文件
x = [x for x in os.listdir('.') if os.path.splitext(x)[1] == '.gitignore']
print("列举目录下所有.gitignore文件:",x)


# key=input('请输入您想要查询的关键字\n')

for root,dir,file in os.walk('.'):
    k=False
    for name in file:
        # if key in name:
        print(root,'==>',name)
        # k=True
    if k==True:
        print('-'*50)
