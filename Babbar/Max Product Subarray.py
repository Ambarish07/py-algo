class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		minVal = maxVal = ans = arr[0]
		if arr[0] == 0:
		    maxVal = minVal = ans = 1 
		for i in range(1,n):
		    tmpMaxVal = maxVal
		    maxVal = max(arr[i],maxVal*arr[i],minVal*arr[i])
		    minVal = min(arr[i],minVal*arr[i],tmpMaxVal*arr[i])
		    ans = max(maxVal,minVal,ans)
		    if arr[i] == 0:
		        maxVal = minVal = 1
	       # print(maxVal,minVal,ans,arr[i])
		return ans