import os
from numpy import *
# 需导入要用到的库文件
import numpy as np  # 数组相关的库
import matplotlib.pyplot as plt  # 绘图库
import pandas as pd

path = "/Users/yangjiyi/master/Data-Ni3Al-SG-tensile-test/"
files = ["Ni3Al17-A1.txt","Ni3Al19-7.txt","Ni3Al25011B1.txt"]
for file in files:
    filename = path+file
    data = pd.read_table(filename
                                 , sep='\t')
    strain = data["true_strain"]
    stress = data["true_stress"]
    min = stress.min()
    max = stress.max()
    plt.scatter(strain,stress,label= file)

    plt.legend()
    plt.show()
#plt.savefig("/Users/yangjiyi/master/research/damask/experiment.jpg")
#plt.show()