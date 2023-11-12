from settings import *
import pandas as pd
import os

try:
    namelist = pd.read_excel(namelist_path)
    chatlist = open(wechat_cache_path,encoding='utf-8')
except:
    input('错误：无法加载到班级名单或微信接龙缓存文本文件，请检查软件高级参数中的【namelist_path】和【wechat_cache_path】！程序已终止运行，按下回车以退出。')
    exit
title = input('请输入需要筛选的接龙的主题：')
ChatRAW = chatlist.readlines()
OKname = []
for i in range(2,len(ChatRAW),1):
    name = ChatRAW[i]
    name = name.split('. ')
    name = name[1]
    name = name.split(' ')
    name = name[0]
    OKname.append(name)
del i
namelist = namelist['姓名']
badlist = []
for need in namelist:
    if (need in OKname):
        pass
    else:
        badlist.append(need)
os.system('cls')
print('筛查目标：'+title)
if badlist == []:
    input('检测结果：回复齐了！')
else:
    print('检测结果：以下'+str(len(badlist))+'位同学未回复！')
    print('、'.join(badlist))
    input()