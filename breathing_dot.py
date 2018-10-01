
import numpy as np
class BreathingDot:

	life_limit = 0
	living_time = 0

	death_limit = 0
	dead_time = 0

	life_status = 0

	def next(self):

		if self.life_status:

			self.living_time += 1

			if self.living_time >= self.life_limit:
				self.life_limit = np.random.randint(50, 500)  # 次のライフタイムをセット
				self.life_status = 0  # kill
				self.living_time = 0

			return 1

		else:

			self.dead_time +=1

			if self.dead_time >= self.death_limit:
				self.death_limit = np.random.randint(50, 500)  # 次のライフタイムをセット
				self.life_status = 1  # birth
				self.dead_time = 0

			return 0

if __name__ == "__main__":
	b = BreathingDot()
	while True:
		print(b.next())