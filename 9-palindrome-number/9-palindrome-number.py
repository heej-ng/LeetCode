class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        input = []
        while x >= 10:
            input.append(x % 10)
            x //= 10
    
        input.append(x)
        print(input)


        #listlen = len(input)
        half = len(input)/2
        i = 0
        while(i < half):
            if input[i] != input[len(input) - i - 1]:
                return False
            i += 1
        
        return True