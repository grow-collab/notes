import os
import multiprocessing


def copy_file(file_name, source_dir, dest_dir):
    # 1.拼接源文件路径和目标文件路径
    source_path = source_dir + '/' + file_name
    dest_path = dest_dir + '/' + file_name
    # 2.打开源文件夹和目标文件
    with open(source_path, 'rb') as source_file:
        with open(dest_path, 'wb') as dest_file:
            while True:
                data = source_file.read()
                if data:
                    dest_file.write(data)
                else:
                    break


if __name__ == '__main__':
    # 1.定义源文件夹和目标文件夹
    source_dir = '../源文件'
    dest_dir = '../目标文件夹'

    # 2.创建目标文件夹
    if not os.path.exists('../目标文件夹'):
        os.mkdir('../目标文件夹')

    # 3.读取源文件夹中的文件列表
    file_list = os.listdir(source_dir)

    # 4.读取文件列表实现拷贝
    for file_name in file_list:
        # 多进程实现文件拷贝操作
        sub_process = multiprocessing.Process(target=copy_file, args=(file_name, source_dir, dest_dir))
        sub_process.start()
