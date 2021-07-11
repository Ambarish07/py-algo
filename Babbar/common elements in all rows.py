from collections import defaultdict
def solve(m):
    r,c = len(m),len(m[0])
    d = defaultdict(set)
    for i in range(r):
        for j in range(c):
            d[m[i][j]].add(i)
    ans = []
    # print(d)
    for i,j in d.items():
        # print(i,j)
        if len(j) == r:
            ans.append(i)
    return ans
        

b = [[1, 2, 1, 4, 8],
       [3, 7, 8, 5, 1],
       [8, 7, 7, 3, 1],
       [8, 1, 2, 7, 9]]
print(solve(b))