import glob, os

current_dir = os.path.dirname(os.path.abspath(__file__))

path_data = 'C:/Users/lgpc/Google drive/yolo/darknet'

percentage_test = 10

file_train = open('C:/Users/lgpc/Google drive/yolo/darknet/train.txt', 'w')
file_test = open('C:/Users/lgpc/Google drive/yolo/darknet/test.txt', 'w')

counter = 1
index_test = round(100 / percentage_test)

for pathAndFilename in glob.iglob(os.path.join(path_data,"img/*.jpg")):
    title, ext = os.path.splitext((os.path.basename(pathAndFilename)))
    tmp = pathAndFilename.replace("C:/Users/lgpc/Google drive/yolo/darknet\img\\", "/content/gdrive/My Drive/yolo/darknet/img/")
    pathAndFilename = tmp
    print(pathAndFilename)

    if counter == index_test:
        counter = 1
        file_test.write(str(pathAndFilename) + "\n")
    else:
        file_train.write(str(pathAndFilename) + "\n")
        counter = counter + 1

