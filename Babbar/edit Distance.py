class Solution:
    def lcs(self, a,b):
        m,n = len(a), len(b)
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    dp[i][j] = i if j == 0 else j
                    continue
                if a[i-1] == b[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j] , dp[i][j-1],dp[i-1][j-1])
        
        return dp[m][n]
    
    
	def editDistance(self, a,b):
		# Code here
		x = self.lcs(a,b)
		return x
		

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s, t = input().split()
		ob = Solution();
		ans = ob.editDistance(s, t)
		print(ans)
# } Driver Code Ends