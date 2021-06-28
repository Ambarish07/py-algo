class Solution:
     
    #Function to find if there exists a triplet in the 
    #array A[] which sums up to X.
    def find3Numbers(self,a, n, x):
        # Your Code Here
        a.sort()
        for i in range(n-2):
            start,end= i+1,n-1
            while start < end:
                tmp = a[i] + a[start]+ a[end]
                if tmp == x:
                    return True
                elif tmp < x:
                    start += 1
                else:
                    end -= 1
        return False