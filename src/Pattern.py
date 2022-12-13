'''
*
**
***
****
'''

print("Enter number of Lines: ")
n = int(input())
#
# for i in range(0,n):
#     for j in range(0,i+1):
#         print("*", end="")
#     print(" ")


for i in range(0, n):
    for j in range(0, n):
        if j >= 3 - i:
            print("*", end="")
        else:
            print(" ", end="")
    print(" ")
