def reverseWord(s):
    #your code here
    i,j = 0,len(s) - 1 
    s = list(s)
    while i < j:
        s[i],s[j] = s[j],s[i]
        i += 1
        j-= 1
    ans = ""
    for i in s:
        ans += i
    return ans