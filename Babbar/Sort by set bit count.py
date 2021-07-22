
class Solution:
    def sortBySetBitCount(self, a, n):
        # Your code goes here
        def count1(x):
            s = bin(x)
            ans = 0
            for i in s:
                if i == '1':
                    ans += 1
            return ans
        a.sort(key = count1,reverse =True)
        