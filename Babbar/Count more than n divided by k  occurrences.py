class Solution:
    
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr,n,k):
        #Your code here
        d = {}
        ans = 0
        for i in arr:
            d[i] = d.get(i,0) + 1
        k = n // k
        for i in d.values():
            if i > k:
               ans += 1 
        return ans