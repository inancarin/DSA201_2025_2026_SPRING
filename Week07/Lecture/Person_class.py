class Person:
    
    # constructor -> a method to create a new instance of given class
    def __init__(self, ID, name, age):
        self.ID = ID
        self.name = name
        self.myAge = age
    
    # getter method
    def getAge(self):
        return self.myAge
    
    # setter method
    def changeAge(self, newAgeValue):
        if isinstance(newAgeValue, int):
            if newAgeValue > 0:
                self.myAge = newAgeValue
            else:
                print("The age must be a positive integer")
        else:
            print("Sorry, the age must be an integer")
    
    # getter
    def getName(self):
        return self.name
    
    # getter
    def printName(self):
        print("Name is", self.name)

    # setter
    def changeName(self, newNameValue):
        self.name = newNameValue


