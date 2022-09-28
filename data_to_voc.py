####将labeling标记后的图像按比例制成voc数据集.得先建立文件夹。
import os
import random

trainval_percent = 0.2    #trainval占整个数据集的百分比，剩下部分就是test所占百分比
test_percent = 0.5     #test占trainval的百分比，剩下部分就是val所占百分比
xmlfilepath = r'E:\yolov5-tree\VOCdevkit\VOC2007\Annotations'
txtsavepath = r'E:\yolov5-tree\VOCdevkit\VOC2007\ImageSets\Main'
total_xml = os.listdir(xmlfilepath)
print (total_xml)
num = len(total_xml)
list = range(num)
#总体取出10%的个数（测试集与验证集个数）
tv = int(num * trainval_percent)
#从10%中再取去90%用作验证集的个数
tr = int(tv * test_percent)
#trainval：包括测试集与验证集
trainval = random.sample(list, tv)#从list中随机获取tv个元素，作为一个片断返回
train = random.sample(trainval, tr)
print(train)

ftrainval = open(r'E:\yolov5-tree\VOCdevkit\VOC2007\ImageSets\Main\trainval.txt', 'w')
print (ftrainval)
ftest = open(r'E:\yolov5-tree\VOCdevkit\VOC2007\ImageSets\Main\test.txt', 'w')
ftrain = open(r'E:\yolov5-tree\VOCdevkit\VOC2007\ImageSets\Main\train.txt', 'w')
fval = open(r'E:\yolov5-tree\VOCdevkit\VOC2007\ImageSets\Main\val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'#也就是去除‘.xml’这四个字符


    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftest.write(name)
        else:
            fval.write(name)
    else:
        ftrain.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
