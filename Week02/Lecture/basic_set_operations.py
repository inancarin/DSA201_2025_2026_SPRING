x = set()
x.add("istanbul")
x.add("ankara")
x.add("antalya")
x.add("ankara")
x.remove("antalya")
# x.remove("izmir") -> not working
print(x)

s = input("Enter a string: ")
if s in x:
    print("YES")
else:
    print("NO")