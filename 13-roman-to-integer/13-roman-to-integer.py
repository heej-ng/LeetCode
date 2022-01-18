class Solution:
    def romanToInt(self, s: str) -> int:
        dic = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }
        
        if len(s) == 1:
            return dic[s]
        value = 0
        post = dic[s[1]]
        for i in range(len(s)):
            ptr = dic[s[i]]
            if ptr >= post:  # 더하는 경우
                value += ptr
            else:           # 뺴는 경우
                value -= ptr
            if i <= len(s)-3:
                post = dic[s[i+2]]
        
        return value
