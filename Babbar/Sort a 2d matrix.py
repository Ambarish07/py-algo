class Solution:
    def sortedMatrix(self,n,m):
        #code here
        temp = []
        for i in m:
            temp.extend(i)
        temp.sort()
        m = []
        i = 0
        t = []
        for i in range(n*n):
            t.append(temp[i])
            if (i+1) % n == 0:
                m.append(t)
                t = []  
        return m