import threading  # 线程模块
from time import *


def sing():
    for i in range(3):
        print('正在唱歌...')
        sleep(0.5)


def dance():
    for i in range(3):
        print('正在跳舞...')
        sleep(0.5)


if __name__ == '__main__':
    # 创建线程任务
    s1 = threading.Thread(target=sing)
    d1 = threading.Thread(target=dance)
    # 启动线程
    s1.start()
    d1.start()
