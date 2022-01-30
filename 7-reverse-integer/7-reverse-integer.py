class Solution:
    def reverse(self, x: int) -> int:
        nega_flag = 0
        if x < 0:
            nega_flag = 1
            x *= -1
        list = []
        while x > 0:
            list.append(x%10)
            x //= 10
        leng = len(list)
        k = 0
        for i in range(leng):
            k += list[i] * (10**(leng-1-i))
        if nega_flag == 1:
            k *= -1
        if k >= 2**31 or k < -1*(2**31):
            k = 0
        return k