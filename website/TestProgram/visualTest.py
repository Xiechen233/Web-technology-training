import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import csv
import random
# 设置matplotlib正常显示中文和负号
mpl.rcParams['font.sans-serif']=['simhei']
mpl.rcParams['axes.unicode_minus']=False     

#读取数据
no=[]
point=[]
with open("全站周排行top100.csv",encoding="utf-8") as f:
    reader=csv.reader(f)
    next(reader)
    for row in reader:
        data=row[2]
        if data[len(data)-1]=='万':
            data=int(float(data[:-1])*10000)
            point.append(data)
            no.append(row[0])
# 生成画布
plt.figure(figsize=(100,50), dpi=20)
x=range(len(no))
plt.bar(x,point,color='darkorange')
darkblue='#994D52'
darkred='#E6B450'
plt.xticks(range(1,100),fontsize=120,color=darkred)
plt.yticks(fontsize=100,color=darkred)
plt.xlabel('排名---→',fontsize=250,color=darkblue)
plt.ylabel('播放量',fontsize=200,color=darkblue)
plt.savefig('全站排名test.jpg')