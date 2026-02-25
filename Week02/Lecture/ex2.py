s = input("Enter a string: ")

mySet = set()
for ch in s:
    if ch.isalpha():
        """
        if ch not in mySet:
            mySet.add(ch)
        """
        mySet.add(ch)

print(len(mySet))