class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return self.name
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
class Course:
    def __init__(self, code, CRN, capacity):
        self.code = code
        self.CRN = CRN
        self.capacity = capacity
        self.currentPopulation = 0
        self.students = []
    
    def __str__(self):
        return self.code + " with CRN: " + str(self.CRN)

class Student(Person):
    def __init__(self, name, age, id, university="Sabanci University"):
        super().__init__(name, age)
        self.id = id
        self.university = university
        self.courses = []
    
    def register(self, course):
        if course not in self.courses:
            if course.currentPopulation < course.capacity:
                self.courses.append(course)
                course.currentPopulation += 1
                course.students.append(self)
                print("Registratation of", self.name, "to course", course, "is successful")
            else:
                print("There is no capacity for", self.name, "for course", course)
        else:
            print(self.name, "has already registered to", course)
    
    def printCourses(self):
        if len(self.courses) > 0:
            print("\nThe courses taken by", self.name, ":")
            for c in self.courses: # [sps101, dsa201, ..]
                print(c)
        else:
            print(self.name, "has not registered any course yet")

class FacultyMember(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id
        self.teachingCourses = []
    
    def teachCourse(self, course):
        if course not in self.teachingCourses:
            self.teachingCourses.append(course)
        else:
            print("you are already teaching", course)


# main
s1 = Student("Bob", 20, 1, "Sabanci University")
s2 = Student("Alice", 21, 2, "Sabanci University")
s3 = Student("Inanc", 21, 3, "Sabanci University")

dsa201 = Course(code="DSA201", CRN=11111, capacity=2)
sps101 = Course(code="SPS101", CRN=22222, capacity=1)


s1.register(dsa201) # proceed
s1.register(sps101) # proceed
s1.register(sps101) # no proceed
s2.register(sps101) # no proceed

# print all courses taken by s1
s3.printCourses()
s1.printCourses()