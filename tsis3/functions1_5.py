def next_permutation(s):
    L = []
    for i in s:
        L.append(i)
     
    n = len(L)
 
    #------------------------------------------------------------
 
    # Step 1: find rightmost position i such that L[i] < L[i+1]
    i = n - 2
    while i >= 0 and ord(L[i]) >= ord(L[i+1]):
        i -= 1
     
    if i == -1:
        return False
 
    #------------------------------------------------------------
 
    # Step 2: find rightmost position j to the right of i such that L[j] > L[i]
    j = i + 1
    while j < n and ord(L[j]) > ord(L[i]):
        j += 1
    j -= 1
     
    #------------------------------------------------------------
 
    # Step 3: swap L[i] and L[j]
    L[i], L[j] = L[j], L[i]
     
    #------------------------------------------------------------
 
    # Step 4: reverse everything to the right of i
    left = i + 1
    right = n - 1
 
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
             
    change(L)
    return True
    
def change(L):
    global s
    s = ''.join(L)

s = input()
while(next_permutation(s)):
    print(s)