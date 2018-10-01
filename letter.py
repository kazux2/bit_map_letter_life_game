
import numpy as np
import game_of_life_patterns

class Letter:

	letters = game_of_life_patterns.bit_map_label_and_img["images"]
	letters_len = len(letters)
	current_letter_index = 0
	current_letter_times = 0

	current_letter = letters[current_letter_index]

	def is_continue(self):
		'''
		continue: 1, true
		not continue: 0
		:return: bool
		'''
		if self.current_letter_times > 3:
			self.current_letter_times = 0
			return 0

		return np.random.randint(1, 11) % 2 > 0  # 70%の確率でTrue


	def next(self):

		if self.is_continue():
			self.current_letter_times += 1
		else:
			self.current_letter_index = np.random.randint(0, self.letters_len)

		return self.letters[self.current_letter_index]


