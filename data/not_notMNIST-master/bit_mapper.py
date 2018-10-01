import pickle
import numpy as np
np.set_printoptions(threshold=np.nan)
import matplotlib.pyplot as plt

# for not_notMNISTの使い方
# SEE: https://github.com/zafartahirov/not_notMNIST

# not_notMNISTのpickle(python2, 0 ~ 255のグレースケールのリスト + 文字ラベル)をpython3,bitmap(0 ~ 1)のpickleに変換するスクリプト

pkl_path = 'data/not_notMNIST-master/small_trial/kanjis/28x28.pickle'
save_path = 'data/not_notMNIST-master/small_trial/kanjis/28x28bit_map_label_and_img.pickle'

with open(pkl_path, 'rb') as f:
	grayscale_label_and_img = pickle.load(f, encoding='latin1')

grayscale_labels = grayscale_label_and_img['labels']
grayscale_images = grayscale_label_and_img['images']


#4つランダムに表示
# num_points = len(grayscale_labels)
# f, ax = plt.subplots(2,2)
# for i in range(2):
# 	for j in range(2):
# 		idx = np.random.randint(num_points)
# 		ax[i,j].imshow(grayscale_images[idx], cmap='Greys_r')
# plt.show()

#1つだけ表示
# img = grayscale_images[0]
# print(img)
# ax[0,0].imshow(img, cmap='Greys_r')
# plt.show()



# bool_array = (grayscale_images[0] < 50)  # 0 が暗い、　255が明るい
# bit_map_img = bool_array * 1
# print(bit_map_img)
# filtered_grayscale_img = 1 - filtered_grayscale_img  # 反転


bit_map_label_and_img = {
	'labels': grayscale_labels,
	'images': []
}

for i in range(len(grayscale_images)):

	bool_array = (grayscale_images[i]< 250)  # 0 が暗い、　255が明るい

	bit_map_img = bool_array * 1
	bit_map_label_and_img['images'].append(bit_map_img)

	# reveresed_bit_map_img = 1 - bit_map_img  # 反転
	# bit_map_label_and_img['images'].append(reveresed_bit_map_img)

# お試し表示
# plt.subplot(2,3,1), plt.imshow(bit_map_label_and_img['images'][0], 'gray'), plt.title("thresh1")
# plt.show()

with open(save_path, 'wb') as f:
	pickle.dump(bit_map_label_and_img, f)


