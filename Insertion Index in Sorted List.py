# SOLUTION 1
# class Solution:
#     def solve(self, arr, target):
#         return bisect.bisect(arr,target)


# SOLUTION 2
# class Solution:
#     solve = bisect.bisect          # don't know how it works...

# SOLUTION 3
# class Solution:
#     def solve(self, arr, target):
#         lo , hi = 0,len(arr)
#                 while lo <= hi:
#                     if lo == hi:
#                         return lo
#                     mid = lo + (hi-lo)//2
#                     # print(mid,lo,hi)
#                     if arr[mid-1] < target < arr[mid]:
#                         return mid
#                     if arr[mid] > target:
#                         hi = mid
#                         # print("mid > target")
#                     else:
#                         # print("else")
#                         lo = mid+1
#                 # print(lo,hi)
#                 return lo