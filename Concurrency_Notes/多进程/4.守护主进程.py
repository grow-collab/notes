from time import *
import multiprocessing

def work():
    for i in range(5):
        print('正在工作中...')
        sleep(0.5)

if __name__ == '__main__':
    wp = multiprocessing.Process(target=work)
    wp.daemon = True # 守护主进程，主进程结束，程序结束
    wp.start()
    # wp.join() # 进程阻塞
    print('主进程结束')