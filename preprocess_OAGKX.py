import numpy as np
import os
import ast
from sklearn.model_selection import train_test_split
from nltk.tokenize import TweetTokenizer as TToken
tkz = TToken()

filepath = '/home/edgeai/krishna19039/Datasets/OAGKX/oagkx/oagkx'
outpath =  '/home/edgeai/lakshya19067/Krishna/Datasets/OAGKX'
temp = os.listdir(outpath)
filesloc = os.listdir(filepath)

filesContent = []
try:
    for i in range(len(filesloc)):
        filesContent.append(open(filepath+'/'+filesloc[i]).read())
except:
    itr=0
print('Files Read: ',len(filesContent))
print("Reading Files [",len(filesContent),"]: ", end=' ')
itr = 0
dictionaries = []
for data in filesContent:
    itr+=1
    if itr%1000 == 0:
        print(itr, end = ' ')
    dictionaries+=[ast.literal_eval(dic_str) for dic_str in data.split('\n')[:-1]]

print("\nSplitting Data...")
train_dictionaries, test_dictionaries = train_test_split(dictionaries, test_size=0.2, random_state=97)
train_dictionaries, val_dictionaries = train_test_split(train_dictionaries, test_size=0.25, random_state=97)

print("Preparing train.txt File [",len(train_dictionaries),"]: ",end=' ')
itr=0
train = open(outpath+"/train.txt","a")
for dic in train_dictionaries:
    itr+=1
    if itr%1000 == 0:
        print(itr,end=' ')
    txt = dic['title']+' '+dic['abstract']
    key = dic['keywords'].split(' , ')
    tokens = tkz.tokenize(txt)
    flag=False
    for token in tokens:
        if token in key:
            if flag:
                train.write(token+'\tI-Key\n')
            else:
                train.write(token+'\tB-Key\n')
                flag=True
        else:
            train.write(token+'\tO\n')
            flag=False
train.close()

print("\nPreparing test.txt File [",len(test_dictionaries),"]: ",end=' ')
itr=0
test = open(outpath+"/test.txt","a")
for dic in test_dictionaries:
    itr+=1
    if itr%1000 == 0:
        print(itr,end=' ')
    txt = dic['title']+' '+dic['abstract']
    key = dic['keywords'].split(' , ')
    tokens = tkz.tokenize(txt)
    flag=False
    for token in tokens:
        if token in key:
            if flag:
                test.write(token+'\tI-Key\n')
            else:
                test.write(token+'\tB-Key\n')
                flag=True
        else:
            test.write(token+'\tO\n')
            flag=False
test.close()

print("\nPreparing val.txt File [",len(val_dictionaries),"]: ",end=' ')
itr=0
val = open(outpath+"/val.txt","a")
for dic in val_dictionaries:
    itr+=1
    if itr%1000 == 0:
        print(itr,end=' ')
    txt = dic['title']+' '+dic['abstract']
    key = dic['keywords'].split(' , ')
    tokens = tkz.tokenize(txt)
    flag=False
    for token in tokens:
        if token in key:
            if flag:
                val.write(token+'\tI-Key\n')
            else:
                val.write(token+'\tB-Key\n')
                flag=True
        else:
            val.write(token+'\tO\n')
            flag=False
val.close()
print()
