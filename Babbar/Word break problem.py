#User function Template for python3
def solve(line,d):
    if line == '':
        return 1
    for i in range(len(line) - 1 , -1,-1):
        tmp = line[i:]
        if d.get(tmp,False):
            return solve(line[:i],d)
    return 0
    
def wordBreak(line, d):
    # Complete this function
    dd = {}
    for i in d:
        dd[i] = 1
    return solve(line,dd)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		number_of_elements = int(input())
		dictionary = [word for word in input().strip().split()]
		line = input().strip()
		res = wordBreak(line, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends