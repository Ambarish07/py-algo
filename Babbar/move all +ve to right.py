def solve(arr):
    l,h = 0,len(arr)-1
    while l <= h:
        if arr[l] > 0 and arr[h] < 0:
            arr[l],arr[h] = arr[h],arr[l]
            l+=1
            h-=1
        elif arr[l] < 0:
            l +=1
        elif arr[h] > 0:
            h-=1
    return arr
    
print(solve([-12, 11, -13, -5, 6, -7, 5, -3, -6]))