def isValid(s):
    if len(s) == 1:
        return False
    
    for idx in range(len(s)):
        if idx != len(s) - 1:
            if s[idx] == '(' and s[idx + 1] != ')':
                return False
            elif s[idx] == '{' and s[idx + 1] != '}':
                return False
            elif s[idx] == '[' and s[idx + 1] != ']':
                return False
    return True 

s = "()[]{}"
string = isValid(s)
print(string)
