'''
count = 1
def solnByAdityaVerma(ip,op = ''):
    global count
    if len(ip) == 0:
        print(op,count)
        count += 1
        return
    op1,op2 = op,op+ip[-1]
    ip = ip[:-1]
    solnByAdityaVerma(ip,op1)
    solnByAdityaVerma(ip,op2)
'''



  # My soln
def solve(s):
    if s == '':
        return [ '' ]
    ans = solve(s[:-1])
    d = {}
    # print(ans)
    for i in ans:
        d[i] = 1
        d[i+s[-1]] = 1
    return list(d.keys())


b = input()
# solnByAdityaVerma(b)
print(*solve(b)[1:])