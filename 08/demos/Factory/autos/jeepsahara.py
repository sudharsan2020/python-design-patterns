from .abs_auto import AbsAuto

class JeepSahara(AbsAuto):

	def __init__(self, name):
		self._name = name

	def start(self):
		print(f'{self.name} running ruggedly.')

	def stop(self):
		print(f'{self.name} shutting down.')