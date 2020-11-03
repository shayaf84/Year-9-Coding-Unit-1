#Shaya Farahmand
#November 2, 2020
#Program that allows the user to have 5 guesses to enter a password

#This is the password. Feel free to change it. It is assigned in the password variable.
password = "self"

#Asks the user to enter a password guess. 
#If it is correct, it will return that he got it correct. If it is incorrect, he will have more tries, and it will output\
#	that it is incorrect.
#This is only for 5 tries. 
for i in range(5):
	attempt = input("Enter a password: ")
	if attempt == password:
		print("You got it!")
		break
	else:
		print("Sorry, that's not correct!")

#After 5 tries, if the user still did not answer the password correctly, he is not allowed to enter anymore.
if attempt != password:
	print("Out of guesses!")
