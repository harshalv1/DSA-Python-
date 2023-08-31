def removdup(s):
    result=[] 
    for ch in s:
        if not result or ch!=result[-1]: #REV LOGIC if the list named result is empty which is likely in first iteration or the current charcter is not same as the last element the result list 
            result.append(ch)
        else:
            result.pop()

    return "".join(result)

s="geeksforgeeg"
print(removdup(s))