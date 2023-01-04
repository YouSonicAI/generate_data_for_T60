import os
import csv
import pandas as pd
import numpy
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




if __name__ == '__main__':
    path = "./Openair_STI_T60/arthur-sykes-rymer-auditorium-university-york.csv"
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
    room[0] = 's1r2_0_1_1'
    num = len(room)

    room_config = ['b-format'] * num
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
    headLine = {"Mic config:": mic_config,
                "Room:": room,
                "Room decode:": room,
                "Room Config:": room_config,
                "Channel:": channel,
                "FB T60:": FB_T60,
                "Mean T60:": FB_T60,
                "FB DRR:": FB_DRR,
                "Mean DRR:": Mean_DRR,

                # 25.11
                "Feq:": freq_25,
                "T60:": T60,
                "Mean T60:": T60,
                "DRR:": FB_DRR,
                "Mean DRR:": Mean_DRR,

                # 31.6
                "Freq:": freq_31,
                "T60:": new_lst_31,
                "Mean T60:": new_lst_31,
                "DRR:": DRR,
                "Mean DRR:": DRR,
                # 39.8
                "Freq:": freq_40,
                "T60:": T60,
                "Mean T60:": T60,
                "DRR:": DRR,
                "Mean DRR:": DRR,
                # 50.11
                "Freq:": freq_50,
                "T60:": T60,
                "Mean T60:": T60,
                "DRR:": DRR,
                "Mean DRR:": DRR,
                # 63.09
                "Freq:": freq_63,
                "T60:": new_lst_63,
                "Mean T60:": new_lst_63,
                "DRR:": DRR,
                "Mean DRR:": DRR,
                # 79.43
                "Freq:": freq_80,
                "T60:": T60,
                "Mean T60:": T60,
                "DRR:": DRR,
                "Mean DRR:": DRR,
                # 100
                "Freq:": freq_100,
                "T60:": T60,
                "Mean T60:": T60,
                "DRR:": DRR,
                "Mean DRR:": DRR,
                # 125
                "Freq:": freq_125,
                "T60:": new_lst_125,
                "Mean T60:": new_lst_125,
                "DRR:": DRR,
                "Mean DRR:": DRR,
                # 160
                "Freq:": freq_160,
                "T60:": T60,
                "Mean T60:": T60,
                "DRR:": DRR,
                "Mean DRR:": DRR,

                # 199
                "Freq:": freq_200,
                "T60:": T60,
                "Mean T60:": T60,
                "DRR:": DRR,
                "Mean DRR:": DRR,
                # 251.1
                "Freq:": freq_250,
                "T60:": new_lst_250,
                "Mean T60:": new_lst_250,
                "DRR:": DRR,
                "Mean DRR:": DRR,
                # 316
                "Freq:": freq_316,
                "T60:": T60,
                "Mean T60:": T60,
                "DRR:": DRR,
                "Mean DRR:": DRR,

                # 389
                "Freq:": freq_400,
                "T60:": T60,
                "Mean T60:": T60,
                "DRR:": DRR,
                "Mean DRR:": DRR,
                # 501
                "Freq:": freq_500,
                "T60:": new_lst_500,
                "Mean T60:": new_lst_500,
                "DRR:": DRR,
                "Mean DRR:": DRR,
                # 630
                "Freq:": freq_630,
                "T60:": T60,
                "Mean T60:": T60,
                "DRR:": DRR,
                "Mean DRR:": DRR,
                # 794
                "Freq:": freq_800,
                "T60:": T60,
                "Mean T60:": T60,
                "DRR:": DRR,
                "Mean DRR:": DRR,
                # 1000
                "Freq:": freq_1000,
                "T60:": new_lst_1000,
                "Mean T60:": new_lst_1000,
                "DRR:": DRR,
                "Mean DRR:": DRR,
                # 1258
                "Freq:": freq_1258,
                "T60:": T60,
                "Mean T60:": T60,
                "DRR:": DRR,
                "Mean DRR:": DRR,
                # 1584
                "Freq:": freq_1600,
                "T60:": T60,
                "Mean T60:": T60,
                "DRR:": DRR,
                "Mean DRR:": DRR,
                # 1995
                "Freq:": freq_2000,
                "T60:": new_lst_2000,
                "Mean T60:": new_lst_2000,
                "DRR:": DRR,
                "Mean DRR:": DRR,
                # 2511
                "Freq:": freq_2500,
                "T60:": T60,
                "Mean T60:": T60,
                "DRR:": DRR,
                "Mean DRR:": DRR,
                # 3162
                "Freq:": freq_3162,
                "T60:": T60,
                "Mean T60:": T60,
                "DRR:": DRR,
                "Mean DRR:": DRR,
                # 3981
                "Freq:": freq_4000,
                "T60:": new_lst_4000,
                "Mean T60:": new_lst_4000,
                "DRR:": DRR,
                "Mean DRR:": DRR,
                # 5011
                "Freq:": freq_5000,
                "T60:": T60,
                "Mean T60:": T60,
                "DRR:": DRR,
                "Mean DRR:": DRR,
                # 6309
                "Freq:": freq_6309,
                "T60:": T60,
                "Mean T60:": T60,
                "DRR:": DRR,
                "Mean DRR:": DRR,
                # 7943
                "Freq:": freq_8000,
                "T60:": new_lst_8000,
                "Mean T60:": new_lst_8000,
                "DRR:": DRR,
                "Mean DRR:": DRR,
                # 10000
                "Freq:": freq_10000,
                "T60:": T60,
                "Mean T60:": T60,
                "DRR:": DRR,
                "Mean DRR:": DRR,
                # 12589
                "Freq:": freq_12500,
                "T60:": T60,
                "Mean T60:": T60,
                "DRR:": DRR,
                "Mean DRR:": DRR,
                # 15848
                "Freq:": freq_16000,
                "T60:": new_lst_16000,
                "Mean T60:": new_lst_16000,
                "DRR:": DRR,
                "Mean DRR:": DRR,
                # 19952
                "Freq:": freq_20000,
                "T60:": T60,
                "Mean T60:": T60,
                "DRR:": DRR,
                "Mean DRR:": DRR,

                }
    file = pd.DataFrame(headLine)
    file.to_csv('./t60.csv')

