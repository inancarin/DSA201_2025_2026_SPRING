def findMostFreq(myList):
    #d = {}
    d = dict()

    for elem in myList:
        """
        if elem in d:
            d[elem] += 1
        else:
            d[elem] = 1
        """
        if elem not in d:
            d[elem] = 0
        d[elem] += 1
    
    maxValue = max(d.values())
    
    temp = []
    for k, v in d.items():
        if v == maxValue:
            temp.append(k)
    
    return min(temp)

a = [7,1,2,1,5,3,5,4,5,1]
res = findMostFreq(a)
print(res)