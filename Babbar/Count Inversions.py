class Solution:
    def __init__(self):
        self.count = 0
    def mergeSort(self,arr):
        n = len(arr)
        if n < 2:
            return 0
        mid = n //2
        S1 = arr[0:mid]
        S2 = arr[mid:n]
        self.mergeSort(S1)
        self.mergeSort(S2)
        # print(S1,S2)
        self.merge(S1,S2,arr)
        # print(arr)
        return self.count
        
    def merge(self,a,b,arr):
        i = j = k = 0
        # print(a,b)
        while i < len(a) and j < len(b):
            # print(a[i],b[j])
            if a[i] <= b[j]:
                arr[k] = a[i]
                i+= 1
                # print("if",self.count)
            else:
                arr[k] = b[j]
                j+=1
                self.count += len(a)-i        # MOST IMPORTANT STEP!!!!
                # print("else",self.count)
            k+=1
        while i < len(a):
            arr[k] = a[i]
            i+=1
            k+=1
        while j < len(b):
            arr[k] = b[j]
            j+=1
            k+=1
    
    def inversionCount(self, arr, n):
        # Your Code Here
        if n == 1:
            return 0
        return self.mergeSort(arr)
        
                
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends