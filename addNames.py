#Shaya Farahmand
#November 2, 2020
#Allows the user to enter five names and append each to a list

#List of names variable, which contains each name
list_of_names = []


#Allows the user to determine how many names you would like to input. Stored in the quant variable.

quant = input("How many names would you like to enter (enter an integer): ")

#Allows the user to a name, stored in the name variable, and will add that name to the list_of_names list.
#Done "quant" times (quant being the variable entered above)
for i in range(quant):
	name = input("What is the name?: ")
	list_of_names.append(name)


#Prints out the new list of names
print(list_of_names)
