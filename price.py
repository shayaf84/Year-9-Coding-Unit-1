#Shaya Farahmand
#November 2, 2020
#Program that allows the user to enter the price of a number of items, and output will be price + tax

#Allows the user to determine how many prices you would like to input. Stored in the quant variable.
quant = int(input("How many prices would you like to enter (enter an integer): "))

#Counter variables initaliazed, for measuring the subtotal (subtotal), total (total), and overall tax paid (tax_overall)
subtotal = 0
total = 0
tax_overall = 0

#For the amount of times specified in quant, the user enters a price of an item (stored in the price variable)
#The price - including tax will be returned, in the overall variable.
#The value for tax paid will be stored in the tax variable
#We will add the values for price, overall, and tax, to the subtotal, total, and tax_overall variables respectively \
#	This is to keep track of subtotal, total, and tax.
for i in range(quant):
	price = float(input("Enter the price of an item, in dollars and cent form: "))
	tax = price*0.13
	overall = tax+price
	print("The total price of this item is: $"+str(overall))
	subtotal += price
	total += overall
	tax_overall += tax

#Returns the overall subtotal, tax, and total price paid.
print("-------------------------")
print("The subtotal is: $" + str(subtotal))
print("The total tax value is: $" + str(tax_overall))
print("The total is: $" + str(total))

