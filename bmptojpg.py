import os
import shutil
from PIL import Image

count = 1
cnt = 10865

for i in range(3000):
    cnt += 1
    if (cnt - 10000) % 5 == 0 :
     oriname = "E:/DownLoad/knives/training_set/Knives/" + str(cnt) + ".bmp"
     newname = "E:/DownLoad/knives/training_set/new/knife_" + str(count) +".jpg"
     #shutil.copy(oriname, newname)
     im = Image.open(oriname)
     im.save(newname, "JPEG")
     count += 1