class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        ans = len(s[0])
        p = s[0]
        for i in s:
            x = 0
            c = 0
            while x<len(i) and x < ans and i[x] == p[x]:
                c += 1
                x += 1
            ans = min(ans,c)
        return s[0][:ans]