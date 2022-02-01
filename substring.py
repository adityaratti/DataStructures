def strstr(Str, target):
    t = 0
    Len = len(Str)
    i = 0

    # Iterate from 0 to Len - 1
    for i in range(Len):
        if t != 0:
            if Str[i] != target[t]:
                t = 0
        if Str[i] == target[t]:
            t += 1
        if t == len(target):
            return i - t+1


# Driver code
# print(strstr("GeeksForGeeks", "Fr"))
print(strstr("GeeksFoForrGeeks", "For"))


def is_substr(str, substr):
    i = 0
    j=0

    while i < len(str):
        if str[i] == substr[j]:
            j +=1
            while j < len(substr):
                if str[i+j] != substr[j]:
                    break
                else:
                    j+=1
                    
            if j == len(substr):
                return i
            else:
                i = i+j-1
                j=0
        i +=1
    return -1
print('is_substr')                 
print(is_substr("GeeksFoForrGeeks", "For"))