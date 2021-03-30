# pickle序列化
# 写序列化
import pickle
d = dict(name='Bob',age=20,score=80)
f = open('./io/dump.txt','wb')
pickle.dump(d,f)
f.close()

# 反序列化
f = open('./io/dump.txt','rb')
d = pickle.load(f)
f.close()
print('pickle:\n',d)
