# financialReport_event
 
依赖
tensor2tensor==1.15.4

生成数据 t2t_data_gen.py

训练 t2t_trainer_yr.py

预测  t2t_decoder_test_v04.py

event extraction

原始数据1条 ：2018年 实 现 总资产 81万元 ， 总负债 45万元 。   


1,第一个样本要预测的关系  {trigger:总资产,arguments:{ arg1:81万元 , 关系:value }; {arg2:time , 关系:time}   #arg =argument

```input :TIME , 实 现 triggerRoot mEntity , trigger mEntity 。```

```y:     time u  u u    trigger    value  u   u       u    u     ```#u=unlabel

2,第二个样本要预测的关系  {trigger:总负债,arguments:{ arg1:45万元 , 关系:value }; {arg2:time , 关系:time}

```input :TIME , 实 现 trigger mEntity , triggerRoot mEntity 。```

```y :    time u  u u    u      u      u   trigger   value   u```


# 评估

事件评估基本单位 [head, head-position, tail,tail-position, relation]

precision,recall,f1-score分别问0.9915694729623408 0.9907699879155678 0.9905141807678854

