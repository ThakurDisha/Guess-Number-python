import random

class game():
	def __init__(self, name="", attempts = 5):
		self.name= name
		self.attempts= attempts

	def greeting(self):
		print("Hello {}".format(self.name))

	def explain(self):
		print("You, the player, are thinking of a number between 1 and 100.\n")
		print("I, the clever computer will try to guess it in as few attempts as possible. I have {} attempts.". format(self.attempts))

	def num(self):
		z= input("Select a number between 1 to 100: ")
		print(z)


class guess(game):

	def __init__(self,attempts):
		super(guess, self).__init__(attempts)

	def number(self):
		count = 1
		while count <= self.attempts:
			self.num = random.randrange(1,100)
			ans= input("Is it {} ? (Yes, Higher, Lower)?".format(self.num))
			if ans == "Yes":
				print("I guessed it")
				break
			count += 1
		print("Ohh no! I ran out of attempts")



a=guess("Disha")
a.greeting()
a.explain()
a.num()
a.number()