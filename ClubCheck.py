from settings import *
import pandas as pd
import os

try:
    namelist = pd.read_excel(clublist_path)
    chatlist = open(wechat_cache_path,encoding='utf-8')
except:
    input('错误：无法加载到社团成员名单或微信接龙缓存文本文件，请检查软件高级参数中的【clublist_path】和【wechat_cache_path】！程序已终止运行，按下回车以退出。')
    exit
title = input('请输入本次签到的收集日期。')+'科技社团签到'
ChatRAW = chatlist.readlines()
OKname = []
for i in range(0,len(ChatRAW),1):
    name = ChatRAW[i]
    name = name.split(' ')
    name = name[0]
    name = name.split('\n')
    name = name[0]
    OKname.append(name)
del i
badnamelist = []
badclasslist = []
for need in namelist['姓名']:
    if (need in OKname):
        pass
    else:
        badindex = namelist[namelist['姓名'] == need].index
        badline = namelist.iloc[badindex]
        print(badline)
        badnamelist.append(badline['姓名'].array[0])
        badclasslist.append(badline['班级'].array[0])
print(badnamelist)
print(badclasslist)
os.system('cls')
baddf = pd.DataFrame({'班级':badclasslist,'姓名':badnamelist})
baddf.to_excel(title+'缺席名单.xlsx',index=None)
print('筛查目标：'+title)
if badnamelist == []:
    input('检测结果：全员到社！')
else:
    print('检测结果：以下'+str(len(badnamelist))+'位同学未到社！')
    print('、'.join(badnamelist))
    input()
