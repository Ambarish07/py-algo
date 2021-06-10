
# Implement using max heap


from heapq import heapify as hp ,heappush as push,heappop as pop
class Solution:
    def __init__(self):
        self.l = []
        hp(self.l)
    def kthSmallest(self,arr, l, r, k):
        for i in arr:
            push(self.l, -1 * i)
            if len(self.l) > k:
                pop(self.l)
        return -1 * pop(self.l)
        
            