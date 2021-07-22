class Solution:
    def reverse(self,q, k):
        # Code here
        count = 0
        p,c,n = None,q,None
        while c and count < k:         # reverse the k elements
            n = c.next
            c.next = p
            p = c
            c = n
            count += 1
        if n is not None:
            q.next = self.reverse(n,k)
        return p
