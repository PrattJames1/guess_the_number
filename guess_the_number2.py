""" Guess the number!

Have the computer select an integer between 1 and 100 (inclusive)
and ask the user to guess that number.

Keep track of the user's number of guesses required to guess the correct value.

Provide feedback to the user indicating if their guess is too low or too high.

Make sure that incorrect input by the user (for exemple: entering a word
instead of number) are taken care of with appropriate feedback
given to the user.

Allow the user to leave the game at any time by entering a value of -1.

End the program by giving the user appropriate feedback; for example, if the
user guesses correctly, indicate how many guesses were needed.
"""

import sys
import random

def main():
	number = random.randint(1, 100)
	guesses = 0
	guess = 0

	while True:
		try:
			guess = int(input("\nI'm thinking of a number between 1 and 100.\nCan you guess it?: " +
				"(Type -1 to quit) "))

			if guess == number:
				print("You got it! The number was " + str(number))
				break
			elif guess == -1:
				print("\nQuitting...\n")
				break
			if guess > number:
				print("\nLower!")
				guesses += 1
			elif guess < number:
				print("\nHigher!")
				guesses += 1
		except ValueError:
			print("\nPlease enter a valid integer!")

	print("Thanks for playing the game!")
	print("Total guesses: " + str(guesses))
	sys.exit()

if __name__ == "__main__":
	main()