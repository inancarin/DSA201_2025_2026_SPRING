class Person:
    def __init__(self, name, age, ssn):
        self.name = name
        self.age = age
        self.ssn = ssn # social security number
    
    def __str__(self):
        return str(self.ssn) + " " + self.name
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    

class Student(Person):
    def __init__(self, name, age, ssn, gpa=2.0, university="Sabanci University"):
        """
        self.name = name
        self.age = age
        self.ssn = ssn # social security number
        """
        super().__init__(name, age, ssn)
        self.gpa = gpa
        self.university = university
    
    def __str__(self):
        return "A student whose name is " + self.name + " from " + self.university 

class BsStudent(Student):
    pass

class MsStudent(Student):
    pass

if __name__ == "__main__":
    p1 = Person("Jack", 24, 11111)
    p2 = Person("Alice", 22, 22222)

    print(p1)
    print(p2)

    s1 = Student("Jack", 24, 11111, 2.1, "Koc University")
    s2 = Student("Alice", 22, 22222, 3.5)

    print(s1)
    print(s2)