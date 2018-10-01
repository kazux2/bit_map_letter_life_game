
import time
import pickle
import numpy as np
np.set_printoptions(threshold=np.nan)
import matplotlib.pyplot as plt

# for not_notMNISTの使い方
# SEE: https://github.com/zafartahirov/not_notMNIST

# not_notMNISTのpickle(python2, 0 ~ 255のグレースケールのリスト + 文字ラベル)をpython3,bitmap(0 ~ 1)のpickleに変換するスクリプト

# pkl_path = 'data/not_notMNIST-master/small_trial/kanjis/28x28.pickle'
save_path = 'data/not_notMNIST-master/small_trial/kanjis/28x28bit_map_label_and_img.pickle'

with open(save_path, 'rb') as f:
	bit_map_label_and_img = pickle.load(f, encoding='latin1')

bit_map_labels = bit_map_label_and_img['labels']
bit_map_images = bit_map_label_and_img['images']


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


grayscale_label_and_img = {
	'labels': bit_map_labels,
	'images': []
}

for i in range(len(bit_map_images)):

	grayscale_img = bit_map_images[i] * 255
	grayscale_label_and_img['images'].append(grayscale_img)

	# reveresed_bit_map_img = 1 - bit_map_img  # 反転
	# bit_map_label_and_img['images'].append(reveresed_bit_map_img)

# お試し表示
# plt.subplot(2,3,1), plt.imshow(bit_map_label_and_img['images'][0], 'gray'), plt.title("thresh1")
# plt.show()

import cv2
import matplotlib.pyplot as plt
for img in grayscale_label_and_img['images']:

	# img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
	# img.dtype = 'uint8'
	# print(img)
	# cv2.imshow('frame', img)
	cv2.imwrite('asd.jpg'.format(img), img)
	# if cv2.waitKey(1) & 0xFF == ord('q'):
	# 	break
	# time.sleep(10)



# Release everything if job is finished

cv2.destroyAllWindows()
