# 一个进程可以有多个线程

# 多个核执行不同的进程

# 在一段时间内，交替执行多个任务
import multiprocessing

import time

def sing():
    for i in range(1,4):
        print('唱歌...')
        time.sleep(0.5)

def dance():
    for i in range(3):
        print('跳舞...')
        time.sleep(0.5)

if __name__ == '__main__':
    start_time = time.time()
    sing()
    dance()
    print(f'执行时间:{time.time()-start_time}')

# 使用多线程实现
# def sing():
#     for i in range(1,4):
#         print('唱歌...')
#         time.sleep(0.5)
#
# def dance():
#     for i in range(3):
#         print('跳舞...')
#         time.sleep(0.5)
#
# if __name__ == '__main__':
#     start_time = time.time()
#     s1 = multiprocessing.Process(target=sing)
#     d1 = multiprocessing.Process(target=dance)
#     s1.start()
#     d1.start()
#     s1.join()
#     d1.join()
#     print(f'执行时间:{time.time()-start_time}')