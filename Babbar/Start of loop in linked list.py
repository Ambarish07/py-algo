class Solution:
    def detectCycle(self, q: ListNode) -> ListNode:
        s,p,f = q,None,q
        while s and f and f.next:
            # p = f
            s = s.next
            f = f.next.next
            if f == s:
                break
        else:
            return
        s = q
        while f != s:
            f = f.next
            s = s.next
        return f