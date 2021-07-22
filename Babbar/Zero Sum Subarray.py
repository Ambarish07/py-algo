class Solution:
    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self,a,n):
        d,l = {},[]
        s = 0
        for i in range(n):
            s += a[i]
            if s == 0:
                l.append([0,i])
            tmp = []
            if s in d:
                tmp = d.get(s)
                for x in range(len(tmp)):
                    l.append([tmp[x],i])
            tmp.append(i)
            d[s] = tmp
        return len(l)