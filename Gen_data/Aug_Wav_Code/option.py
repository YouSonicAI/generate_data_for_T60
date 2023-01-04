import argparse

parser = argparse.ArgumentParser(description='load these files')
#
parser.add_argument('--CORPUS_INPUT_FOLDER_ROOT', default='/data2/new_wzd/1000Hz/RIR_Data/', type=str,help='load rir root')
parser.add_argument('--CORPUS_OUTPUT_FOLDER_ROOT', default='/data2/new_wzd/1000Hz/modif_output_wav/', type=str)
parser.add_argument('--T60DRRresultsFile', default='/data2/new_wzd/1000Hz/modif_code/12_28_1000_HZ.csv', type=str)
#为了加速训练，必需按照config分开才行
parser.add_argument('--need_config', default='trollers-gill', type=str)
parser.add_argument('--MIC_CONFIGs', default="trollers-gill", type=str)
#parser.add_argument('--MIC_CONFIGs', default="Nature,Miscellaneous,Recreation,Stairwells,Underground,Underpasses,Venues", type=str)
parser.add_argument('--noise_dir', default="/data2/cql/code/augu_data/get_data/15NoiseScenes_txt", type=str)
parser.add_argument('--timit_root', default='/data2/cql/code/augu_data/concatPeople/chinese_concat', type=str)
parser.add_argument('--Speaker_txt', default='/data2/cql/code/augu_data/concatPeople/chinese_concat/catChinese.txt', type=str)
args = parser.parse_args()
