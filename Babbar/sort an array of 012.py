class Solution:
    def sort012(self,arr,n):
        # code here
        count = [0,0,0]
        for i in arr:
            count[i] += 1
        for i in range(n):
            if count[0]:
                arr[i] = 0
                count[0] -= 1
            elif count[1]:
                arr[i] = 1
                count[1] -= 1
            elif count[2]:
                arr[i] = 2
                count[2] -= 1
        return arr