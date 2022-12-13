# Arrays in Python


marks = [100, 73, 44, 98, 23, 87]
marks.insert(1,99)   #Important
for i in range(0, len(marks)):
    print("Marks of Student",i+1, "are",marks[i])
print("End of the program!!")

'''
Append: array_name.append(value) adds the particular value at the END of the array

'''
print(" ")
marks.sort()
for i in range(0, len(marks)):
    print("Marks of Student",i+1, "are",marks[i])
print("End of the program!!")