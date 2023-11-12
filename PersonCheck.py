import pandas as pd
import os
from settings import *

try:
    namelist = pd.read_excel(namelist_path)
except:
    input('错误：无法加载到班级名单，请检查软件高级参数中的【namelist_path】！程序已终止运行，按下回车以退出。')
    exit
if mode != 0:
    if mode != 4:
        if mode != 8:
            input('错误：作业命名方式设置不正确，请检查软件高级参数中的【mode】！程序已终止运行，按下回车以退出。')
            exit
if sex != 0:
    if sex != 1:
        if sex != 2:
            input('错误：性别过滤模式设置不正确，请检查软件高级参数中的【sex】！程序已终止运行，按下回车以退出。')
            exit

if sex == 1:
    namelist = namelist[namelist['性别'] == '男']
if sex == 2:
    namelist = namelist[namelist['性别'] == '女']

inputOK = False
print('请拖动作业文件夹到此处，确保路径不包含空格且显示路径正确后回车。')
while inputOK == False:
    filepath = input()
    try:
        if filepath == '':
            raise
        for i in filepath:
            if i == ' ':
                raise
    except:
        print('路径格式错误，请重试！')
        continue
    inputOK = True
title = filepath.split('微信收集')
title = title[1]
title = title.split('\\')[1]
OKnameRAW = os.listdir(filepath)
OKname = []
for i in OKnameRAW:
    i = i.split('.')[0]
    OKname.append(i)
del i

if mode == 0:
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
        input('检测结果：交齐了！')
    else:
        print('检测结果：以下'+str(len(badlist))+'位同学未提交！')
        print(badlist)
        input()

if mode == 4 or 8:
    name = []
    for i in namelist['姓名']:
        name.append(str(i))
    del i
    numlist = []
    for i in namelist['学号']:
        numlist.append(str(i))
    del i
    OKnameFIX = []
    for i in OKname:
        i = i[-3:]
        OKnameFIX.append(i)
    del i
    badlist = []
    need = 0
    while need < len(numlist):
        if (numlist[need] in OKnameFIX):
            pass
        else:
            badlist.append(name[need])
        need = need + 1
    os.system('cls')
    print('筛查目标：'+title)
    if badlist == []:
        input('检测结果：交齐了！')
    else:
        print('检测结果：以下'+str(len(badlist))+'位同学未提交！')
        print('、'.join(badlist))
        input()
