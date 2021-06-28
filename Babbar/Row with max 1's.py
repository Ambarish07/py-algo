class Solution:
	def rowWithMax1s(self,a, n, m):
		i,j = 0,m-1
		ans = 0
		mx1 = 0
		gotOne = False
		while i < n and j >= 0:
		    if a[i][j] == 1:
		        mx1 += 1
		        gotOne = True
		        ans = i
		        j-=1
            else:
                i+=1
        return ans if gotOne else -1
		
		
		