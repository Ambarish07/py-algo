#code
l = [0,-1,-2,-8,8,10,60,-50,90]
def solve(l):
    if l[0] != None:
        mx,mn = l[0],l[0]
    else:
        return
    for i in l:
        if i > mx:
            mx = i
        elif i < mn:
            mn = i
    return [mx,mn]

print(*solve(l))