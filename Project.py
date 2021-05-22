# import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


ds = pd.read_csv("Dataset.csv")
#출처 : https://www.kaggle.com/mustafaali96/weight-height
h = ds.loc[:,'Height']
w = ds.loc[:,'Weight']
height = []
weight = []
for i in range(0,len(h)) :
    height.append(h[i] * 2.54) # 인치를 cm로 변환
    weight.append(w[i]*0.453592) # 파운드를 kg으로 변환


y = np.array(height)
x = np.array(weight)



n=np.size(x)
b=(n*np.sum(x*y)-(np.sum(x)*np.sum(y)))/(n*np.sum(x**2)-(np.sum(x))**2)
# b= -0.30285714285714288: slope
a=(np.sum(y)-b*np.sum(x))/n
# 0.75714285714285723: intercept

p1=np.polyfit(x,y,1)  # 1: linear  array([-0.30285714,  0.75714286])  slope and intercept
plt.figure(1)
plt.plot(x, y, 'o')
plt.grid()
plt.plot(x, np.polyval(p1,x), 'r-')  # p1 from np.polyfit, plot(x, p1 with polyval
plt.xlabel("Weight(kg)")
plt.ylabel("Height(cm)")
# plt.xlim([25,140])
# plt.ylim([100,210])

plt.show()

