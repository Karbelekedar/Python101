'''

The def keyword suggests that the block of code is a function.

Function Definition is as follows:
def function_name():
    // logic

We call the function as function_name().
The execution starts from the global scope and not from the function definition.
'''


def print_message():
    print("Control is inside the function!!")


print("This is where execution starts")
print_message()
print("Control is outside the function!!")

'''
Parameters: Parameters are variables listed within the brackets at the time of function definition.
Arguments: These are the actual values that are passed into the function whenever it is called.
                       Order of arguments matters!!!!

Here, a & b are PARAMETERS and values of x & y are ARGUMENTS.
'''

# def add_number(a, b):
#     res = a + b
#     return print("The sum is", res)
#
# print("Enter a number: ")
# x = int(input())
# print("Enter another number: ")
# y = int(input())
#
# add_number(x, y)

'''
Euclid's Algorithm to find GCD

GCD(a, b): 
GCD(0, b): b
GCD(a, 0): a
Quotient of a/b
Remainder of a/b
a = b*q + r
GCD(b, r)


'''



def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        q = divmod(a, b)
        r = a % b
        return gcd(b, r)

print("Euclid's Algorithm!!")

print("Enter 1st number: ")
x = int(input())
print("Enter 2nd number: ")
y = int(input())

result = gcd(x, y)
print("The GCD of",(x, y),"is ",result)
