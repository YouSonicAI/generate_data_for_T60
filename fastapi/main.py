import os
import sys
import time
import pandas as pd
import torch
import torch
import time
import wave
import numpy as np
import scipy
from torch.utils.data import DataLoader
from fastapi import FastAPI
import onnxruntime as ort
from fastapi import FastAPI, File, UploadFile
from scipy.io.wavfile import write
from dataloader import DatasetSlice, vad_collate_fn
# import librosa
from starlette.responses import FileResponse
from moviepy.editor import AudioFileClip
from tqdm import tqdm
onnx_path = "./Model/ImageClassifier2.onnx"
save_dir = "./Sava_floder/"
output__dir = "./Pro_floder/"
zip_dir = './zip_floder/'
app = FastAPI()
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import zipfile
import oss2
import glob

overlap = 1
batch_size = 4
average_iterval = 5



def read_root():
#     info = load_model()
    return "Hello"
#
# @app.get("/process")
# def process_audio():
#     info = load_model()
#
#     return {"Hello": info}



@app.post("/upload")#, summary="上传数据文件")
async def upload_file(file: UploadFile = File(...)):
    name = file.filename
    # print("name", name)
    # In order to obtain user file of uploading and save the 'save_dir'
    info = await file.read()
    with open(save_dir + file.filename, "wb") as f:
        f.write(info)
    f.close()

    # user upload file  processed  by model then save file to 'output__dir'
    # file = os.listdir(save_dir)
    temp = os.path.join(save_dir, name)
    load_model(temp, output__dir)

    # model processed file is made the zip file then save 'zip_dir'

    zip_name = zip_dir + name.split(".")[0] + '.zip'



    zip = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    for item in os.listdir(output__dir):
        compare_name = str(name.split('.')[0])
        new_item = str(item)
        # print("item", item)
        # print("name", name)
        if compare_name in new_item:
            file = os.path.join(output__dir, item)
            print(file)
            zip.write(file, arcname=item)
    zip.close()

    # zip file upload file to oss
    temp_file = './zip_floder/'
    usr_name = name.split(".")[0] + '.zip'
    # upload_oss(usr_name, zip_name)

    print('finished!')



    # 返回服务端处理后的文件
    return FileResponse(str(temp_file+ usr_name), filename=usr_name)
    # return {'finished'}

def upload_oss(filename, file):
    access_key_id = 'LTAI5tAzLJwWiQBHqX6ywLxa'
    access_key_secret = 'R60PTPKqrMgPwli9dZjwL1Mp3xmCxR'
    bucket_name = 'sti-user-file'
    endpoint = 'https://oss-cn-hangzhou.aliyuncs.com'
    auth = oss2.Auth(access_key_id, access_key_secret)
    bucket = oss2.Bucket(auth, endpoint, bucket_name, connect_timeout=40)
    final = bucket.put_object_from_file(filename, file)
    print('finished!!!!')



# @app.post("/uploadfiles/")
# async def create_upload_files(files: List[UploadFile] = File(...)):
#     for files in files:
#         name = file.filename
#     return {"filenames": [file.filename for file in files]}


# Load model
def load_model(path, output_dir):

    video_path = path
    video = VideoProcessing(video_path)
    resultPrinter = ResultPrinter()
    if video.audio_time <= 4:
        raise ValueError('Audio time less than 4s, cannot infer its STI!')

    start_time = time.time()
    ort_session = ort.InferenceSession(onnx_path)
    dataset = DatasetSlice(video.audio, video.fs, overlap, False)
    videoloader = DataLoader(dataset, batch_size=batch_size, shuffle=False, collate_fn=vad_collate_fn, drop_last=False)
    print('Analyse STI of the audio...')
    output_collection = []
    empty_index = []
    with torch.no_grad():
        progress_bar = tqdm(videoloader)
        for i, datas in enumerate(progress_bar):
            images, temp_vad_lst = datas
            if temp_vad_lst:
                empty_index.extend(temp_vad_lst)
            if isinstance(images, bool):
                continue

            if not images.shape[0] == 4:
                continue
            input_image = images.numpy().astype(np.float32)
            # print("input image shape:",input_image.shape)

            output_pts = ort_session.run(None, {'modelInput': input_image})
            output_pts = np.squeeze(output_pts).tolist()
            # print("output pts shape:",output_pts)
            # onnx_cost  = time.time() - begin
            # print("pytorch output:",output_pts,",cost time:",pytorch_cost)
            # print("onnx output:",output_pts2,",onnx time:",onnx_cost)

            if isinstance(output_pts, float):
                output_collection.append(output_pts)
            else:
                output_collection.extend(output_pts)

    if empty_index:
        for item in empty_index:
            output_collection.insert(item, 'NaN')
        # print('STI Results:')
    resultPrinter.print_results(out=output_collection)
    save_name = os.path.join(output_dir, video_path.split('/')[-1].split('.')[0])
    # print("123132132132"+ video_path.split('\\')[-1].split('.')[0])
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # print("output_dir", output_dir)
    resultPrinter.save_csv_result(save_name + '.csv')
    print('- Csv results saved:', save_name + '.csv')

    gen_plot(resultPrinter.out_dict['STI'], resultPrinter.end_time_num, video_path, save_name + '.png')
    print('- Plot results saved:', save_name + '.png')







