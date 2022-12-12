# IF - ELSE

print("Hey !! What's the weather today??", end="\n")
weather_condition = input()

'''
In Python, we use indentation instead of braces to define scopes 

When the "IF" statement is True, it executes the commands within indentation and directly jumps the else part.
Whatever is written outside else or Indented outside else is executed thereafter
'''

if weather_condition == "Rainy" or weather_condition == "Stormy":
    print("Hey, Please don't go out today.")
else:
    print("Hey, you can go out today and enjoy!!")
print("The program jumped here after the IF statement was True")
