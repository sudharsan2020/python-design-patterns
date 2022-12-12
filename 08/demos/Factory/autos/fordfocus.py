from .abs_auto import AbsAuto

class FordFocus(AbsAuto):

	def start(self):
		print(f'{self.name} running cooly!')

	def stop(self):
		print(f'{self.name} shutting down.')