class Solution:
    
    # arr[] : the input array
    # N : size of the array arr[]
    
    #Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self,arr, N):
        #code here
        d = {}
        for i in arr:
            d[i] = 1
        firstEle = []
        for i in arr:
            if not d.get(i-1,None):
                firstEle.append(i)
        ans = 0
        for i in firstEle:
            tempAns = 0
            x = i
            while d.get(x,None):
                x += 1
                tempAns += 1
            ans = max(ans,tempAns)
        return ans
