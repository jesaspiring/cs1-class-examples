"""
Create an App that will get two numbers 
from the users. 
The user will then input the desired 
operation to perform. +-/*
"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter desired operation (+,-,/,*): ")
result = 0

#Alternative Solution
# operation_choice = input("Select operation: \n" + 
#                          "1. Addition \n" +
#                          "2. Subtraction \n")



if(operation == "+"):
    result = num1 + num2
    
elif(operation == "-"):
    result = num1 - num2

elif(operation == "*"):
    result = num1 * num2

elif(operation == "/"):
    result = num1 / num2
    
print("First number:", num1)
print("Second Number:", num2)
print("Operation entered:", operation)
print("Result: ", result)