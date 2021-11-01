import os
from numpy import *
# 需导入要用到的库文件
import numpy as np  # 数组相关的库
import matplotlib.pyplot as plt  # 绘图库




def plot_curve(filename):
    import pandas as pd     #引入pandas包
    data=pd.read_table(filename
                        ,sep='\t')     #读入txt文件，分隔符为\t
    strain = data["1_ln(V)"].mean()
    s1 = data["1_S[0_0.7_-0.7](0.6_0.6_0.6)"].mean()
    s2 = data["2_S[-0.7_0_0.7](0.6_0.6_0.6)"].mean()
    s3 = data["3_S[0.7_-0.7_0](0.6_0.6_0.6)"].mean()
    s4 = data["4_S[0_-0.7_-0.7](-0.6_-0.6_0.6)"].mean()
    s5 = data["5_S[0.7_0_0.7](-0.6_-0.6_0.6)"].mean()
    s6 = data["6_S[-0.7_0.7_0](-0.6_-0.6_0.6)"].mean()
    s7 = data["7_S[0_-0.7_0.7](0.6_-0.6_-0.6)"].mean()
    s8 = data["8_S[-0.7_0_-0.7](0.6_-0.6_-0.6)"].mean()
    s9 = data["9_S[0.7_0.7_0](0.6_-0.6_-0.6)"].mean()
    s10 = data["10_S[0_0.7_0.7](-0.6_0.6_-0.6)"].mean()
    s11 = data["11_S[0.7_0_-0.7](-0.6_0.6_-0.6)"].mean()
    s12 = data["12_S[-0.7_-0.7_0](-0.6_0.6_-0.6)"].mean()

    schmidlist = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12]
    colorlist = ['r', 'g', 'b', 'y', 'c', 'm', 'k','chocolate','darkmagenta','deeppink','gold','orange']
    for i  in range(len(schmidlist)):
        plt.scatter(strain, schmidlist[i],color=colorlist[i])





if __name__ == '__main__':
    path = "/Users/yangjiyi/master/research/damask/test4/test4/post3/postProc/"  # 文件夹目录
    files = os.listdir(path)
    for file in files:
        filename = path+file
        plot_curve(filename)
    plt.legend(["s1","s2","s3","s4","s5","s6","s7","s8","s9","s10","s11","s12"],bbox_to_anchor=(1,0),loc =3,borderaxespad=0)
    plt.savefig("schmidfactor.jpg")
    plt.show()




