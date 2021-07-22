#given str a and b and check if a is present in b in shuffled form
def solve(m):
    r,c = len(m),len(m[0])
    if r==1 or c==1:
        return -1
    d = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if i == 0 or j == 0:
                d[i][j] = float('inf')
            elif i > 1 and j > 1:
                d[i][j] = min(d[i-1][j-1],d[i-1][j-2],d[i-2][j-1])
                # print(d[i][j],m[i-1][j-1],m[i-1][j-2],m[i-2][j-1],i,j)
            else:
                m1 = m[i-1][j-1]
                m2 = m[i-2][j-1] if i>1 else float('inf')
                m3 = m[i-1][j-2] if j>1 else float('inf')
                d[i][j] = min(m1,m2,m3)
    
    ans = float('-inf')

    for i in range(r):
        for j in range(c):
            tmp = m[i][j] - d[i][j]
            ans = max(ans,tmp)
    return ans

    

# b = [[ -29, 2, -1, -4, -20 ],
#       [ -8, -3, 4, 2, 1 ],
#       [ 3, 8, 6, 1, 3 ],
#       [ -4, -1, 1, 7, -6 ],
#       [ 0, -4, 10, -5, 50 ]];


b = [[-1,-10],[0,2]]
print(solve(b))