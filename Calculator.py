# Arithmetic operators
# Operator	Operator Name	Example
# +	         Addition	      15+7
# -	         Subtraction	  15-7
# *	         Multiplication	  5*7
# **	     Exponential	  5**3
# /          Division	      5/3
# %	         Modulus	      15%7
# //	     Floor Division	  15//7
# print(5+6)
# print(15//6)
# print(10%3)
# print(2**10)

# Exercise 1 - Create a Calculator
# Create a calculator capable of performing addition, subtraction, multiplication and division operations on two numbers. Your program should format the output in a readable manner!

a = int(input("Enter the first digit\n"))
operator = input("Enter the operator\n")
b = int(input("Enter the Second digit\n"))

ans=None

if operator == '+':
 ans = a + b
elif operator == '-' :
  ans = a - b
elif operator == '/' :
  ans = a / b  
elif operator == '//' :
  ans = a // b
elif operator == '*' :
  ans = a * b  
elif operator == '**' :
  ans = a ** b
else :
  ans = a % b
print(a,operator,b," = ",ans)