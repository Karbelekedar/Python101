'''
FOR loops:
Here the end point in the range isn't included

'''

print("Increment Loop")
for i in range(1, 11, 1):
    print(i, end=" ")

print("")

print("Decrement Loop")
for i in range(10, 0, -1):
    print(i, end=" ")

print("")


print("Multiplication Table of 7")
print("")

for i in range(1, 11):
    print(i,"x",7, "=",i*7, sep=" ")