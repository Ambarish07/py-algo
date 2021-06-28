class Solution:
	def threeWayPartition(self, arr, a, b):
        n = len(arr)
        i = start = 0
        end = n-1
        while i <= end:
            if arr[i] < a:
                arr[i],arr[start] = arr[start],arr[i]
                i += 1
                start += 1
            elif arr[i] > b:
                arr[i],arr[end] = arr[end],arr[i]
                end -=1 
            else:
                i += 1
        