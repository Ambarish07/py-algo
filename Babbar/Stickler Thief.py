
#User function Template for python3

class Solution:  
    
    #Function to find the maximum money the thief can get.

    def FindMaxSum(self,a, n):                         # Space : O(n)
        # code here
        dp = [-1 for i in range(n)]
        def rec(i):
            # print(dp,i)
            if dp[i] != -1:
                return dp[i]
            if i == 0:
                dp[i] = a[i]
                return a[0]
            if i == 1:
                dp[i] = max(a[0],a[1])
                return dp[i]
            dp[i] = max(rec(i-1),rec(i-2)+a[i])
            return dp[i]
        return rec(n-1)
        
        def findMaxSum(self,a, n):                      # Space O(1)
            # code here
            i=e=0
            for x in a:
                tmp = max(i,e)
                i = e+x
                e = tmp
        return max(i,e)
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.FindMaxSum(a,n))
# } Driver Code Ends

