class Solution:
    def search(self, n: List[int], t: int) -> int:
        l = len(n)
        if l == 0:
            return -1
        low,high = 0, l-1
        while low <= high:
            mid = ( low + high) //2
            # print(low,high,mid,n[mid])
            if n[mid] == t:
                return mid
            if n[low] <= n[mid] :
                if n[mid] >= t >= n[low]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if n[mid] <= t <= n[high]:
                    low = mid+1
                else:
                    high = mid - 1
        return -1