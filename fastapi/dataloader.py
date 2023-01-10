# -*- coding: utf-8 -*-
"""
@file      :  dataloader.py
@Time      :  2022/11/22 12:44
@Software  :  PyCharm
@summary   :
@Author    :  Bajian Xiang
"""
import numpy as np
import torch
from torch.utils.data import DataLoader, Dataset
from wav2spec import All_Frequency_Spec, imageListTransform
import splweighting
from webrtc_vad import get_utter_time
from snr import wada_snr

def imageTransform(temp_image):
    temp_image = temp_image.unsqueeze(0)
    return temp_image


class DatasetSlice(Dataset):

    def __init__(self, waves, fs, overlap, ifVad=True):
        self.waves = waves
        self.fs = fs
        self.overlap = overlap
        self.chunk_length = 4
        self.total_cut_num = int(((len(self.waves)/self.fs)-self.chunk_length) // self.overlap)
        # for vad
        self.ifVad = ifVad
        self.snr_threshold = 8
        self.cut_slice_portion = 0.75
        self.cut_slice_time = int(self.fs * 4 * self.cut_slice_portion) # 3s
        self.cat_head = False

    def __len__(self):
        return self.total_cut_num

    def __getitem__(self, idx):
        start = idx * self.fs
        end = start + self.chunk_length * self.fs
        audio_chunk = self.waves[start: end]

        if self.ifVad:
            snr = wada_snr(audio_chunk)
            if snr >= self.snr_threshold:
                utter_time_3_head = get_utter_time(audio_chunk[:self.cut_slice_time], self.fs)
                utter_time_1_tail = get_utter_time(audio_chunk[self.cut_slice_time:], self.fs)

                if utter_time_3_head + utter_time_1_tail < 2:
                    if utter_time_1_tail < self.chunk_length * (1 - self.cut_slice_portion) * 0.5:
                        return idx
                    else:
                        if isinstance(self.cat_head, bool):
                            return idx
                        else:
                            audio_chunk = np.append(self.cat_head, audio_chunk[self.cut_slice_time:])
                else:
                    if utter_time_1_tail < self.chunk_length * (1 - self.cut_slice_portion) * 0.5 and idx != 0:
                        return idx

        chunk_a_weighting = splweighting.weight_signal(audio_chunk, self.fs)
        chunk_result, _, _ = All_Frequency_Spec(chunk_a_weighting, self.fs)

        image = torch.from_numpy(chunk_result)  # shape=[257, 166]
        image = imageTransform(image)           # shape=[1, 257, 166]
        return image


def vad_collate_fn(batch):
    # batch -> list: [tensor(1, 257, 166), 1, tensor(1, 257, 166), tensor(1, 257, 166), 4, ...]
    nan_lst = []
    image_lst = []
    for item in batch:
        if isinstance(item, int):
            nan_lst.append(item)
        else:
            image_lst.append(item)
    if image_lst:
        image_lst = torch.cat(image_lst, dim=0)
        image_lst = imageListTransform(image_lst)
        return image_lst, nan_lst
    else:
        return False, nan_lst














