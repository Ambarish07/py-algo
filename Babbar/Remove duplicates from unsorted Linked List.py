class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        q,p = head,None
        d = {}
        while q:
            if q.data in d:
                p.next = q.next or None
            else:
                d[q.data] = 1\
                p = q
            q = q.next
        return head
        