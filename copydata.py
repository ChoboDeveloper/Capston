"""
import os
import shutil
from os import rename,listdir

os.chdir('E:/DownLoad/knives/training_set/Knives')
files = listdir('.')
count = 1
cnt = 10865

for file in files:
    cnt += 1
    if (cnt - 10000) % 5 == 0 :
     oriname = "E:/DownLoad/knives/training_set/Knives/" + str(cnt) + ".bmp"
     newname = "E:/DownLoad/knives/training_set/new/knife_" + str(count) +".jpg"
     shutil.copy2(oriname, newname)
     count += 1
"""