def gen_plot(result, endLst, file_path, save_path):
    if isinstance(result[0], float):
        filtered_res, timeLst = [result[0]], [0]
    else:
        filtered_res, timeLst = [], []

    sti_total = 0
    sti_count = 0
    for item, endtime in zip(result, endLst):
        if item not in ['nan', 'NaN']:
            sti_total += float(item)
            sti_count += 1
            filtered_res.append(float(item))
            timeLst.append(endtime)

    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    plt.rcParams["axes.unicode_minus"] = False
    fig = plt.figure(figsize=(15, 9))
    ax = fig.add_subplot(111)
    plt.xlabel('Time / s', fontsize=20)

    if sti_count != 0:
        avarage = str(sti_total / sti_count)[:4]
    else:
        avarage = 0

    plt.ylabel('STI', fontsize=20)

    plt.plot(timeLst, filtered_res, color='red', label='right', linestyle='-')

    plt.ylim(0, 1)
    plt.grid(linestyle='-.')
    plt.yticks(size=15)
    plt.xticks(size=15)

    yMajorLocator = MultipleLocator(0.1)
    ax.yaxis.set_major_locator(yMajorLocator)

    xMajorLocator = MultipleLocator(10 ** int(np.log10(sti_count)))
    ax.xaxis.set_major_locator(xMajorLocator)

    title = "\n".join(['STI Result', 'File:' + file_path.split('/')[-1]])
    plt.suptitle(title, fontsize=25)
    fig.text(s='Average STI:  ' + str(avarage), x=0.85, y=0.955, fontsize=25, ha='center', color='red')
    fig.savefig(save_path)


class ResultPrinter(object):
    """一个无情的结果打印机器"""

    def __init__(self):
        self.out_dict = {'start': [], 'end': [], 'STI': []}
        self.end_time_num = []

    def print_results(self, out):
        already_time = self.get_start_len()
        for i in range(len(out)):
            start = (already_time + i) * overlap
            end = start + 4
            # print('time: [%.1f]s ~ [%.1f]s      STI: [%.2f] ' % (start, end, float(out[i])))
            self.out_dict['start'].append(second_to_time(start))
            self.end_time_num.append(start)
            self.out_dict['end'].append(second_to_time(end))
            # if i < average_iterval:
            #     average_sti = get_sum(out[:i + 1]) / (i + 1)
            # else:
            #     average_sti = get_sum(out[i - average_iterval + 1:i + 1]) / average_iterval
            self.out_dict['STI'].append(float(out[i]))

    def save_csv_result(self, save_file_path):
        for i in range(len(self.out_dict['STI'])):
            self.out_dict['STI'][i] = str(self.out_dict['STI'][i])[:4]
        out_data = pd.DataFrame.from_dict(self.out_dict)
        out_data.to_csv(save_file_path)
        print('Save csv already! Path: ', save_file_path)

    def get_start_len(self):
        return len(self.out_dict['start'])


class VideoProcessing(object):
    def __init__(self, path):
        self.path = path
        self.audio = None
        self.audio_time = None
        self.fs = None
        self.get_wav_from_video()

    def get_wav_from_video(self):
        my_audio_clip = AudioFileClip(self.path)
        audio_data = my_audio_clip.to_soundarray()
        framerate = my_audio_clip.fps
        if framerate != 16000:
            audio_data = scipy.signal.resample(audio_data, int(len(audio_data) / framerate * 16000))
        nframes, nchannels = audio_data.shape
        if nchannels == 2:
            audio_data = audio_data.T[0]
        if isinstance(audio_data[0], np.float):
            audio_data = np.array(audio_data * 32768.0, dtype=np.int16)
        elif isinstance(audio_data[0], np.int32):
            audio_data = (audio_data >> 16).astype(np.int16)
        audio_time = len(audio_data) / 16000
        self.audio, self.audio_time, self.fs = audio_data, audio_time, 16000


def second_to_time(a):
    if '.5' in str(a):
        ms = 5000
        a = int(a - 0.5)
    else:
        ms = 0000
        a = int(a)
    h = a // 3600
    m = a // 60 % 60
    s = a % 60
    return str("{:0>2}:{:0>2}:{:0>2}.{:0>4}".format(h, m, s, ms))

