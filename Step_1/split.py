import os
import csv
import argparse
import shutil

import numpy as np
parser = argparse.ArgumentParser()
#创建解析器
#ArgumentParser 对象包含将命令行解析成 Python 数据类型所需的全部信息。
#path = r"C:\Users\17579\Desktop\新建文件夹\TAE_Train\Data_Aug\Step_1\test_1.csv"

parser.add_argument("--csv_file",default=r"C:\Users\17579\Desktop\新建文件夹\TAE_Train\Data_Aug\Step_1\T2000_Wav.csv",type=str)
parser.add_argument("--split_key",default="T60 AHM:",type=str)
parser.add_argument("--freq_num",default="11",type=str)

parser.add_argument("--split_internal",default=0.1,type=float)
parser.add_argument('--input_dir',default=None,type=str)
parser.add_argument("--output_dir",default="./output_test",type=str)

if __name__ == "__main__":
    args = parser.parse_args()
    with open(args.csv_file,'r') as f:
        f_csv = csv.reader(f)
        key_index = None
        headers = next(f_csv)
        for head_str_i in range(len(headers)):
            if headers[head_str_i] == args.split_key:
                key_index = head_str_i

        data_dict = {}
        for row in f_csv:
            if str(row[9])  == args.freq_num:
                key = round(float(row[key_index]),1)
                value = row
            else:
                continue

        min_key = min(data_dict.keys())
        max_key = max(data_dict.keys())
        c = 0
        for key in np.arange(min_key,args.split_internal,max_key):
            save_dir = os.path.join(args.output_dir,"split_%d" %(c))
            c+=1
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            values = data_dict[key]
            for value in values:
                scene_name = value[7]
                room_name = value[3]
                src_path = os.path.join(args.input_dir,scene_name,room_name + ".wav")
                dst_path = os.path.join(save_dir,room_name + ".wav")
                shutil.copy(src_path,dst_path)




