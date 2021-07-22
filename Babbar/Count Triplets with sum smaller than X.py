
class Solution:
    def countTriplets(self, a, n, t):
        #code here
        a.sort()
        i,j,k = 0,1,n-1
        ans = 0
        for x in range(n):
            i = x + 1
            j = n-1
            while i < j:
                tmp = a[i] + a[j] +a[x]
                # print(x,i,j)
                if tmp < t:
                    ans += j-i
                    i += 1
                else:
                    j -= 1
        return ans