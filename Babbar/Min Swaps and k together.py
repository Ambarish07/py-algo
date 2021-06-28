def getCount(arr,n,k):
    count = 0
    for i in range(n):
        if arr[i] <= k:
            count += 1
    return count
def minSwap (arr, n, k) : 
    #Complete the function
    c = getCount(arr,n,k)
    ans = float(-1)
    j = 0
    tmp = 0
    for i in range(n):
        if i < c - 1:
            if arr[i] <= k:
                tmp += 1
            i += 1
            continue
        else:
            if arr[i] <= k:
                tmp += 1
            ans = max(tmp,ans)
            # print(ans,arr[i],tmp,i,j)
            if arr[j] <= k:
                tmp -= 1
            j += 1
    return c - ans
    