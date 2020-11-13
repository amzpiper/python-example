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
# 19.4.1.map
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素
def f(x):
    return x*x
r = map(f,[1,2,3,4,5,6])
r = list(r)
print(r)
# 结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
# 19.4.2.reduce
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def cheng(x,y):
    return x*y
print("reduce(cheng,['1','2','3','4','5']):",reduce(cheng,[1,2,3,4,5]))
# 19.5.filter
# 删除了偶数，只保留奇数
print(list(filter(lambda x : x % 2 == 1,[1,2,3,4,5,6,7,8,9,10])))
# 用filter求素数:埃氏筛选法
# 1.生成器，并且是一个无限序列
def odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
# 2.筛选函数
def not_divisible(n):
    return lambda x : x % n > 0
# 生成器，不断返回下一个素数
def prims():
    yield 2
    it = odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(not_divisible(n),it)
# 打印1000以内的函数
for n in prims():
    if n < 10:
        print(n)
    else:
        break
# 19.5.sorted
list = sorted([34,1,31,-23,0])
print(list)
list = sorted([34,1,31,-23,0],key=abs)
print(list)
list = sorted(['Zeb','ord','abe','C'],key=str.upper)
print(list)
# 19.6.返回函数
# 不需要立刻求和，而是在后面的代码中,返回求和的函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for x in args:
            ax += x
        return ax
    return sum
f = lazy_sum(1,2,3,4,5,6,7,8,9,10)
print(f)
print(f())
# 返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print("f1():",f1(),"f2():",f2(),"f3():",f3())
# 一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值
def count():
    fs = []
    def f(j):
        def g():
             return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()
print("f1():",f1(),"f2():",f2(),"f3():",f3())

# 装饰器
# 1.decorator就是一个返回函数的高阶函数
def log(func):
    def wrapper():
        print('call %s():' % func.__name__)
        func()
        print('call %s():' % func.__name__)
        # return "func"
    return wrapper
# 2.把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
@log
def now():
    print("2015-3-25")

now()


# 19.7. 偏函数
# 假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去
def int2(x, base=2):
    return int(x, base)
# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2
import functools
int2 = functools.partial(int, base=2)
print(int2('1000000'))
# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。

# 20.模块

' a test module '

__author__ = 'Michael Liao'

name = "gyh"
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
# 在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了,这也是一种非常有用的代码封装和抽象的方法

# 20.1.安装第三方模块
# 装第三方模块，是通过包管理工具pip完成的。
# 如果你正在使用Mac或Linux，安装pip本身这个步骤就可以跳过了。
# 如果你正在使用Windows，请参考安装Python一节的内容，确保安装时勾选了pip和Add python.exe to Path。
# 注意：Mac或Linux上有可能并存Python 3.x和Python 2.x，因此对应的pip命令是pip3。
# 一般来说，第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第三方库，必须先知道该库的名称，
# 可以在官网或者pypi上搜索，比如Pillow的名称叫Pillow，因此，安装Pillow的命令就是：
# pip install Pillow
# 如果我们要添加自己的搜索目录，有两种方法：
# 一是直接修改sys.path，添加要搜索的目录：
# >>> import sys
# >>> sys.path.append('/Users/michael/my_py_scripts')
# 这种方法是在运行时修改，运行结束后失效。
# 第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。

# 21.面向对象编程
# 面向过程的程序的方式
std1 = {'name': 'Mi','score' :98}
std2 = {'name':'Bob','score' :81}
def print_score(std):
    print("%s:%s" % (std['name'],std['score']))
# 面向对象的方式
class Student(object):
    def __init__(self, name, score):
        # 21.1访问限制
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s : %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self , score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

# 调用对象对应的关联函数
bart = Student('ban',59)
lisa = Student('Lisa',87)
bart.print_score()
lisa.print_score()
# 实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
# print(lisa.name, lisa.get_grade())
# print(bart.name, bart.get_grade())
# 类中定义的函数只有一点不同，就是第一个参数永远是实例变量self
# 在Python中，变量名类似__xxx__的，是特殊变量，特殊变量是可以直接访问的，不是private变量
# 以一个下划线开头的实例变量名,照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
# 仍然可以通过_Student__name来访问__name变量
# 强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。
# 21.2继承和多态
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    def run(self):
        print('Dog is running...')

dog = Dog()
dog.run()
isinstance(dog,Animal)
isinstance(dog,Dog)

def _run(animal):
    animal.run()
_run(Animal())
_run(Dog())

# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
class Timer(object):
    def run(self):
        print('Start...')

_run(Timer())

# 20.3获取对象信息
# 拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
# 20.3.1使用type()
type(123)
# 它返回对应的Class类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：
if type(123) == type(456):
    print(True)
# 判断一个对象是否是函数怎么办？
import types
def fn():
    pass
if type(fn) == types.FunctionType:
    print(True)

# 20.3.2对于class的继承关系来说
# 使用isinstance()
isinstance(dog, Dog) and isinstance(dog, Animal)

# 20.3.3使用dir()
print(dir('ABC'))
# 如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的

