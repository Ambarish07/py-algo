class Solution:
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,m, R, C): 
        visited = [[False for _ in range(C)] for _ in range(R)]
        r = c = di = 0
        count = r*c
        ans = []
        if len(m) == 0:
            return ans
        dr,dc = [0,1,0,-1],[1,0,-1,0]
        for i in range(R*C):
            ans.append(m[r][c])
            visited[r][c] = True
            cr,cc = r+dr[di],c+dc[di]
            if 0<=cr<R and 0<=cc<C and not visited[cr][cc]:
                r = cr
                c = cc
            else:
                di = (di+1)%4
                r += dr[di]
                c += dc[di]
        return ans
       
'''
METHOD 2

class Solution:
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,m, r,c): 
        i = j = di = 0
        dr,dc = [0,1,0,-1],[1,0,-1,0]
        ans = []
        v = [[False for _ in range(c)] for _ in range(r)]
        for _ in range(r*c):
            if not v[i][j]:
                ans.append(m[i][j])
                v[i][j] = True
            i += dr[di]
            j += dc[di]
            if 0<=i<r and 0<=j<c and not v[i][j]:
                continue
            else:
                i -= dr[di]
                j -= dc[di]
                di = (di + 1) % 4
                i,j = i+dr[di],j+dc[di]
        return ans
'''   