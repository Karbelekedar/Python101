# Oops-2


class A(object):
    def __init__(self):
        self.name = "Class A"
        self.id = 10

class B(A):

    def __init__(self):
        A.__init__(self)
        self.name = "Class B"
        self.id = 20

class C(A):
    def __init__(self):
        self.name ="Class C"
        self.id = 30
        A.__init__(self)

'''
In the case of class C, as the Parent Class A contains the same attributes i.e name & id 
It first calls the constructor of C but the attributes are overridden because A has the same attributes 
and it's called afterwards.

Explore Class and static methods, also explore Class Variables and Instance Variables...

'''

b = B()
c = C()

print(b.name, b.id)
print(c.name, c.id)