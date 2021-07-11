#code
def solve(s):
    ans = 0
    c0 = c1 = 0
    for i in s:
        if i == '1':
            c1 += 1
        else:
            c0 += 1
        if c0 == c1:
            ans += 1 
    return ans if ans>0 else -1
    
print(solve('0111100010'))