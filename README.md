# financialReport_event
 
依赖
tensor2tensor==1.15.4

生成数据 t2t_data_gen.py

训练 t2t_trainer_yr.py

预测  t2t_decoder_test_v04.py

event extraction

原始数据1条 ：
2018年实现总资产81万元，总负债45万元
# 第一个样本要预测的关系  [trigger:总资产  arg1:81万元  关系:value ; arg2:time  关系:time]   #arg =argument

input :TIME , 实 现 triggerRoot mEntity , trigger mEntity 。
y:     time u  u u    trigger    value  u   u       u    u     #u=unlabel

# 第二个样本要预测的关系   [trigger:总负债 arg1 45万元 关系value; arg2:time 关系:time]

input :TIME , 实 现 trigger mEntity , triggerRoot mEntity 。
y :    time u  u u    u      u      u   trigger   value   u
