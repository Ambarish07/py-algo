#User function Template for python3
def bs(a,n,t):
    ans = [-1,-1]
    i = 0
    j = n-1
    while i <= j:
        mid = (i+j) //2
        if arr[mid] == t:
            ans[0] = mid
            j = mid - 1               # get left most
        elif arr[mid] > t:
            j = mid -1
        else:
            i =mid+1
    i,j = 0,n-1
    while i <= j:
        mid = (i+j) // 2
        if arr[mid] == t:
            ans[1] = mid
            i = mid + 1               # get right most
        elif arr[mid] > t:
            j = mid -1
        else:
            i = mid+1
            
    return ans
def find(arr,n,x):
    return bs(arr,n,x)

#{ 
#  Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends