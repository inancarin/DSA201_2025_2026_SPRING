def isPangram(s):
    s = s.lower()
    
    letters = dict()
    for ch in s:
        if ch.isalpha():
            if ch not in letters:
                letters[ch] = 1
            else:
                letters[ch] += 1
    
    if len(letters) == 26:
        return "pangram"
    return "not pangram"
    

#s = "We promptly judged antique ivory buckles for the next prize"
s = "We promptly judged antique ivory buckles for the prize"
ans = isPangram(s)
print(ans)