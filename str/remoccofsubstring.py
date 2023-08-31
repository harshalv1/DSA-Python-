
def rem_occ_of_substring(s,part):
    
    while part in s:
        index=s.find(part)
        s=s[:index]+s[index+len(part):]
    return s
        

s = "axxxxxxyyyyyyb"
part = "xy"
print(rem_occ_of_substring(s,part))