#Shaya Farahmand
#November 2, 2020
#This is a program that will allow the teacher to enter a certain number of student's grades, and calculate the average\
#	of them.


#Counter that specifies the sum of all grades before calculating average
total = 0


#Specifies how many grades teacher will input (not the actual grade)
input_grades = int(input("How many grades will you input?"))


#For the number of times, the teacher specified above, the program will ask the teacher to input a grade, and that will \
#	be stored in the changing grade variable. 
#The total counter will be updated, by adding the existing value to the new grade
for i in range(input_grades):
	grade = int(input("Enter the grade: "))
	total += grade

#Divides the sum of grades by number of grades inputted, and stored in the avg variable
avg = total/input_grades


#Prints the final grade (stored in the avg variable) - converted to string in order to allow concactenation
print("-------------------------------------")
print("The student's average grade is: " + str(avg))
