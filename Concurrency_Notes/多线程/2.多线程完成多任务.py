import threading
from time import *


def demo():
    for i in range(5):
        print('我是子线程')
        sleep(0.5)


if __name__ == '__main__':
    # 创建线程任务
    d1 = threading.Thread(target=demo)
    d1.daemon = True
    # 执行线程任务
    d1.start()
    # d1.join() # 等待子线程执行结束之后，主线程继续执行，有点像程序阻塞
    print('我是主线程')
