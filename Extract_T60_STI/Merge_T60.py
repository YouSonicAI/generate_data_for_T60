# -*- coding: utf-8 -*-
"""
@file      :  data_select.py
@Time      :  2022/11/8 13:59
@Software  :  PyCharm
@summary   :  将不同的T60的值放到表格中
@Author    :  Zedong Wu
"""

import os
import csv
import pandas as pd
import numpy


path = "./Openair_STI_T60/arthur-sykes-rymer-auditorium-university-york.csv"
room = []
lst_31 = []
lst_63 = []
lst_125 = []
lst_250 = []
lst_500 = []
lst_1000 = []
lst_2000 = []
lst_4000 = []
lst_8000 = []
lst_16000 = []

header = ["Mic config:", "Room:", "Room decode:", "Room Config:",

          "Channel:", "FB T60:", "Mean T60:", "FB DRR:", "Mean DRR:",
          # 25.11
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:",
          # 31.6
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:",
          # 39.8
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:",
          # 50.11
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:",
          # 63.09
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:",
          # 79.43
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:",
          # 100
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:",
          # 125
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:",
          # 160
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:",
          # 199
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:",
          # 251.1
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:",
          # 316
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:",
          # 389
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:",
          # 501
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:",
          # 630
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:",
          # 794
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:",
          # 1000
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:",
          # 1258
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:",
          # 1584
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:",
          # 1995
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:",
          # 2511
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:",
          # 3162
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:",
          # 3981
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:",
          # 5011
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:",
          # 6309
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:",
          # 7943
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:",
          # 10000
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:",
          # 12589
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:",
          # 15848
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:",
          # 19952
          "Freq:", "T60:", "Mean T60:", "DRR:", "Mean DRR:", ]




