class Solution:				# Recursive
    def addOne(self,head):
        #Returns new head of linked List.
        def add(q):
            if q.next == None:
                q.data += 1
                carry = q.data//10
                q.data %= 10
                return carry
            c = add(q.next)
            q.data += c
            c = q.data// 10            
            q.data %= 10
            return c
        c = add(head)
        cc= head
        if c!=0:
            cc = Node(c)
            cc.next = head
        return cc