# 20.3.4.仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr(),可以直接操作一个对象的状态
hasattr(dog, '__name') # 有属性'x'吗？
setattr(dog, '__name', '19') # 设置一个属性'y'
getattr(dog, '__name') # 获取属性'y'
# 试图获取不存在的属性，会抛出AttributeError的错误
# 可以传入一个default参数，如果属性不存在，就返回默认值
getattr(dog,'__name',404)

# 20.4.实例属性和类属性
# 由于Python是动态语言，根据类创建的实例可以任意绑定属性。
# 给实例绑定属性的方法是通过实例变量，或者通过self变量
# 如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：
class Stu(object):
    name = "Stu"
# 属性虽然归类所有，但类的所有实例都可以访问到
s = Stu()
print(s.name)

# 20.5.面向对象高级编程
# 20.5.1.使用__slots__
# 我们可以给该实例绑定任何属性和方法
# 1.给实例绑定一个属性：
s = Stu()
s.name2 = "M2"
print(s.name2)
# 2.给实例绑定一个方法：
def set_name2(self, name2):
    self.name2 = name2

from types import MethodType
s.set_name2 = MethodType(set_name2,s)
s.set_name2('M3')
print(s.name2)
# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：

# 3.给所有实例都绑定方法，可以给class绑定方法
Stu.set_name2 = set_name2
s2 = Stu()
s2.set_name2('2M3')
print(s2.name2)

# 4.为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class Student2(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

# 20.5.2.使用@property
# 绑定属性时，如果我们直接把属性暴露出去,，没办法检查参数
# s = Student()
# s.score = 9999

class Stu2(object):
    @property
    def score(self):
        return self._score
    # @property本身又创建了另一个装饰器@score.setter
    # 把一个setter方法变成属性赋值
    def score(self,value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 0:
            raise ValueError('score must between 0 ~ 100')
        self._score = value
s2 = Stu2()
s2.score = 60   # 实际转化为s.set_score(60)
print(s2.score) # 实际转化为s.get_score()

class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth
# 上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。
# @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

# 20.5.3多重继承
# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。
# 让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。
# MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，
# 我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。

# 20.6.定制类
# 20.6.1.__repr__ , __str__
class Stu3(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Stu3 object name is %s' % self.name

    # 偷懒写法
    __repr__ = __str__

s3 = Stu3('MMM')
print(Stu3('MMM'))
print(s3)
# 两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串
# 20.6.2.__iter__
# 一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a
for n in Fib():
    print(n)
# 20.6.3.__getitem__
# Fib()[5]
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a+b

            return a
        # 实现切片
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b

            return L

f = Fib()
print(f[1])
print(f[2])
print(f[3])
print(f[0:5])

# 20.6.4.__getattr__
class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda : 29

        # 让class只响应特定的几个属性
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

st = Student()
print(st.score)
print(st.age())
# 注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None
# 只有在没有找到属性的情况下，才调用__getattr__

# 如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
# 利用完全动态的__getattr__，我们可以写出一个链式调用：
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.itemline.list)
# 如果我们能写出这样的链式调用：
# Chain().users('michael').repos
# 就可以非常方便地调用API了。有兴趣的童鞋可以试试写出来。

# 20.6.5.__call__
# 只需要定义一个__call__()方法，就可以直接对实例进行调用
class Student4(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print("My name is %s " % self.name)

s4 = Student4("YuHang")
s4()
# __call__()还可以定义参数

# 20.7.使用枚举类
# from enum import Enum
# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# for name,member in Month.__member__.items():
#     print(name, '=>', member, ',', member.value)

# @unique装饰器可以帮助我们检查保证没有重复值。
# 需要更精确地控制枚举类型，可以从Enum派生出自定义类：
from enum import Enum, unique
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# 访问这些枚举类型可以有若干种方法：
day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)

# 20.8.使用元类
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
print(type(Stu()))
print(s)
# <class '__main__.Stu'>
# <__main__.Stu object at 0x000001A207071908>
#
# type()
# type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，通过type()函数创建出Hello类
def fun(self, name = 'value'):
    print("Hello %s ." % name)
# 创建Hello class
Hello = type("Hello", (object,), dict(hello=fun))
h = Hello()
h.hello()
# 创建一个class对象，type()函数依次传入3个参数：
# 1).class的名称；
# 2).继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3).class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
#
# metaclass:直译为元类，简单的解释就是：
# 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
# 有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass：
class MyList(list, metaclass=ListMetaclass):
    pass
# 当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建
# 在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
# __new__()方法接收到的参数依次是：
# 1当前准备创建的类的对象；
# 2类的名字；
# 3类继承的父类集合；
# 4类的方法集合。

# 测试一下MyList是否可以调用add()方法：
ml = MyList()
ml.add(1)
print(ml)

# 要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。
# 让我们来尝试编写一个ORM框架。
# 编写底层模块的第一步，就是先把调用接口写出来。
# 比如，使用者如果使用这个ORM框架，想定义一个User类来操作对应的数据库表User，我们期待他写出这样的代码：
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()
# 其中，父类Model和属性类型StringField、IntegerField是由ORM框架提供的，剩下的魔术方法比如save()全部由metaclass自动完成。
# 虽然metaclass的编写会比较复杂，但ORM的使用者用起来却异常简单。
# 实现该ORM
# 首先来定义Field类，它负责保存数据库表的字段名和字段类型：
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)
# 在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等：
class StringField(Field):
    pass