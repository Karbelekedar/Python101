# OOPS
'''
During Garbage Collection, the del method is called but if we manually call the del method, it does not
destroy the object from the memory.

'''
# Creating a class Dog and it's methods
class Dog():

    # def set_name(self, name):
    #     self.name = name

    def __init__(self, name): # This is a constructor in Python
        self.name = name

    def bark(self):
        print(self.name,"is barking!!")

    def run(self):
        print(self.name,"is running!!")

    def born(self):
        print(self.name,"is born!!")

# Creating Objects of class Dog
# obj1 = Dog()
# obj2 = Dog()
#
# obj1.set_name("Tommy")
# obj2.set_name("Max")
#
# obj1.bark()
# obj1.run()
# obj2.bark()
# obj2.run()

print("Tommy is having a baby, is it a boy or a girl??")

x = input()

if x=="Boy":
    Max = Dog("Max")
    Max.born()
elif x=="Girl":
    Nina = Dog("Nina")
    Nina.born()
else:
    print("Incorrect Input")
