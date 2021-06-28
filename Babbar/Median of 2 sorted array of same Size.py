def solve(a,b):
    print(a,b)
    n,m = len(a),len(b)
    if n == m == 2:
        return (max(a[0],b[0]) + min(a[1],b[1])) / 2
    mida = a[n//2]
    midb = b[m//2]
    if mida < midb:
        return solve(a[ n//2 : ],b[ : m//2+1 ])
    else:
        return solve(a[  : n//2 +1  ],b[ m//2: ])



a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(solve(a,b))