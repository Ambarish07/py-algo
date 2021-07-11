
def countRev (s):
    # your code here
    ans = open = 0
    for i in s:
        if i == '{':
            open+= 1
        elif open and i == '}':
            open -=1
        else:
            open+=1
            ans+=1
    if open % 2 == 1:
        return -1
    ans += open // 2 
    return ans

#{ 
#  Driver Code Starts

t = int (input ())
for tc in range (t):
    s = input ()
    print (countRev (s))

# Contributed By: Pranay Bansal

# } Driver Code Ends