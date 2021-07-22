class Solution:
    def fourSum(self, a, k):
        # code here
        ans= []
        a.sort()
        for x in range(len(a)-3):
            for y in range(x+1,len(a)-2):
                i,j = y+1,len(a)-1
                while i<j:
                    tmp = a[x]+a[y]+a[i]+a[j]
                    if tmp == k:
                        ans.append(sorted([a[x],a[y],a[i],a[j]]))
                        oldi,oldj = i , j
                        while i < j and i == oldi:
                            i+=1
                        while j > i and j == oldj:
                            j-=1
                    elif tmp < k:
                        i+=1
                    else:
                        j-=1
        # print(ans)
        ans = [list(x) for x in set(tuple(x) for x in ans)]
        # print(ans)
        return sorted(ans)

