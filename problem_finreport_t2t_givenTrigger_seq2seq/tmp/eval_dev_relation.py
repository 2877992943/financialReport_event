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
import pandas as pdd
lenll=[]
p_num=re.compile('\d+')


event_mention_typ={'m','TIME','trigger','WithIn','company','ORG'}


def make_pair(head,headpos,tail,tailpos,rela):
    return ' '.join([head,str(headpos),tail,str(tailpos),rela])

def calc_precision_recall_f1(yll,predll):
    yll=set(yll)
    predll=set(predll)
    eps=0.000001
    precision = len(yll & predll) / float(eps + len(predll))
    recall =len(yll&predll)/float(eps+len(yll))
    f1=precision*2*recall/(precision+recall+eps)
    return precision,recall,f1




f='output.pkl'

rst=pdd.read_pickle(f)
print ('')
xll_predll,yll=rst
xll,predll=xll_predll

precisionll,recalll,f1ll=[],[],[]

for x1,pred1,y1 in zip(xll,predll,yll):
    print ('')

    #############
    # 找出所有 关系  评估
    ##  先找到 trigger root
    root=None
    rootpos=None
    for wid,pred in enumerate(pred1):
        word=x1[wid]
        if pred=='trigger':
            root=word
            rootpos=wid
            break

    ##### 预测的
    pred_pair_ll = []
    for wid,pred in enumerate(pred1):
        if pred=='trigger':continue
        if pred!='unlabel':
            l=make_pair(root,rootpos,x1[wid],wid,pred)
            pred_pair_ll.append(l)
    ####### 标注的
    label_pair_ll=[]
    for wid,y in enumerate(y1):
        if y=='trigger':continue
        if y!='unlabel':
            l=make_pair(root,rootpos,x1[wid],wid,y)
            label_pair_ll.append(l)

    precision,recall,f1=calc_precision_recall_f1(label_pair_ll,pred_pair_ll)
    precisionll.append(precision)
    recalll.append(recall)
    f1ll.append(f1)

####
print (np.mean(precisionll),np.mean(recalll),np.mean(f1ll))





