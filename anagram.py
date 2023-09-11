
def check(s1,s2):

    if len(s1)!=len(s2):
        return False
    
    ch_count1={}
    ch_count2={}

    for ch in s1:
        ch_count1[ch]=ch_count1.get(ch,0)+1

    for ch in s2:
        ch_count2[ch]=ch_count2.get(ch,0)+1

    
    if ch_count1==ch_count2:
        return True
    
    else:return False





    
