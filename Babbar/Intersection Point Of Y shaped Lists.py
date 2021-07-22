def intersetPoint(p,q):
    #code here
    while p:
        p.data = str(p.data)
        p = p.next
    while q:
        if type(q.data) == str:
            return int(q.data)
        q = q.next
    return -1
    