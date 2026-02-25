def findFreqs(names, d):
    for elem in names:
        if isinstance(elem, str):
            if elem not in d:
                d[elem] = 1
            else:
                d[elem] += 1
        elif isinstance(elem, list):
            findFreqs(elem, d)
        
names = ["Adam", ["Bob", ["Alex","Bob"], "Barb", "Bert"], 
         "Alex", ["Bea", "Alex"], "Ann"]
d = {} # empty dictionary
findFreqs(names, d)
print(d)

# a = [10, 20, 30] -> list
# b = (10, 20, 30) -> tuple

# immutable -> float, int, str
# mutable -> list