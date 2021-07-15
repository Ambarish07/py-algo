#User function Template for python3

class Solution:
    def findTwoElement( self,a, n): 
        # code here
        ans = [0,0]
        for i in range(n):
            x = int(a[i])
            if type(a[x - 1]) == str:
                ans[0] = x
                continue
            a[x-1] = str(a[x-1])
        for i in range(n):
            if type(a[i]) == int:
                ans[1] = i+1
                break
        return ans
            
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends