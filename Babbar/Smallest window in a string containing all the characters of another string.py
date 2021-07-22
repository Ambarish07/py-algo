class Solution:
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        #code here
        ans = float('inf')
        ansI,ansJ = 0,0
        def included(pd,sd):
            # print(sd,pd)
            for i,j in pd.items():
                # print(i,j)
                if sd.get(i,-1) < j:
                    # print(i,j,sd.get(i,-1))
                    return False
            # print(True)
            return True
        pd = {}
        for i in p:
            pd[i] = pd.get(i,0)+1
        i = j = 0
        sd =  {}
        while i < len(s):
            if i < len(p)-1:
                sd[s[i]] = sd.get(s[i],0)+1
                i+=1
                continue
            sd[s[i]] = sd.get(s[i],0)+1
            # print(sd)
            if included(pd,sd):
                # print("included",sd)
                while  j < i and included(pd,sd):
                    #print(s[j:i+1],sd)
                    if ans > i-j+1:
                        ansI,ansJ,ans = i,j,i-j+1
                    sd[s[j]] -= 1
                    j+=1
                    
            i+=1
        return s[ansJ:ansI+1] if ans != float("inf") else -1

if __name__=='__main__':
    s='timetopractice'
    p='toc'
    ob = Solution()
    print(ob.smallestWindow(s,p))

