import os

num = 0
with open('C:/caffe-project/Ages/label_imagess/Age_label.txt', 'w') as label_txt:
    for root, dirs, files in os.walk('C:/caffe-project/Ages/label_imagess/'):
        for dir in dirs:
            if str(dir) == "01_05":
                num = 0
            elif str(dir) == "06_10":
                num = 1
            elif str(dir) == "11_15":
                num = 2
            elif str(dir) == "16_20":
                num = 3
            elif str(dir) == "21_25":
                num = 4
            elif str(dir) == "26_30":
                num = 5
            elif str(dir) == "31_35":
                num = 6
            elif str(dir) == "36_40":
                num = 7
            elif str(dir) == "41_45":
                num = 8
            elif str(dir) == "46_50":
                num = 9
            elif str(dir) == "51_55":
                num = 10
            elif str(dir) == "56_60":
                num = 11
            elif str(dir) == "61_100":
                num = 12
            n += 1
            for root, dirs, files in os.walk('C:/caffe-project/Ages/label_imagess/' + str(dir)):
                for file in files:
                    image_file = str(dir) + '\\' + str(file)
                    label = image_file + ' ' + str(num) + '\n'
                    label_txt.writelines(label)

print "succeed"

