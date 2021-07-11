
class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        m,n = len(a), len(b)
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                    continue
                if a[i-1] == b[j-1]:
                    dp[i][j] = 1+ dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
        # for i in dp:
        #     print(*i)
        return dp[m][n]