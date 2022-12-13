# OOPS

# Creating a class Dog and it's methods
class Dog():

    def set_name(self, name):
        self.name = name

    def bark(self):
        print(self.name,"is barking!!")

    def run(self):
        print(self.name,"is running!!")

# Creating Objects of class Dog
obj1 = Dog()
obj2 = Dog()

obj1.set_name("Tommy")
obj2.set_name("Max")

obj1.bark()
obj1.run()
obj2.bark()
obj2.run()
