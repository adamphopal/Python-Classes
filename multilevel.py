# Multilevel Inheritance
# base class
class grandpha:
    def display(self):
        print("Hello, this is the base class, named gradpha")


#derived class 1
class dad(grandpha):
    def printing(self):
        print("Hello, this is the derived class dad")

#derived class 2
class son(dad):
    def show(self):
        print("Hello, this is another derived class son")


adam = son()
adam.display()
adam.printing()
adam.show()
