# prints to the console
print("Hello World")
print(10, end=" ")
print(20)

# the end parameter specifies what do you want at the end, by default it is \n
print(10, end=" and ")
print(20)

# the sep seperates the things within the print statement by whatever is denoted within sep =
print(10, 20, sep=",", end=" and ")
print(30)

# Task: Hello World, India, Brazil.
print("Hello","World")
print("India", "Brazil")

# Answer:
print("Hello","World", sep=" ", end=", ")
print("India", "Brazil", sep=", ", end=".")
