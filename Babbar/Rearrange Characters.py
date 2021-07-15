#code
def solve(a):
    d = {}
    for i in a:
        d[i] = d.get(i,0)+1
    m = max(d.values())
    if m <= len(s) // 2:
        return 1
    else:
        return 0
    
    
    
for _ in range(int(input())):
    s = input()
    print(solve(s))
