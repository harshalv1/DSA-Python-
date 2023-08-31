#It calculates the number of ways to climb a staircase with n steps starting from 0th step
#using a combination of taking either 1 step or 2 steps at a time.

def ways(n):
    if n<0: #there cannot be less than 0 stairs at a time 
        return 0 #if that's the case return 0
    elif n==0: # if you are on the 0th step and want to reach 0th step 
        return 1 #there is only one way

    return ways(n-1)+ways(n-2) #aakhri nth step par jane ke liye ya to aap n-1 step se 
#chalang mari hogi wa n-2th step se 

res=ways(1)
print(res)
