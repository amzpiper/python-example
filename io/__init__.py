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

#读写内存
from io import StringIO
from io import BytesIO

f = StringIO()
f.write('Hello')
print(f.getvalue())

b = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(b.read())

#操作文件和目录
import os
print('os.name:',os.name)
# print('os.uname:',os.uname())
print('os.environ:\n',os.environ)
print('os.environ.PATH:\n',os.environ.get('PATH'))

# 绝对路径
print(os.path.abspath(''))

# 添加/删除文件夹
# os.mkdir('./io/testDir')
# os.rmdir('./io/testDir')

# 拆分路径
os.path.splitext('./io/text.txt')

os.rename('./io/text.txt','./io/text3.txt')
os.rename('./io/text3.txt','./io/text.txt')

# 写序列化
import pickle
d = dict(name='Bob',age=20,score=80)
f = open('./io/dump.txt','wb')
pickle.dump(d,f)
f.close()

# 读序列化
f = open('./io/dump.txt','rb')
d = pickle.load(f)
f.close()
print('pickle:\n',d)

# json序列化
import json
d = dict(name='bob',age=20,score=80)
print(d['name'])
j = json.dumps(d,ensure_ascii=True)
print('json:\n',j)
d = json.loads(j)
print(d['name'])

# 写
f = open('./io/json.json','w')
json.dump(d,f)
f.close()

# 读
f = open('./io/json.json','r')
d = json.load(f)
f.close()
print(d['name'])

# json进阶-类转换json
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
s = Student('aoa',30,100)

# 设计一个转化函数
def studentToJson(stu):
    return {
        'name': stu.name,
        'age': stu.age,
        'score': stu.score
    }
# 首先被student2dict()函数转换成dict
print(json.dumps(s,default=studentToJson))
# 通用转换
print(json.dumps(s,default=lambda obj: obj.__dict__))

# json转换类
def jsonToStu(js):
    return Student(js['name'],js['age'],js['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=jsonToStu))

