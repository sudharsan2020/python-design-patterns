from .abs_auto import AbsAuto

class NullCar(AbsAuto):

	def start(self):
		print(f'Unknown car "{self.name}".')

	def stop(self):
		pass