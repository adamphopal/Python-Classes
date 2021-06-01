#Polymorphism is the ability of an object to adapt the code to the type of the data
#it is processing.Here poly means many and morphi means forms.
#In Python polymorphism is one of the key concepts and we can say that it is a built-in feature.
#polymorphism helps us to describe an action regardless of the type of objects.


#polymorphism is nothing more than a method that behaves diffrently for diffrent objects
class dog:
    def sound(self):
        print("bow wow")

class cat:
    def sound(self):
        print("meow")

def makesound(animaltype): #function created for class objects
    animaltype.sound()

catobj = cat()
dogobj = dog()
makesound(catobj) #prints bow wow
makesound(dogobj) #prints meow




    
