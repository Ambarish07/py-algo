def maxSubArraySum(self,a,size):
    max_so_far = a[0]
    max_ending_here = 0
    for i in range(size):
        max_ending_here += a[i]
        max_ending_here = max(max_ending_here,a[i])
        max_so_far = max(max_ending_here,max_so_far)
    return max_so_far
