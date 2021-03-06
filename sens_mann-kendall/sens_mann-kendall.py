import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def mk(x):
    s=0
    length=len(x)
    for m in range(0,length-1):
      for n in range(m+1,length):
          if x[n]>x[m]:
              s=s+1
          elif x[n]==x[m]:
              s=s+0
          else:
              s=s-1
    
    vars=length*(length-1)*(2*length+5)/18
    if s>0:
        zc=(s-1)/math.sqrt(vars)
    elif s==0:
        zc=0
    else:
        zc=(s+1)/math.sqrt(vars)
        
    zc1=abs(zc)
    
    ndash=length*(length-1)//2
    slope1=np.zeros(ndash)
    m=0
    for k in range(0,length-1):
        for j  in range(k+1,length):
            slope1[m]=(x[j]-x[k])/(j-k)
            m=m+1
        
    slope=np.median(slope1)
    
    return (slope,zc1)


def CUFK(x):
    sk=0
    length=len(x)
    list = []
    list.append(0.0)
    print("ufk: 0.0")
    for i in range(2, length):
        for j in range(1, i):
            if x[i]>x[j]:
                sk+=1
            else:
                sk+=0
        esk=float(i*(i-1.0)/4.0)
        varsk=float(i*(i-1.0)*(2.0*i+5.0)/72.0)
        ufk=(sk-esk)/math.sqrt(varsk)
        print("ufk: ",ufk)
        list.append(ufk)

    return list

def CUBK(x):
    sk=0
    length=len(x)
    list = []
    for i in range(1, length):
        x[i]=x[length-i]

    for i in range(2, length):
        for j in range(1,i):
            if x[i]>x[j]:
                sk+=1
            else:
                sk+=0
        esk=float(i*(i-1.0)/4.0)
        varsk=float(i*(i-1.0)*(2.0*i+5.0)/72.0)
        ubk=0-(sk-esk)/math.sqrt(varsk)
        
        list.append(ubk)
        print("ubk", ubk)

    return list


def LoadCSVData(path):
    list=[]
    data = pd.read_csv(path,usecols=[0])
    for index,row in data.iterrows():
        if index > 22 and index < 61:
            print(row['h'])
            list.append(row['h'])

    return list

list_data=LoadCSVData('projects/sens_mann-kendall/data/data.csv')

(slope,zc1)=mk(list_data)

list_ufk=CUFK(list_data)
list_ubk=CUBK(list_data)

print("slope: ", slope)
print("Z: ", zc1)

plt.plot(list_ubk,'r', label='ubk')
plt.plot(list_ufk,'b',label='ufk')
plt.legend(bbox_to_anchor=[0.3, 1])  
plt.grid()  
plt.show()

