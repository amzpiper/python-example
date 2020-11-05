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

# 数值类型
print(10_000_000_000+0.00001)
print("r\\\t")
print('''
123
''')
a=123                               # 整数
print(not a>5 or not 5>1)
a="123"                             # 字符串
print(a)

# 编码问题,pyton3.0- 使用Unicode编码
a = ord('A')                        # ord把字符转化为整数
print(a)
a = chr(65)                         # chr把
print(a.encode('ascii'))            # encode()方法可以编码为指定的bytes
x = b'ABC'                          # byte类型
x = b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8', errors='ignore')     # 把bytes变为str
print(len('abc'))

# 格式化输出 "%d" % (12)
print('Hello %s,my age is %d' % ('apple', 23))          # %
print("Hello {0},my age is {1}".format("apple", 23))    # format
print("Hello {0},my age is {1}".format("apple", 23))    # f-string
age = 23
name = "apple"
print(f"Hello {age:.2f},my age is {name}")

# List
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

# tuple
classmate = ('Me','You', 'He', 'She')
class2 = (1,['Me','You', 'He', 'She'])
class2[1][0] = 'x'
class2[1][1] = 'y'
print(class2)

# 条件判断