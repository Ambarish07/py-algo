class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        ans = self.countAndSay(n-1)
        nn = len(ans)
        # print(ans,nn,n)
        tmp,tmpCount = '',1
        a = ''
        i = 0
        while i < nn:
            tmp,tmpCount = ans[i],1
            j = i+1
            while j < nn and ans[j] == tmp:
                tmpCount += 1
                j += 1
                i += 1
            a += str(tmpCount) + str(tmp)
            i += 1
        # print(a)
        return a