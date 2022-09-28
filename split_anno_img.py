#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 将一个文件夹下图片按比例分在三个文件夹下
import os
import random
import shutil
from shutil import copy2
datadir_normal = "./images"
annopath="./Annotations" 

all_data = os.listdir(datadir_normal)#（图片文件夹）
num_all_data = len(all_data)
print( "num_all_data: " + str(num_all_data) )
index_list = list(range(num_all_data))
#print(index_list)
random.shuffle(index_list)
num = 0

trainDir = "./images/train2017/"#（将训练集放在这个文件夹下）
if not os.path.exists(trainDir):
    os.mkdir(trainDir)
        
validDir = './images/val2017/'#（将验证集放在这个文件夹下）
if not os.path.exists(validDir):
    os.mkdir(validDir)
        
testDir = './images/test2017/'#（将测试集放在这个文件夹下）        
if not os.path.exists(testDir):
    os.mkdir(testDir)

trainannoDir = "./Annotations/train2017/"#（将训练集放在这个文件夹下）
if not os.path.exists(trainannoDir):
    os.mkdir(trainannoDir)
        
validannoDir = './Annotations/val2017/'#（将验证集放在这个文件夹下）
if not os.path.exists(validannoDir):
    os.mkdir(validannoDir)
        
testannoDir = './Annotations/test2017/'#（将测试集放在这个文件夹下）        
if not os.path.exists(testannoDir):
    os.mkdir(testannoDir)
       
for i in index_list:
    imgName = os.path.join(datadir_normal, all_data[i])
    anno=all_data[i].split(".")[0]+".xml"
    annoName=os.path.join(annopath, anno)
    
    if num < num_all_data*0.6:
        #print(str(fileName))
        copy2(imgName, trainDir)
        
        
        copy2(annoName,trainannoDir)
    
    elif num>num_all_data*0.6 and num < num_all_data*0.8:
        #print(str(fileName))
        copy2(imgName, validDir)
        
        copy2(annoName,validannoDir)
    else:
        copy2(imgName, testDir)
        
        copy2(annoName,testannoDir)
    num += 1
