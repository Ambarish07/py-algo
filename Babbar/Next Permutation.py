#User function Template for python3

class Solution:
    def nextPermutation(self, n, a):
        # code here
        for i in range(n-2, -2,-1):
            if i == -1:
                return sorted(a)
            else:
                if a[i] < a[i+1]:
                    j = i+1
                    tmp = i+1
                    while tmp < n:
                        if a[j] > a[tmp] > a[i]:
                            j = tmp
                        tmp += 1
                    a[i],a[j] = a[j],a[i]
                    break
        a[i+1:] = sorted(a[i+1:])
        return a
                        
                        
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends