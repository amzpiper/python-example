import pymysql
import sys


#打开数据库连接
conn = pymysql.connect('39.106.63.189',user='root',passwd='root')
print(conn)
sys.stdout.write("打开数据库连接 \n")
sys.stdout.flush()

#获取游标
cursor=conn.cursor()
print(cursor)
sys.stdout.write("打开数据库连接游标 \n")
sys.stdout.flush()

#创建pythonBD数据库
# cursor.execute('CREATE DATABASE IF NOT EXISTS pythonDB;')
# cursor.close()#先关闭游标
# conn.close()#再关闭数据库连接
# sys.stdout.write("创建pythonBD数据库成功 \n")
# sys.stdout.flush()

conn.select_db('pythonDB')
#创建user表
cursor.execute('drop table if exists user')
sql="""CREATE TABLE IF NOT EXISTS `user` (
	  `id` int NOT NULL AUTO_INCREMENT,
	  `name` varchar(255) NOT NULL,
	  `age` int NOT NULL,
	  PRIMARY KEY (`id`)
	) ENGINE=InnoDB AUTO_INCREMENT=0"""

cursor.execute(sql)
sys.stdout.write("创建数据表成功 \n")
sys.stdout.flush()

# 插入数据
insert=cursor.execute("insert into user values(1,'tom',18)")
sys.stdout.write("添加语句受影响的行数：%s \n" % insert)
sys.stdout.flush()

#另一种插入数据的方式，通过字符串传入值
sql="insert into user values(%s,%s,%s)"
insert=cursor.executemany(sql,[(4,'wen',20),(5,'tom',10),(6,'test',30)])
conn.commit()
sys.stdout.write("添加语句受影响的行数：%s \n" % insert)
sys.stdout.flush()

# 查询
cursor.execute("select * from user;")
while 1:
    res=cursor.fetchone()
    if res is None:
        #表示已经取完结果集
        break
    sys.stdout.write("添加语句受影响的行数：%s \n" % insert)
sys.stdout.flush()

#先关闭游标
cursor.close()
sys.stdout.write("关闭数据库连接 \n")
sys.stdout.flush()
#再关闭数据库连接
conn.close()
sys.stdout.write("关闭数据库连接游标 \n")