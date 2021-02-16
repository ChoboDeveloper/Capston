import os
from os import rename,listdir

os.chdir('E:/DownLoad/person')
files = listdir('.')
count = 1

for file in files:
    new_name = 'person_' + str(count) + '.jpg'
    rename(file,new_name)
    count += 1
