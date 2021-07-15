#User function Template for python3

class Solution:
    def findSubString(self, s):
        # Your code goes here
        # s = s.upper()
        dc = len(set(s))
        ans = len(s)
        i = j = 0
        tmp = {}
        i = j = 0
        while i < len(s):
            if i < dc-1:
                tmp[s[i]] = tmp.get(s[i],0) + 1
                i+=1
                continue
            tmp[s[i]] = tmp.get(s[i],0) + 1
            if len(tmp.keys()) == dc:
                ans = min(ans,i-j+1)
                while j < i and len(tmp.keys()) == dc:
                    ans = min(ans,i-j+1)
                    if tmp[s[j]] == 1:
                        tmp.pop(s[j])
                        j+=1
                        break
                    tmp[s[j]] -= 1
                    j+=1
            i+=1        
        return ans
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
    	str = input()
    	ob=Solution()
    	print(ob.findSubString(str))
    	
    	T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends