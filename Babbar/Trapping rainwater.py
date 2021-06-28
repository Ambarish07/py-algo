class Solution:
    def trappingWater(self, arr,n):
        #Code here
        ans = 0
        mxl,mxr = [-1],[-1]
        mx = arr[0]
        for i in range(1,n):
            mx = max(mx,arr[i])
            mxl.append(mx)
        mx = arr[-1]
        for i in range(n-2,-1,-1):
            mx = max(mx,arr[i])
            mxr.append(mx)
        mxr.reverse()
        ans = 0
        for i in range(n):
            ans += max(min(mxl[i],mxr[i]) - arr[i],0)
        
        return ans
