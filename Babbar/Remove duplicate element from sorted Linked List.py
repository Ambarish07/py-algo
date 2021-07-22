def removeDuplicates(q):
    #code here
    while q:
        if q.next and q.data == q.next.data:
            q.next = q.next.next or None
            continue
        q = q.next
