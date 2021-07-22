
class Solution:
    def hasCycle(self, q: ListNode) -> bool:         # Recursive (Worked in Leetcode)
        if q is None:
            return False
        if type(q.val) == str:
            return True
        q.val = str(q.val)
        return self.hasCycle(q.next)





class Solution:
    def hasCycle(self, q: ListNode) -> bool:         # Iterative
        slow = q
        fast = q
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False