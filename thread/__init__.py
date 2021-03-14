
import os

print('Press (%s) start...' % os.getpid())

# unix
# pid = os.fork()
pid = -1
if pid == 0 :
    print('I am child')
else:
    print('I am (%s) just create a child process (%s)' % (os.getpid(), pid))

# windows
from multiprocessing import Process

#子进程执行的代码
def child_run(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    count=0
    while count<100:
        count = count+1
        print('Child.count:',count)

if __name__=='__main__':
    print('Parent process (%s) start...' % os.getpid())
    p = Process(target=child_run, args=('test',))
    print('Child will start...')
    p.start()
    p.join()

    count=0
    while count<100:
        count = count+1
        print('Parent.count:',count)
    
    print('Child process end.')

# 进程池Pool
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))
if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(9)
    for i in range(10):
        p.apply_async(long_time_task, args=(i,))
    print('Wait all subprocess done.')

    p.close()
    p.join()

    print('END')


import subprocess
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)


# 进程通信
from multiprocessing import Process, Queue
import os,time,random


# 写数据进程
def write(q):
    print('Process to Write:%s' % os.getpid)
    for value in ['a','b','c']:
        print('Put %s in queue.' % value)
        p.put(value)
        time.sleep(random.random()*3)

# 读数据进程
def read(q):
    print('Process to read : %s.' % os.getpid)
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

# 主进程
if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()

    # 启动子进程pw，写入:
    pw.join()
    # 启动子进程pr，读取:
    pr.join()

    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
    
