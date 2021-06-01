#Multitple inherianace


class mother:
    def printing(self):
        print("I am the mother of the child")



class father:
    def display(self):
        print("I am the father of the child")


class child(mother,father):
    pass



hamim = child()
hamim.printing()
hamim.display()
