
def romanToDecimal(s):
    # code here
    d = {'I':1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,
        "IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900
    }
    ans = 0
    if len(s) == 1:
        return d[s[0]]
    i = 0
    while i < len(s):
        
        if i == len(s)-1:
            ans += d[s[i]]
            return ans
        tmp = d.get(s[i:i+2],None)
        # print(ans,s[i:i+2],i,tmp)
        if not tmp:
            ans += d.get(s[i])
            i+=1
        else:
            ans += tmp
            i+=2
    return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3




if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        print(romanToDecimal(str(input())))
# } Driver Code Ends