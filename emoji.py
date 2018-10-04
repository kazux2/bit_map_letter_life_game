

import cv2
import json
import pickle
from os import listdir
from os.path import isfile, join, splitext
import numpy as np
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN


class Emoji:
	with open('data/emoji/w_twe.pickle', 'rb') as f:
		emojis = pickle.load(f)
	emojis_len = len(emojis)
	current_emoji_index = 0
	current_emoji_times = 0

	def is_continue(self):
		'''
		continue: 1, true
		not continue: 0
		:return: bool
		'''
		if self.current_emoji_times > 3:
			self.current_emoji_times = 0
			return 0

		return np.random.randint(1, 11) % 2 > 0  # 70%の確率でTrue

	def next(self):
		if self.is_continue():
			self.current_emoji_times += 1
		else:
			self.current_emoji_index = np.random.randint(0, self.emojis_len)

		return self.emojis[self.current_emoji_index]

if __name__ == "__main__":

	dir_path = 'data/emoji/whiten_twemoji72x72'
	save_pickle_path = 'data/emoji/w_twe.pickle'
	# dir_path = 'data/emoji/whiten_twemoji72x72'

	file_names = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
	emojis = []
	for file_name in file_names:
		root, ext = splitext(file_name)
		if not ext in ['.png', '.jpeg', '.jpg']:
			continue

		img = cv2.imread('{}/{}'.format(dir_path, file_name), cv2.IMREAD_UNCHANGED)
		print(img.shape)
		emojis.append(img)

	with open(save_pickle_path, 'wb') as f:
		pickle.dump(emojis, f)

	# cv2.imshow('name', emojis[500])
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

