import random

number = random.randint(1, 10)

def question():
	print("I'm thinking of a number. Can you guess it?: ")
	guess = input("")
	if int(guess) > number:
		print("Lower!")
		question()
	elif int(guess) < number:
		print("Higher!")
		question()
	elif int(guess) == number:
		print("You got it!")
		quit

question()