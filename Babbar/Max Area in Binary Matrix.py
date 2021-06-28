def getMaxArea(arr): # max area of histogram
    s = [-1]
    n = len(arr)
    area = 0
    i = 0
    left_smaller = [-1]*n
    right_smaller = [n]*n
    while i < n:
    	while s and (s[-1] != -1) and (arr[s[-1]] > arr[i]):
    		right_smaller[s[-1]] = i
    		s.pop()
    	if((i > 0) and (arr[i] == arr[i-1])):
    		left_smaller[i] = left_smaller[i-1]
    	else:
    		left_smaller[i] = s[-1]
    	s.append(i)
    	i += 1
    for j in range(0, n):
    	area = max(area, arr[j]*(right_smaller[j]-left_smaller[j]-1))
    return area

class Solution:
    def maxArea(self,a, n, m):
        for i in range(1,n):
            for j in range(m):
                if a[i][j] != 0:
                    a[i][j] += a[i-1][j]
        ans = float('-inf')
        for i in a:
            ans = max(ans,getMaxArea(i))
        return ans
        # return 0
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3



# Driver Code 
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R,C = map(int, input().strip().split())
        A = []
        for i in range(R):
            line = [int(x) for x in input().strip().split()]
            A.append(line)
        print(Solution().maxArea(A, R, C)) 
	