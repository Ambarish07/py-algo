class Solution:
    def sb(self, a, n, x):
        # Your code goes here 
        i = j = 0
        sum = 0
        ans = float('inf')
        while j < n:
            if sum <= x:
                sum += a[j]
                j += 1
            while i < j and sum > x:
                ans = min(ans,j - i)
                sum -= a[i]
                i += 1
        return ans