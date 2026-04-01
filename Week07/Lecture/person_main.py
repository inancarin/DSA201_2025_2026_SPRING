#from Person_class import Person
import Person_class as p

p1 = p.Person(ID=1, name="John", age=22) # p1 is an instance of Person class
p2 = p.Person(2, "Alice", 21) # p2 is an instance of Person class

print(p1.name, p1.myAge)

#p1.myAge = 24
p1.changeAge(24)

print(p1.name, p1.getAge())
print(p2.name, p2.getAge())

p1.printName()

print(p1)
print(p2)

people = [] # a list of people objects
people.append(p1)
people.append(p2)

print(people)