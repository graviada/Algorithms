from typing import List


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        temp = x
        reversedNum = 0

        while temp > 0:
            reversedNum = reversedNum * 10 + temp % 10
            temp //= 10

        return x == reversedNum or x == reversedNum // 10


sol = Solution()
print(sol.isPalindrome(1001))
print(100%10)