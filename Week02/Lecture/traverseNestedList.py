def countElems(elems):
    count = 0
    for elem in elems:
        if isinstance(elem, str):
            count += 1
        elif isinstance(elem, list):
            count += countElems(elem)
    
    return count


names = ["Adam", ["Bob", ["Chet","Cat"], "Barb", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
res = countElems(names)
print(res)

