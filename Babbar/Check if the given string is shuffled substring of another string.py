#given str a and b and check if a is present in b in shuffled form
def solve(a,b):
    m,n = len(a),len(b)
    if m < n:
        return "NO"
    d,d1 = {},{}
    x = 0
    for i in a:
        d[i] = d.get(i,0) + 1
    for i in range(n):
        ans = True
        if i < m - 1:
            d1[b[i]] = d1.get(b[i],0) + 1
            continue
        
        d1[b[i]] = d1.get(b[i]) + 1
        print(d1)
        for j in d:
            if d[j] != d1.get(j,0):
                ans = False
        if ans is True:
            return "YES"
            
        d1[b[x]] -= 1
        x += 1
        
    return "NO"

    
    
a = input()
b = input()
print(solve(a,b))