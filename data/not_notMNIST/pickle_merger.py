import pickle
import numpy as np
np.set_printoptions(threshold=np.nan)
import matplotlib.pyplot as plt

# for not_notMNISTの使い方
# SEE: https://github.com/zafartahirov/not_notMNIST

# not_notMNISTのpickle(python2, 0 ~ 255のグレースケールのリスト + 文字ラベル)をpython3,bitmap(0 ~ 1)のpickleに変換するスクリプト

pkl_path1 = '2018summer_art_project/merged_pickle/number_and_a_to_z_and_kana.pickle'
pkl_path2 = '2018summer_art_project/kanji_small/28x28bit_map_label_and_img.pickle'

save_path = '2018summer_art_project/merged_pickle/number_and_a_to_z_and_kana_and_kanji.pickle'

with open(pkl_path1, 'rb') as f:
	grayscale_label_and_img = pickle.load(f, encoding='latin1')

grayscale_labels1 = grayscale_label_and_img['labels']
grayscale_images1 = grayscale_label_and_img['images']

with open(pkl_path2, 'rb') as f:
	grayscale_label_and_img = pickle.load(f, encoding='latin1')

grayscale_labels2 = grayscale_label_and_img['labels']
grayscale_images2 = grayscale_label_and_img['images']

grayscale_labels1.extend(grayscale_labels2)
grayscale_images1.extend(grayscale_images2)

new_dict = {
	'labels': grayscale_labels1,
	'images': grayscale_images1
}

with open(save_path, 'wb') as f:
	pickle.dump(new_dict, f)


