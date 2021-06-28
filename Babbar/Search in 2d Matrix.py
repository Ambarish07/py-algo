class Solution:
    def searchMatrix(self, m: List[List[int]], t: int) -> bool:
        i = j = 0
        r,c = len(m),len(m[0])
        for i in m:
            if i[0] <= t <= i[-1]:
                break
        for k in i:
            if k == t:
                return True
        return False
                