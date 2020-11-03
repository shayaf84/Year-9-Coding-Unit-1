# Here is a program to show the area of a circle, rectangle, or triangle
#The hash-tag is used to show the comments
#Author: Shaya Farahmand
#Upper Canada College


#Options to choose from:
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

print("--------------------------------")

#User enters the corresponding number for shape - stored in shapeoption
shapeoption = int(input("Choose the number for your shape: \n"))
print("--------------------------------")


#Asks user length/width/radius/base/height - depending on the shape
#Calculates area and stores in respective variable - before printing it out.
	if shapeoption == 1:
		print("To calculate area of circle, enter the radius length. Pi is 3.14")
		radius = float(input("What is your radius?"))
		area = radius*radius*3.14
		print("The area of the circle is:", area, " sq. units")
		print("--------------------------------")
	elif shapeoption == 2:
		print("To calculate area of rectangle, enter length and width")
		length = float(input("What is the length?"))
		width = float(input("What is the width?"))
		area2 = length*width
		print("The area of the rectangle is:", area2, " sq. units")
		print("--------------------------------")
	elif shapeoption == 3:
		print("To calculate area of triangle, enter length and width")
		base = float(input("What is the base?"))
		height = float(input("What is the height?"))
		area3 = 0.5*base*height
		print("The area of the triangle is:", area3, " sq. units")
		print("--------------------------------")
	else:
		print("This is not a valid choice")
	
#Tells the user politely to quit program
input("Press ENTER to quit the program")





