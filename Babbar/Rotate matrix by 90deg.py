# Flip the matrix then transpose it.

class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i,j = 0, len(m) - 1
        while i < j:
            m[i],m[j] = m[j],m[i]
            i += 1
            j -=1
        for i in range(len(m)):
            for j in range(i+1):
                m[i][j],m[j][i] = m[j][i],m[i][j]
        