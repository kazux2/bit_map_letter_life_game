import numpy as np

STATIC = np.array(
[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [1,1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0],
 [1,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1],
 [0,0,0,0,0,1,1,0,0,0,0,1,0,1,0,0,0,1,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
])

OSCILLATOR = np.array(
[[1,0,0,0,0,1,0,0],
 [1,0,0,0,1,0,0,1],
 [1,0,0,0,1,0,0,1],
 [0,0,0,0,0,0,1,0]])

GLIDER = np.array(
[[0,0,0,0],
 [0,0,1,0],
 [0,0,0,1],
 [0,1,1,1]])


GLIDER_GUN = np.array(
[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
 [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
 [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])

DOT = np.array(
 [[1]])

import pickle
# with open("binary_img_PixelMplus_344.pickle", "rb") as f:
# with open("binary_img_misaki_gothic.pickle", "rb") as f:
with open('data/a_charactor_bim.pickle', "rb") as f:
 BITMAP = pickle.load(f)

with open('data/not_notMNIST/small_trial/kanjis/28x28bit_map_label_and_img.pickle', "rb") as f:
 bit_map_label_and_img = pickle.load(f)


with open('data/not_notMNIST/2018summer_art_project/numbers/28x28bit_mapped_thresh50.pickle', "rb") as f:
 SCENE2NUM_TH50 = pickle.load(f)

with open('data/not_notMNIST/2018summer_art_project/numbers/28x28bit_mapped_thresh150.pickle', "rb") as f:
 SCENE2NUM_TH150 = pickle.load(f)

with open('data/not_notMNIST/2018summer_art_project/numbers/28x28bit_mapped_thresh250.pickle', "rb") as f:
 SCENE2NUM_TH250 = pickle.load(f)

# with open('data/not_notMNIST/2018summer_art_project/a_to_z/28x28bit_map_label_and_img.pickle', "rb") as f:
#  SCENE3ALPHABET = pickle.load(f)
#
# with open('data/not_notMNIST/2018summer_art_project/kana/28x28bit_map_label_and_img.pickle', "rb") as f:
#  SCENE4KANA = pickle.load(f)
#
# with open('data/not_notMNIST/2018summer_art_project/kanji_small/28x28bit_map_label_and_img.pickle', "rb") as f:
#  SCENE5KANJI = pickle.load(f)


with open('data/not_notMNIST/2018summer_art_project/merged_pickle/number_and_a_to_z.pickle', "rb") as f:
 NUM_ALPH = pickle.load(f)

with open('data/not_notMNIST/2018summer_art_project/merged_pickle/number_and_a_to_z_and_kana.pickle', "rb") as f:
 NUM_ALPH_KANA = pickle.load(f)

with open('data/not_notMNIST/2018summer_art_project/merged_pickle/number_and_a_to_z_and_kana_and_kanji.pickle', "rb") as f:
 NUM_ALPH_KANA_KANJI = pickle.load(f)

