def solve(a,x,k,i = 0):
    i = 0
    while i < len(a):
        if a[i] == k:
            return i
        i += max(1,int(abs(a[i] - x) // k))
        # print(i)
    return -1 
a = [2,4,5,7,7,6,5,4,3,2]
print(solve(a,2,6))