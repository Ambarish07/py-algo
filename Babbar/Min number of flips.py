#User function Template for python3


class Solution:
    def minFlips(self, s):
        # Code here
        s = list(s)
        tmp = s[:]
        if len(s) == 1:
            return 0
        f1 = f2 = 0
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                f1 += 1
                s[i] = str((int(s[i-1]) + 1) % 2)
        # print(s)
        s = tmp
        s[0] = '1' if s[0] is '0' else '0'
        # print(s)
        f2 += 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                f2 += 1
                s[i] = str((int(s[i-1]) + 1) % 2)
        # print(f1,f2,s)
        return min(f1,f2)


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        S=input()
        Obj=Solution()
        ans=Obj.minFlips(S)
        print(ans)
# } Driver Code Ends