from bisect import bisect
class Solution:
    def median(self, m, r, c):
    	mi,mx = float('inf'),float('-inf')
    	for i in m:
    	    if i[0] < mi:
    	        mi = i[0]
    	    if i[c-1] > mx:
    	        mx = i[c-1]
        desired =(r*c + 1) // 2
        # print(mi,mx,desired)
        while mi < mx:
            ans = 0
            mid = (mi + mx) // 2
            for i in m:
                ans += bisect(i,mid)
            # print(mi,mx,mid,ans,desired)
            # if ans == desired:    #we will not put this statement cuz there can
                # return mid        # be value less than mid 
            if ans < desired:
                mi = mid+1
            else:
                mx = mid
        return mi
