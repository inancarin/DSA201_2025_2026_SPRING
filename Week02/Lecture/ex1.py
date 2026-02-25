s = input("Enter a string: ") # "izmir"

d = {}
for ch in s:
    if ch.isalpha():
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1

maxFreq = max(d.values())
for k, v in d.items():
    if v == maxFreq:
        print(k)
        break
