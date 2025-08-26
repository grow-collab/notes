import multiprocessing
import os
from time import *

def sing(name,num):
    print('唱歌进程编号:',os.getpid())
    print('唱歌父进程编号:',os.getppid())

    for i in range(num):
        print(f'{name}唱歌...')
        sleep(0.5)


def dance(name,num):
    print('跳舞进程编号:', os.getpid())
    print('跳舞父进程编号:', os.getppid())

    for i in range(num):
        print(f'{name}跳舞...')
        sleep(0.5)

if __name__ == '__main__':
    print('主进程的编号:',os.getpid())
    s1 = multiprocessing.Process(target=sing,args=('朱晓明',3))
    d1 = multiprocessing.Process(target=dance,kwargs={'name':'萧兮','num':5})
    s1.start()
    d1.start()