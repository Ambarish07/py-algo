#User function Template for python3

class Solution:

    def findPair(self, a, l,n):
        #code here
        a.sort()
        i,j = 1,0
        while i < l:
            if a[i] - a[j] == n:
                return True
            if a[i] - a[j] > n:
                j+=1
            else:
                i+=1
        return False
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        L,N = [int(x) for x in input().split()]
        arr = [int(x) for x in input().split()]

        solObj = Solution()

        if(solObj.findPair(arr,L, N)):
            print(1)
        else:
            print(-1)
# } Driver Code Endshttps://media.geeksforgeeks.org/img-practice/check-square-1596781127.svg