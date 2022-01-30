class Solution:
    def reverse(self, x: int) -> int:
        sign_flag = 1
        if x < 0:
            sign_flag = -1
            x *= -1
        result = 0
        out_bound = 2**31
        while x > 0:
            result = result * 10 + (x%10)
            x //= 10
        result *= sign_flag
        if result >= out_bound or result < -1*out_bound:
            return 0
        return result