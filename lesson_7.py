#1#

import os
import shutil
from os import path

def save_fold(folder):
    main_f = os.path.join(folder)
    if not os.path.exists(main_f):
        os.mkdir(main_f)
        path.exists('my project')
        destination_path = 'my project'
        shutil.move(folder, destination_path)
    return


save_fold('my_project')
save_fold('mainapp')
save_fold('adminapp')
save_fold('authapp')
save_fold('settings')

#3.
# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или
# «руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку
# templates, например:
# |--my_project
# ...
# |--templates
# | |--mainapp
# | | |--base.html
# | | |--index.html
# | |--authapp
# | |--base.html
# | |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы
# расположены в родительских папках (они играют роль пространств имён); предусмотреть
# возможные исключительные ситуации; это реальная задача, которая решена, например, во
# фреймворке django.

import os
import shutil

my_dir = 'templates'  # save folder
if not os.path.exists(my_dir):
    os.mkdir(my_dir)

folder = r'my_project'  # search folder
files = []

for root, dirs, filenames in os.walk(folder):
    for file in filenames:
        if '.html' in file:
            files.append(os.path.join(root, file))

for path in files:
    folder = os.path.join(my_dir, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder):
        os.mkdir(folder)
    save_path = os.path.join(folder, os.path.basename(path))
    shutil.copy(path, save_path)

#4.
# Написать скрипт, который выводит статистику для заданной папки в виде словаря, где ключи — верхняя граница
# размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках), размер
# которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
import os
my_dir = 'virt'
files = []
for r, d, f in os.walk(my_dir):
    for file in f:
        file_path = os.path.join(r, file)
        files.append(os.stat(file_path).st_size)
max_size = max(files)
i = 1
out_dict = {}
for _ in range(len(str(max_size))):
    i *= 10
    out_dict[i] = 0

for file in files:
    out_dict[10 ** len(str(file))] += 1

print(out_dict)