# -*- coding: utf-8 -*-
"""
@file      :  data_select.py
@Time      :  2022/10/26 11:54
@Software  :  PyCharm
@summary   :  T60、STI_数据提取
@Author    :  Zedong Wu
"""
import os
import pandas as pd
import numpy as np

def process(lst_name):
    xlsx_path = r"C:\Users\17579\Desktop\2022.10.25_数据整理\data\{}\new.xlsx".format(lst_name)
    temp_xlsx = pd.read_excel(xlsx_path)
    lst = []
    for row in range(len(temp_xlsx)):
        if temp_xlsx.iloc[row, 0] == 'T20 [s]':
            config = row - 3
            while not isinstance(temp_xlsx.iloc[config, 0], str):
                config = config - 1
            lst.append(temp_xlsx.iloc[config, :].tolist())
            lst.append(temp_xlsx.iloc[row - 3, :].tolist())
            lst.append(temp_xlsx.iloc[row, :].tolist())  # t20
            lst.append(temp_xlsx.iloc[row + 1, :].tolist())  # t30
            T60 = []
            for i in range(len(temp_xlsx.iloc[row, :])):
                if isinstance(temp_xlsx.iloc[row, :][i], str):
                    T60.append('T60')
                elif isinstance(temp_xlsx.iloc[row, :][i], float):
                    temp_sum = np.add(temp_xlsx.iloc[row, :][i], temp_xlsx.iloc[row + 1, :][i])
                    average = temp_sum / 2
                    T60.append(average)
                else:
                    T60.append(temp_xlsx.iloc[row, :][i])
            lst.append(T60)
        if temp_xlsx.iloc[row, 0] == 'STI male':
            lst.append(temp_xlsx.iloc[row, :].tolist())
            lst.append([])
            lst.append([])

    csv_file = pd.DataFrame(lst)
    save_path = "./Finished_File/{}.csv".format(lst_name)
    csv_file.to_csv(save_path, index=False)

if __name__ == '__main__':
    config_path = r"C:\Users\17579\Desktop\2022.10.25_数据整理\data"
    lst = os.listdir(config_path)
    for i in lst:
        process(i)
