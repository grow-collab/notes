import multiprocessing
import time


def sing(name, num):
    for i in range(num):
        print(f'{name}唱歌...')
        time.sleep(0.5)


def dance(name, num):
    for i in range(num):
        print(f'{name}跳舞...')
        time.sleep(0.5)


if __name__ == '__main__':
    s1 = multiprocessing.Process(target=sing, args=('朱小明', 3))
    d1 = multiprocessing.Process(target=dance, kwargs={'name': '娃哈哈', 'num': 3})
    d1.start()
    s1.start()
