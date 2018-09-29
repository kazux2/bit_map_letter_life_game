
import cv2
import pickle
from matplotlib import pyplot as plt


# bit_map_letter_path = "misaki_gothic.png"
#
# img = cv2.imread(bit_map_letter_path, cv2.IMREAD_GRAYSCALE)
# img = img[300:350,300:350]
#
# # cv2.imshow('letter', img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
#
#
# ret,thresh1 = cv2.threshold(img,127,1,cv2.THRESH_BINARY)
# thresh1 = 1 - thresh1
# #SEE: http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html
#
#
# with open('binary_img_misaki_gothic.pickle', 'wb') as f:
# 	pickle.dump(thresh1, f)
# # plt.subplot(2,3,1), plt.imshow(thresh1, 'gray'), plt.title("thresh1")
# # plt.show()





"""
not_notMNISTの使い方
https://github.com/zafartahirov/not_notMNIST
"""
import pickle
import numpy as np
np.set_printoptions(threshold=np.nan)
import matplotlib.pyplot as plt

with open("data/not_notMNIST-master/Demo/Japanese/28x28/28x28.pickle", 'rb') as f:
	data = pickle.load(f, encoding='latin1')

labels = data['labels']
images = data['images']
num_points = len(labels)
f, ax = plt.subplots(2,2)
# for i in range(2):
# 	for j in range(2):
# 		idx = np.random.randint(num_points)
# 		ax[i,j].imshow(images[idx], cmap='Greys_r')
# plt.show()

img = images[7]
print(img)
ax[0,0].imshow(img, cmap='Greys_r')
plt.show()
with open('data/a_charactor.pickle', 'wb') as f:
	pickle.dump(img, f)

