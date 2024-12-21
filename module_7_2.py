import os
import  time

directory = os.getcwd()
for root, dirs, files in os.walk(directory):

    dir_name = root.split('/')
    dir_name = dir_name[len(dir_name)-1]
    if root == directory or dir_name.rfind('module') >= 0:
        for file in files:
            filepath = os.path.join(root,file)
            filetime = os.path.getmtime(filepath)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize(filepath)
            parent_dir = os.path.dirname(filepath)
            print(f'\033[33m°\033[0m \033[4mОбнаружен файл\033[0m: \033[32m\033[1m{file},\033[0m  \033[4mПуть\033[0m:{filepath},')
            print(f'   |  \033[4mРазмер\033[0m: {filesize} байт, \033[4mВремя изменения\033[0m: {formatted_time},')
            print(f'   |  \033[4mРодительская директория\033[0m: \033[3m{parent_dir}\033[0m')
