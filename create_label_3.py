import shutil

num = 0

f = open('C:/caffe-project/Ages/label/flist_IMDB_FULL_Age_label.txt', 'r')

line = f.readline()
while line != "":
    image = line[0:7] + "/" + line[8:31] + ".bmp"
    a = line[-3:-1]
    i = int(a)
    if i >= 1 and i <= 5:
        num += 1
        shutil.copy("C:/caffe-project/Ages/NormFace/" + image, "C:/caffe-project/Ages/label_image/1_5/")

    line = f.readline()

f.close()

print num
