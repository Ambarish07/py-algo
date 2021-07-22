#User function template for Python 3
# from collections import Counter

class Solution:
    def majorityElement(self, a, n):
        if n == 0:
            return -1
        #Your code here
        count,majIdx = 1,0
        for i in range(n):
            if a[majIdx] == a[i]:
                count+=1
            else:
                count -=1 
            if count== 0:
                majIdx = i
                count = 1
            print(count,a[i],majIdx)
        ans = a[majIdx]
        cnt = 0
        for i in a:
            if i == ans:
                cnt += 1
        return ans if cnt > n//2  else -1


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends