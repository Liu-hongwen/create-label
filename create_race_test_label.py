import os

num_A = 1
num_W = 1
num_B = 1
flags = 0
a = 0
w = 1
b = 2

with open('C:/caffe-project/VGG-Fcae/labels/test.txt','w') as test_txt:
    for root,dirs,files in os.walk('C:/FaceAttribute/DeepID1015RGB/'):
        for dir in dirs[::-1]:
            
            f = open("C:/FaceAttribute/Deep1015ID_Gender_Race_Total_CLAID.txt", "r")
            line = f.readline()
            while line != "":
                s = line[:12]
                if s == dir:
                    flag = line[15]
                    break
                line = f.readline()
            f.close()
            
            for root,dirs,files in os.walk('C:/FaceAttribute/DeepID1015RGB/' + str(dir)):
                
                for file in files:
                    
                    if flag == "A":
                        if num_A <= 10000:
                            image_file = str(dir) + '\\' + str(file)
                            label = image_file + ' ' + str(a) + '\n'
                            test_txt.writelines(label)                        
                            num_A += 1
                    elif flag == "W":
                        if num_W <= 10000:
                            image_file = str(dir) + '\\' + str(file)
                            label = image_file + ' ' + str(w) + '\n'
                            test_txt.writelines(label)                        
                            num_W += 1
                    elif flag == "B":
                        if num_B <= 10000:
                            image_file = str(dir) + '\\' + str(file)
                            label = image_file + ' ' + str(b) + '\n'
                            test_txt.writelines(label)                        
                            num_B += 1
                                               
                    if num_A == 10000 and num_W == 10000 and num_B == 10000:
                        flags = 1
                        break
                        
                if flags == 1:
                    break
                    
            if flags == 1:
                    break
                    
        if flags == 1:
                    break
                
print(num_A)  
print(num_W) 
print(num_B) 
print("succeed!")

