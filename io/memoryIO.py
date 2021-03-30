#读写内存
from io import StringIO
from io import BytesIO

# 字符串数据
f = StringIO()
f.write('Hello')
print(f.getvalue())

f = StringIO("Hello!\nHi!\nGoodBye")
while True:
    r = f.readline()
    if r == "":
        break
    print(r.strip())        


# 二进制数据
f = BytesIO()
f.write('中文'.encode("utf-8"))
print(f.getvalue())
print(f.getvalue().decode("utf-8"))

b = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(b.read())
