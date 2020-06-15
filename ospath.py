import os
import sys

filepath = 'd:/Shagane/FirstProject/oscarwilde.txt'

#   возвращает нормализированный абсолютный путь (все слеши в одну сторорону и др)
abspath = os.path.abspath(filepath)
print (abspath)

base_name = os.path.basename(filepath)
print(base_name)

#  имя директории 
dir_name = os.path.dirname(filepath)
dir_name_abs = os.path.dirname(abspath)
print(dir_name)
print(dir_name_abs)

print(os.path.exists(filepath))
print(os.path.exists('d:/hahane'))

print(os.path.getsize(filepath))
print(os.path.isabs(filepath))
print(os.path.isfile(filepath), 'file')
print(os.path.isfile('d:/Shagane'), 'file')
print(os.path.isdir(filepath), 'dir')

print('norm path', os.path.normpath(filepath))
print('norm case', os.path.normcase(filepath))
print('rel path', os.path.relpath(filepath, 'd:/'))
print('real path', os.path.realpath(filepath))

print(os.path.split(filepath))

print(os.path.splitdrive(filepath))