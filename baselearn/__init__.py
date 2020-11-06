#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

# # 1.print - hello world
# print("hello-world")
# print("1","2","3")
#
# # 2.input()
# name = input()
# print(name)
#
# name = input("please enter your name:")
# print("hello",name,".")
#

# 3.数值类型
print(10_000_000_000+0.00001)
print("r\\\t")
print('''
123
''')
a=123                               # 整数
print(not a>5 or not 5>1)
a="123"                             # 字符串
print(a)

# 4.编码问题,pyton3.0- 使用Unicode编码
a = ord('A')                        # ord把字符转化为整数
print(a)
a = chr(65)                         # chr把
print(a.encode('ascii'))            # encode()方法可以编码为指定的bytes
x = b'ABC'                          # byte类型
x = b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8', errors='ignore')     # 把bytes变为str
print(len('abc'))

# 5.格式化输出 "%d" % (12)
print('Hello %s,my age is %d' % ('apple', 23))          # %
print("Hello {0},my age is {1}".format("apple", 23))    # format
print("Hello {0},my age is {1}".format("apple", 23))    # f-string
age = 23
name = "apple"
print(f"Hello {age:.2f},my age is {name}")

# 6.List
classmate = ['Me','You', 'He', 'She']
print(classmate)
print(len(classmate))
print(classmate[0])
print(classmate[-1])
classmate.append("his")
classmate.insert(2,"his2")
classmate.pop()
classmate.pop(1)
print(classmate)

# 7.tuple
classmate = ('Me','You', 'He', 'She')
class2 = (1,['Me','You', 'He', 'She'])
class2[1][0] = 'x'
class2[1][1] = 'y'
print(class2)

# 8.条件判断
age = 20
if age > 20:
    print("you are old")
else:
    print("you are young")

age = 10
if age > 20:
    print("young")
elif age < 20:
    print("too young")
else:
    print("too old")

# 9.input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成
age = "200"
birth = int(age)
if birth == 200:
    print("number")

# 10.循环 for x in array:
classmate = ('Me','You', 'He', 'She')
for mate in classmate:
    print(mate)

sumNum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sumNum += x
print(sumNum)

for x in range(101):
    sumNum += x
print(sumNum)

# 11.while
sumNum = 0
n = 99
while n > 0:
    sumNum += n
    n -= 2
print(sumNum)

# 12.dict字典,dictionary=map,键值对储存,具有极高的查询速度
classmate = {"me":100, "you":100, "she":100}
classmate["he"] = 1000
print(classmate["he"])
# dict就是第二种实现方式，给定一个名字，比如'Michael'，
# dict在内部就可以直接计算出Michael对应的存放成绩的“页码”，
# 也就是95这个数字存放的内存地址，直接取出来，所以速度非常快。
# in判断key是否存在 / get("",-1)
if "he" in classmate:
    print("he is my classmate")
    print(f"he srocs is {classmate.get('he')}")

classmate.pop("he")

# 和list比较，dict有以下几个特点：
#
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 而list相反：
#
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。

# 13.set,创建一个set，需要提供一个list作为输入集合
s = set([1,2,3,1,2,3])
s.add(4)
s.remove(4)
print(s)

# 13.1交集并集
s1 = ([1,2,3])
s2 = ([2,3,4])
# s1 & s2
# s1 | s2

# 14.函数
def my_abs( xx ):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if xx >= 0:
        return xx
    else:
        return -xx

print(my_abs(12))

# 14.1 空函数
def nop():
    pass

# 14.2 返回多个数值, 返回值是一个tuple
import math
def move(x1, y1, step, angle=0):
    nx = x1 + step * math.cos(angle)
    ny = y1 - step * math.sin(angle)
    return nx, ny
x2, y2 = move(100,100,60,math.pi / 6)
print(x2, y2)

# Python的函数定义非常简单，但灵活度却非常大。
# 除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，
# 使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。
def power(x3):
    return x3 * x3

# 14.3 默认参数,n = 2 默认参数:降低调用函数的难度
def powerN(x4, n1 = 2):
    ss = 1
    while n1 > 0:
        n1 = n1 - 1
        ss = ss * x4
    return s

# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L = None):
    if L is None:
        L = []
    L.append("END")
    return L

# 14.4 可变参数
# 要定义出这个函数，我们必须确定输入的参数。
# 由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下：
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
# 但是调用的时候，需要先组装出一个list或tuple：

# 利用可变参数，调用函数的方式可以简化成这样：calc(1, 2, 3)
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum
# 在函数内部，参数numbers接收到的是一个tuple
# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
num1 = [1,2,3]
calc(*num1)

# 14.5 关键字参数
def person(name,age,**city):
    print("name:",name,"age:",age,"city:",city)
# 可以只传入必选参数name,age,或传入任意数量的city,这些关键字参数在函数内部自动组装为一个dict
person("yuhang",12,gender="M",job = "Enginer")
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

# 14.6 命名关键字
# 要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。
def person(name,age,*,city,job):
    print(name,age,city,job)
# 函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*
# 命名关键字参数必须传入参数名
def person(name,age,*args,city,job):
    print(name,age,args,city,job)

# 命名关键字参数可以有缺省值，从而简化调用：由于命名关键字参数city具有默认值，调用时，可不传入city参数：
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
person("name",12,job="Engineer")

