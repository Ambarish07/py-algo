#User function Template for python3

class Solution:
    def longestPalin(self, s):
        # code here
        s1,s2 = s,s[::-1]
        dp = [[-1 for _ in range(len(s)+ 1)]   for _ in range(len(s) + 1)]
        def lps(x,y):
            # print(s1,s2)
            ans = ''
            mx,mxi,mxj = 0,x,y
            for i in range(x+1):
                for j in range(y+1):
                    if i == 0 or j == 0:
                        dp[i][j] = 0
                        continue
                    if dp[i][j] != -1:
                        continue
                    if s1[i-1] == s2[j-1]:
                        # ans += s1[i-1] 
                        dp[i][j] = 1+ dp[i-1][j-1]
                        if mx < dp[i][j]:
                            mx = dp[i][j]
                            mxi,mxj = i,j
                    else:
                        dp[i][j] = 0
                        
            for i in dp:
                print(*i)
            # print(mxi,mxj)
            if mx == 1:
                return s[0]
            i,j = mxi , mxj
            ans = ''
            while i>0 and j > 0:
                if s1[i-1] == s2[j-1]:
                    if dp[i][j] > 0:    
                        ans += s1[i-1] 
                        print(ans,dp[i][j],i,j)
                    i-=1
                    j-=1

            return ans
            
        return lps(len(s),len(s))
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalin(S)

        print(ans)
# } Driver Code Ends