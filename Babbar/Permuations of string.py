#User function Template for python3
ans = []
class Solution:
    
    def permute(self,a, l, r):
        global ans
        if l==r:
            ans.append(''.join(a))
        else:
            for i in range(l,r+1):
                a[l], a[i] = a[i], a[l]
                self.permute(a, l+1, r)
                a[l], a[i] = a[i], a[l]
        return sorted(ans)
    
    
    def find_permutation(self, s):
        # Code here
        global ans
        ans.clear()
        return self.permute(list(s),0,len(s)-1)
        
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends