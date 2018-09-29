import pickle
import numpy
numpy.set_printoptions(threshold=numpy.nan)
import matplotlib.pyplot as plt

pkl_path = 'data/a_charactor.pickle'
save_path = 'data/a_charactor_bim.pickle'

with open(pkl_path, 'rb') as f:
	grayscale_img = pickle.load(f)

bool_array = (grayscale_img < 150)  # 0 が暗い、　255が明るい
filtered_grayscale_img = bool_array * 1

print(filtered_grayscale_img)

# filtered_grayscale_img = 1 - filtered_grayscale_img  # 反転


with open(save_path, 'wb') as f:
	pickle.dump(filtered_grayscale_img, f)

plt.subplot(2,3,1), plt.imshow(filtered_grayscale_img, 'gray'), plt.title("thresh1")
plt.show()