# !特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数

# 参数组合
# 可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# 比如定义一个函数，包含上述若干种参数：
def farg(a,b,c=0,*args,**kw):
    print(a,b,c,args,kw)
def farg2(a,b,c=0,*,d,**kw):
    print(a,b,c,d,kw)

farg(1,2)
farg(1,3,4, 5,6,7, x=99,y=100)
farg2(1,2,4, d=2, x=100,y=200)

# 通过一个tuple和dict，你也可以调用上述函数：
args = (1,2,3,4,5)
kw = {'d':99,'x':"#"}
farg(*args,**kw)

# 14.7 递归函数
def a(x):
    if x==1:
        return 1
    else:
        return x * a(x-1)
print(a(5))
# 计算机中，函数调用是通过栈（stack）这种数据结构实现的
# 递归调用的次数过多，会导致栈溢出
# print(a(1000))

# 解决递归调用栈溢出的方法是通过尾递归优化
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
# 这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
# 上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。
# 要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中
def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num-1,num * product)
def fact(num):
    return fact_iter(num,1)
print(fact(100))
# 多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出.

# 15.切片
# 经常取指定索引范围的操作，用循环十分繁琐
L = ["1","2","3","4","5"]
L = list(range(101))
print(L[0:10])
print(L[10:20])
print(L[:20:2])
print(L[::10])
print(L[:])
print(L[-10:])
print('ABCDEFG'[:3])

# 15.迭代
# 在Python中，迭代是通过for ... in来完成的，Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()
# 同时迭代key和value，可以用for k, v in d.items()

# 通过collections模块的Iterable类型判断，判断一个对象是可迭代对象
from collections.abc import Iterable
flag = isinstance('abc', Iterable)
print(flag)
# 转化为有索引下标方式进行遍历
for i,value in enumerate(["A","B","C"]):
    print(i,value)

# 16.列表生成式
list(range(100))
# 生成的元素x * x放到前面，后面跟for循环，后面还可以加上if判断
L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)
# 还可以使用两层循环，可以生成全排列：
L = [x + y for x in 'ABC' for y in 'XYZ']
print(L)

L = [x if x % 2 == 0 else -x for x in range(1,11)]
print(L)

# 17.生成器Generator
# 列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢
# 一边循环一边计算的机制，称为生成器：generator
# 第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
G = (x for x in range(100))
for x in G:
    print(x)

# 17.1.斐波拉契数列:列表生成式写不出来，但是，用函数把它打印出来却很容易
def fib(max):
    n,a,b = 0,0,1
    while n<max:
        print("b:",b)
        a,b = b, a+b
        n = n + 1
    return 'done'
fib(6)

# 要把fib函数变成generator，只需要把print(b)改为yield b就可以了
# 函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b = b, a+b
        n += 1
    return 'done'
fib(6)

# for循环拿不到generator的return语句返回值，必须使用stopIteration错误，返回值包含在stopIterator的value中
g = fib(6)
while True:
    try:
        x = next(g)
        print("g:",x)
    except StopIteration as e:
        print("Generator return value:",e.value)
        break

# 18.Iterable and Iterator
from collections.abc import Iterable
# isinstance 来判断对象是否是Iterable对象
# 可以直接作用于for循环的对象统称为可迭代对象：Iterable。
# isinstance 检测 list
print("是否是Iterable对象")
print("检测 list：",isinstance([],Iterable))
# isinstance 检测 dict
print("检测 dict：",isinstance({},Iterable))
# isinstance 检测 tuple
print("检测 tuple：",isinstance((1,),Iterable))
# isinstance 检测 string
print("检测 string：",isinstance('abc',Iterable))
# isinstance 检测 生成器
print("检测 生成器：",isinstance((x for x in range(101)),Iterable))
# isinstance 检测 set
print("检测 set：",isinstance(([]),Iterable))


from collections.abc import Iterator
# isinstance 来判断对象是否是Iterator对象
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# isinstance 检测 list
print("是否是Iterable对象")
print("检测 list：",isinstance([],Iterator))
# isinstance 检测 dict
print("检测 dict：",isinstance({},Iterator))
# isinstance 检测 tuple
print("检测 tuple：",isinstance((1,),Iterator))
# isinstance 检测 string
print("检测 string：",isinstance('abc',Iterator))
# isinstance 检测 生成器
print("检测 生成器：",isinstance((x for x in range(101)),Iterator))
# isinstance 检测 set
print("检测 set：",isinstance(([]),Iterator))

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
# 为什么list、dict、str等数据类型不是Iterator？
#
# 这是因为Python的Iterator对象表示的是一个数据流，
# Iterator对象可以被next()函数调用并不断返回下一个数据，
# 直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，
# 但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，
# 所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。


# 19.高阶函数
# 19.1.变量可以指向函数,把函数本身赋值给变量
my_abs = abs
print(my_abs(-10))
# 19.2.函数名也是变量,函数名其实就是指向函数的变量,把abs指向其他对象
# abs = 10
# abs(-10)
# 要让修改abs变量的指向在其它模块也生效，要用import builtins; builtins.abs = 10
# 19.3.传入函数
# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x,y,f):
    return f(x)+f(y)
sum = add(-10,-10,abs)
print(sum)
# 19.4.map/reduce
# Python内建了map()和reduce()函数



