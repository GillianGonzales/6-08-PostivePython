#
# Created By Gillian Gonzales
# Created On April 14 2018
#
# This program will multiply to postive integers 
#

print("Multiply two postive integers")

print("")

number1 = int(input("Integer 1: "))

print("")

number2 = int(input("Integer 2: "))

one = 1

answer = number2 

for loop in range(one,number1):
	answer = answer + number2
pass

print("")

print ("Your answer is:") 
print (answer)

print("")

input("End of program")