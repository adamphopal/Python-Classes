#encapsulation
#Public methods and variables can be accessible outside the class also.
#But we cant access private methods outside the class and private variables
#can be modified only inside the class.

#only access private methods inside the class, aka the init method
#class car:
#    def __init__(self):
#        self.__updatesoftware()
#    def drive(self):
#        print("driving")
#    def __updatesoftware(self):
#        print("updating software")


#blackcar = car()
#blackcar.drive()


#private variables can be modified only inside the class, thorugh the class methods
class car:
    __maxspeed = 0
    __name = ""
    def __init__(self):
        self.__maxspeed = 200
        self.__name = "supercar"
    def drive(self):
        print("driving")
        print(self.__maxspeed)
    def setspeed(self,speed):
        self.__maxspeed = speed
        print(self.__maxspeed)

redcar = car()
redcar.drive()
redcar.setspeed(100)


