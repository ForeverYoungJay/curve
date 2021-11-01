import os
from numpy import *
# 需导入要用到的库文件
import numpy as np  # 数组相关的库
import matplotlib.pyplot as plt  # 绘图库


def plot_curve_ratio(filename):
    import pandas as pd     #引入pandas包
    data=pd.read_table(filename
                        ,sep='\t')     #读入txt文件，分隔符为\t
    stress11 = data["1_Cauchy"].mean()
    strain = data["1_ln(V)"].mean()
    rssco = []
    rsslist = ["1_resolvedstress_slip",
               "2_resolvedstress_slip",
               "3_resolvedstress_slip",
               "4_resolvedstress_slip",
               "5_resolvedstress_slip",
               "6_resolvedstress_slip",
               "7_resolvedstress_slip",
               "8_resolvedstress_slip",
               "9_resolvedstress_slip",
               "10_resolvedstress_slip",
               "11_resolvedstress_slip",
               "12_resolvedstress_slip"]
    for rssi in rsslist:
        rss = data[rssi].mean()
        rssco.append(rss)

    colorlist = ['r', 'g', 'b', 'y', 'c', 'm', 'k', 'chocolate', 'darkmagenta', 'deeppink', 'gold', 'orange']
    for i in range(len(rssco)):
        plt.subplot(1, 2, 1)
        plt.xlabel("strain")
        plt.ylabel("RSS/Cauchy")
        plt.scatter(strain,abs(rssco[i]/stress11), color=colorlist[i])




def delete_lines(filename):
    fin = open(filename, 'r')
    a = fin.readlines()
    count = 0
    for row in a:
        first = row.split("\t")[0]
        if first == "inc":
            break
        else:
            count += 1
            fout = open(filename, 'w')
            b = ''.join(a[count:])  # count为前N行
            fout.write(b)

def plot_curve_from_addschmid(filename):
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
        plt.subplot(1, 2, 2)
        plt.xlabel("strain")
        plt.ylabel("schimidfactor")
        plt.scatter(strain, schmidlist[i],color=colorlist[i])


if __name__ == '__main__':

    sample = ["17A1","197","250","17A1-2","197-2","250-2"]
    for sm in sample:
        path = f"/Users/yangjiyi/master/research/damask/{sm}/postProc/"  # 文件夹目录
        files = os.listdir(path)
        fig = plt.figure(figsize=(30, 10))
        for file in files:
            filename = path+file
            delete_lines(filename)
            plot_curve_ratio(filename)
            plot_curve_from_addschmid(filename)

        plt.legend(["s1","s2","s3","s4","s5","s6","s7","s8","s9","s10","s11","s12"],bbox_to_anchor=(1,0),loc =3,borderaxespad=0)
        plt.savefig(f"/Users/yangjiyi/master/research/damask/{sm}/schmidfactor.jpg")
        plt.show()
