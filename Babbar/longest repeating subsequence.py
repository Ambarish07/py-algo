#User function Template for python3

class Solution:
	def LongestRepeatingSubsequence(self, s):
		# Code here
		n = len(s)
		dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
		for i in range(n+1):
		    for j in range(n+1):
		        if i == 0 or j == 0:
		            dp[i][j] = 0
		            
		        elif s[i-1] == s[j-1] and i!= j:
		            dp[i][j] = 1+ dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1] )
                    
        # for i in dp:
        #     print(*i)
        return dp[n][n]
		

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution()
		ans = ob.LongestRepeatingSubsequence(str)
		print(ans)

# } Driver Code Ends