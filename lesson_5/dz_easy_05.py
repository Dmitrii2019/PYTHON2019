#__author__ = 'Гродзинский Дмитрий Александрович'# Задача-1:
import os
import sys
import shutil
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# dir_create = [i for i in range(1, 10)if os.mkdir(f'dir_{i}')]
# dir_remove = [i for i in range(1, 10)if os.rmdir(f'dir_{i}')]

def dir_create_1(i):
    os.mkdir(f'{i}')

def dir_remove_1(i):
    os.rmdir(f'{i}')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

#1 вариант
def directory():
    for itm in os.listdir():
        print(itm)

# #2 вариант
# print([i for i in os.listdir()])

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

# shutil.copy(sys.argv[0], sys.argv[0] + '.copy.py')
