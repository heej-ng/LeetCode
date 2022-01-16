class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        input = []
        while x >= 10:
            input.append(x % 10)
            x //= 10
    
        input.append(x)

        listlen = len(input)
        half = listlen/2
        i = 0
        while(i < half):
            if input[i] != input[listlen - i - 1]:
                return False
            i += 1
        
        return True