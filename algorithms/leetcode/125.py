def isPalindrome(s):
    new_string = ''
    for ch in s:
        if ch >= 'a' and ch  <= 'z':
            new_string += ch
        elif ch >= 'A' and ch  <= 'Z':
            new_string += chr(ord(ch) + 32)

    first_index = 0
    last_index = len(new_string) - 1

    first_index = 0
    last_index = len(new_string) - 1

    if len(new_string) == 0:
            return True 
    elif len(new_string) == 2 and (new_string[first_index] == new_string[last_index]):
        return True 
    elif len(new_string) == 2 and (new_string[first_index] != new_string[last_index]):
        return False
    elif len(new_string) == 1:
        return True
    
    print(last_index)
    print(first_index)
    while first_index != last_index:
        if new_string[first_index] != new_string[last_index]:
            return False
        first_index += 1
        last_index -= 1

    return True

s = '0P'
p = isPalindrome(s)
print(p)
