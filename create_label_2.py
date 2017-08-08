import os

with open('C:/caffe-project/Ages/label_images/labels/Age_1_5.txt','w') as label_txt:
    for root, dirs, files in os.walk('C:/caffe-project/Ages/label_images/labels/1_5/'):
        for dir in dirs:         
            for root, dirs, files in os.walk('C:/caffe-project/Ages/label_images/labels/1_5/' + str(dir)):
                for file in files:
                    image_file = str(dir) + '\\' + str(file)
                    label = image_file[:-4] + '\n'
                    label_txt.writelines(label)
                    
print "succeed"
