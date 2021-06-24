class Solution:
    
    def getPairsCount(self, arr, n, k): # k = target sum
        d = defaultdict(int)
        ans = 0
        for i in range(n):
            
            tofind = k - arr[i]
            ans += d[tofind]
            d[arr[i]] += 1
        return ans