if __name__ == '__main__':
    temp_csv = pd.read_csv(path)
    for row in range(len(temp_csv)):
        if temp_csv.iloc[row, 0] == 'T60':
            room.append(temp_csv.iloc[row - 4, 0])
            lst_31.append(temp_csv.iloc[row, 2])
            lst_63.append(temp_csv.iloc[row, 3])
            lst_125.append(temp_csv.iloc[row, 4])
            lst_250.append(temp_csv.iloc[row, 5])
            lst_500.append(temp_csv.iloc[row, 6])
            lst_1000.append(temp_csv.iloc[row, 7])
            lst_2000.append(temp_csv.iloc[row, 8])
            lst_4000.append(temp_csv.iloc[row, 9])
            lst_8000.append(temp_csv.iloc[row, 10])
            lst_16000.append(temp_csv.iloc[row, 11])

    # 记得每次换路径的时候，改room[0]
    room[0] = 's1r2_0_1_1'
    num = len(room)

    room_config = ['b-format'] * num
    # mic_config也需要修改
    mic_config = [path.split("/")[2].split(".")[0]] * num
    channel = [1] * num
    FB_T60 = [0] * num
    FB_DRR = [0] * num
    DRR = [0] * num
    Mean_DRR = [0] * num
    T60 = [0] * num

    new_lst_31 = [round(float(i), 2) for i in lst_31]
    new_lst_63 = [round(float(i), 2) for i in lst_63]
    new_lst_125 = [round(float(i), 2) for i in lst_125]
    new_lst_250 = [round(float(i), 2) for i in lst_250]
    new_lst_500 = [round(float(i), 2) for i in lst_500]
    new_lst_1000 = [round(float(i), 2) for i in lst_1000]
    new_lst_2000 = [round(float(i), 2) for i in lst_2000]
    new_lst_4000 = [round(float(i), 2) for i in lst_4000]
    new_lst_8000 = [round(float(i), 2) for i in lst_8000]
    new_lst_16000 = [round(float(i), 2) for i in lst_16000]

    freq_25 = [25.11886] * num
    freq_31 = [31.6227766] * num
    freq_40 = [39.81072] * num
    freq_50 = [50.11872] * num
    freq_63 = [63.09573] * num
    freq_80 = [79.43282] * num
    freq_100 = [100] * num
    freq_125 = [125.8925] * num
    freq_160 = [158.4893] * num
    freq_200 = [199.5262] * num
    freq_250 = [251.1886] * num
    freq_316 = [316.2278] * num
    freq_400 = [398.1072] * num
    freq_500 = [501.1872] * num
    freq_630 = [630.9573] * num
    freq_800 = [794.3282] * num
    freq_1000 = [1000] * num
    freq_1258 = [1258.925] * num
    freq_1600 = [1584.893] * num
    freq_2000 = [1995.262] * num
    freq_2500 = [2511.886] * num
    freq_3162 = [3162.278] * num
    freq_4000 = [3981.072] * num
    freq_5000 = [5011.872] * num
    freq_6309 = [6309.573] * num
    freq_8000 = [7943.282] * num
    freq_10000 = [10000] * num
    freq_12500 = [12589.25] * num
    freq_16000 = [15848.93] * num
    freq_20000 = [19952.62] * num
    with open('test23.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i in range(len(mic_config)):
            content = [mic_config[i], room[i], room[i], room_config[i], channel[i], FB_T60[i],
                       FB_T60[i], FB_DRR[i], Mean_DRR[i],
                       # 25.11
                       freq_25[i], T60[i], T60[i], FB_DRR[i], Mean_DRR[i],
                       # 31.6
                       freq_31[i], new_lst_31[i], new_lst_31[i], DRR[i], DRR[i],
                       # 39.8
                       freq_40[i], T60[i], T60[i], DRR[i], DRR[i],
                       # 50.11
                       freq_50[i], T60[i], T60[i], DRR[i], DRR[i],
                       #  63.09
                       freq_63[i], new_lst_63[i], new_lst_63[i], DRR[i], DRR[i],
                       # 79.43
                       freq_80[i], T60[i], T60[i], DRR[i], DRR[i],
                       # 100
                       freq_100[i], T60[i], T60[i], DRR[i], DRR[i],
                       # 125
                       freq_125[i], new_lst_125[i], new_lst_125[i], DRR[i], DRR[i],
                       # 160
                       freq_160[i], T60[i], T60[i], DRR[i], DRR[i],
                       # 199
                       freq_200[i], T60[i], T60[i], DRR[i], DRR[i],
                       # 251.1
                       freq_250[i], new_lst_250[i], new_lst_250[i], DRR[i], DRR[i],
                       #  316
                       freq_316[i], T60[i], T60[i], DRR[i], DRR[i],
                       # 389
                       freq_400[i], T60[i], T60[i], DRR[i], DRR[i],
                       # 501
                       freq_500[i], new_lst_500[i], new_lst_500[i], DRR[i], DRR[i],
                       # 630
                       freq_630[i], T60[i], T60[i], DRR[i], DRR[i],
                       # 794
                       freq_800[i], T60[i], T60[i], DRR[i], DRR[i],
                       # 1000
                       freq_1000[i], new_lst_1000[i], new_lst_1000[i], DRR[i], DRR[i],
                       # 1258
                       freq_1258[i], T60[i], T60[i], DRR[i], DRR[i],
                       # 1584
                       freq_1600[i], T60[i], T60[i], DRR[i], DRR[i],
                       # 1995
                       freq_2000[i], new_lst_2000[i], new_lst_2000[i], DRR[i], DRR[i],
                       # 2511
                       freq_2500[i], T60[i], T60[i], DRR[i], DRR[i],
                       # 3162
                       freq_3162[i], T60[i], T60[i], DRR[i], DRR[i],
                       # 3981
                       freq_4000[i], new_lst_4000[i], new_lst_4000[i], DRR[i], DRR[i],
                       # 5011
                       freq_5000[i], T60[i], T60[i], DRR[i], DRR[i],
                       # 6309
                       freq_6309[i], T60[i], T60[i], DRR[i], DRR[i],
                       # 7943
                       freq_8000[i], new_lst_8000[i], new_lst_8000[i], DRR[i], DRR[i],
                       # 10000
                       freq_10000[i], T60[i], T60[i], DRR[i], DRR[i],
                       #  12589
                       freq_12500[i], T60[i], T60[i], DRR[i], DRR[i],
                       # 15848
                       freq_16000[i], new_lst_16000[i], new_lst_16000[i], DRR[i], DRR[i],
                       # 19952
                       freq_20000[i], T60[i], T60[i], DRR[i], DRR[i], ]
            writer.writerow(content)








