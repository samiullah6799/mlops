class Wallet:
	def __init__(self, amount):
		self.amount = amount

	def getAmount(self):
		return self.amount

	def withdraw(self, amount):
		self.amount = self.amount - amount
		return self.amount

	def deposit(self, amount):
		self.amount = self.amount + amount
		return self.amount
