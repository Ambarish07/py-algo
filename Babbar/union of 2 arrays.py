class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        a.extend(b)
        return len(set(a))
        #code here