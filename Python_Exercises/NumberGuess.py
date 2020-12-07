#Allows a user to have 10 guesses to predict a number between 1 and 20
#Shaya Farahmand
#Oct. 30, 2020

#Imports the random number library
import random


print("Welcome to number guesser!")

#Random number generates a number between 1 and 20, and stores it in a number variable.
number = random.randint(1,20)


#User will have 10 guesses
for i in range(10):
	#Guess variable collects the user's guess
	guess = int(input("Please enter a number: "))
	#If the guess is out of range, they wasted a guess
	if guess >20 or guess<0:
		print("Error, select a number from 1-20")
	#Print, you got it, if the user guessed the number
	#If it was too high or too low, the program will return a statement for each respectively
	if guess == number:
		print("You got it!")
		break
	elif guess > number:
		print("A bit too high")
	elif guess < number:
		print("A bit too low")
#If all guesses are exhausted, the game will end
if guess != number:
	print("Sorry, you are out of guesses")
	print("Would you like to play again")
