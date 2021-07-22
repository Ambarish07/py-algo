#User function Template for python3
# from collections import Counter
class Solution:
    def removeConsecutiveCharacter(self, s):
        # code here
        ans = [s[0]]
        for i in s:
            if i != ans[-1]:
                ans.append(i)
        return "".join(ans)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        s = input()
        ob = Solution()
        print(ob.removeConsecutiveCharacter(s))

# } Driver Code Ends