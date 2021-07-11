#User function Template for python3
from collections import Counter
class Solution:
    def secFrequent(self, a, n):
        # code here
        c = Counter(a)
        # print(c,c.items())
        mx,mx1,ans,ans1 = -1,-2,"",""
        for i,j in c.items():
            # print(i,j)
            if j > mx:
                mx1,ans1 = mx,ans
                mx,ans = j,i
                # print(mx1,ans1)
            elif j> mx1:
                mx1,ans1 = j,i
        return ans1
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        arr = input().strip().split(" ")
        ob = Solution()
        ans = ob.secFrequent(arr,n)
        print(ans)
# } Driver Code Ends