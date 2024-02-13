def isValid(s):
    if len(s) == 1:
        return False
    
    hashMap = {"parenthsis" : 0, "hardblock": 0, "squickly": 0}

    for idx in range(len(s)):
        if s[idx] == '(' or s[idx] == ')':
            hashMap["parenthsis"] += 1
        elif s[idx] == '[' or s[idx] == ']':
            hashMap["hardblock"] += 1
        elif s[idx] == '{' or s[idx] == '}':
            hashMap["squickly"] += 1
    
    for key, values in hashMap.items():
        if values % 2 != 0:
            return False
    return True 

s = "()[]{}"
string = isValid(s)
print(string)
