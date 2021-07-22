def findIntersection(p,q):
    #return head
    ans = Node(0)
    head = ans
    while q and p:
        # print(q.data,p.data)
        if p.data == q.data:
            ans.next = p
            ans = ans.next
            p = p.next
            q = q.next
        elif p.data < q.data:
            p = p.next
        else:
            q = q.next
    return head.next
    