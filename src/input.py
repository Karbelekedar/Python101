# Learning about inputs in Python

print("Demo program for user input")
print("Enter the first number:", end=" ")

'''
x = input() takes input from the user in the form of a STRING
so we convert it into integer for this case as follows:

Note: Every data-type has a wrapper class in Python and hence upon checking the data-type
of any variable, we get output as <class 'data-type'>
'''

x = int(input())
print("")
print("Enter the second number:", end=" ")

y = int(input())
print(type(y))

print("Sum is:", x+y)
print("Difference is:", x-y)
print("Division is:", x/y)
print("Product is:", x*y)
