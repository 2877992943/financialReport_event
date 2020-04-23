####################
# 给定 trigger 预测 这个trigger的属性 subject time value ratio..
##  原始句子 company time trigger1 m m m, org time trigger2 m m m
## 想分别预测 trigger1 的相关 attribute:company time m m m  ,
# trigger2和相关的属性 都作为unlabel
## 输入  company time triggerRoot   m     m     m,     org   time    trigger   m       m       m
## 输出  subject time  trigger   value  value value  unlabel unlabel unlabel unlabel unlabel unlabel

import json
import re
import sys
import os
import copy
import numpy as np

lenll=[]



p_num=re.compile('\d+')







f='./train.json'

writer=open('tmp.txt','w')
reader=open(f)
n=0
for line in reader.readlines():

    ll=json.loads(line)
    print ('')
    line=' '.join([d['char'] for d in ll])
    print (line)
    writer.write(line+'\n')
    n+=1
    if n>5:break