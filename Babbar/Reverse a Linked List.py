class Solution:                                              # Iterative
    #Function to reverse a linked list.
    def reverseList(self, q):
        # Code here
        prev , cur = None, q
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev
        





class Solution:                                               # Recusrive
    def reverseList(self, q):
        if q is None:
            return
        def rev(q):
            if q.next is None:
                return q,q
            tmp = q.next
            q.next = None
            x,h = rev(tmp)
            x.next = q
            return q,h
        return rev(q)[1]