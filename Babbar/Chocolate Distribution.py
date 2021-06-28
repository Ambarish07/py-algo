class Solution:

    def findMinDiff(self, A,N,M):
        A.sort()
        i,j = 0,M-1
        ans = float('inf')
        while j<N:
            ans = min(ans,A[j] - A[i])
            i+=1
            j+=1
        return ans