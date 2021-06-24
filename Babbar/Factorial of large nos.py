
class Solution:
    def appendInArray(self,arr,n):
        while n:
            arr.append(n%10)
            n = n//10
    
    def factorial(self, n):
        ans = [1]
        carry = 0
        while n:
            for i in range(len(ans)):
                # print(ans,carry,n)
                temp = ans[i]
                no = temp * n + carry
                ans[i] = no % 10
                carry = no // 10
            self.appendInArray(ans,carry)
            carry = 0
            n -= 1
        ans.reverse()
        return ans
