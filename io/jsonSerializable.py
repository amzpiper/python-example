# json序列化
import json
d = dict(name='宝宝',age=20,score=80)
# dumps()方法返回一个str
j = json.dumps(d,ensure_ascii=True)
print('json序列化:\n',j)

# json反序列化
# 把JSON反序列化为Python对象
d = json.loads(j)
print('json反序列化:\n',j)
print(d['name'])

# JSON标准规定JSON编码是UTF-8


# json写入文件
f = open('./io/json.json','w')
json.dump(d,f)
f.close()

# 读json文件转换为dict
f = open('./io/json.json','r')
d = json.load(f)
f.close()
print(d['name'])


# json进阶-
# 类转换json
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
# 首先被student2dict()函数转换成dict,下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。
print("首先被student2dict()函数转换成dict:",json.dumps(s,default=studentToJson))

# class的实例都有一个__dict__属性，它就是一个dict
print("通用转换:",json.dumps(s,default=lambda obj: obj.__dict__))

# json转换类
def jsonToStu(js):
    return Student(js['name'],js['age'],js['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
stu=json.loads(json_str, object_hook=jsonToStu)
print("json转换类:",stu)

