#Property Decorators - Getters, Setters, and Deleters
#The property decorator allows us to define Class methods that we can access like attributes.
#This allows us to implement getters, setters, and deleters.

#property decorator allows us to define a method, that we can access like an attibute
#defining email, fullname in our class as a method, but we are able to access it like an attribute
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

        
emp_1 = Employee('hamim', 'Phopal')

#emp_1.fullname = 'Adam Phopal' #setting a new fullname

#del(emp_1.fullname)   #deleting a fullname

#Remember, property decorator allows us to define a method, that we can access like an attibute.
print(emp_1.first) #emplyess class instance, thats prints first name
print(emp_1.email) #property decorator email method returns email
print(emp_1.fullname) #property decorator fullname method returns fullname
