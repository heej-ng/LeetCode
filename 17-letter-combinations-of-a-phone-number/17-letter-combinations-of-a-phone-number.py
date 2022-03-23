class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        dic = { "2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz" }
        result = []
        def dfs(element, digits):
            if len(digits) == 0:
                result.append(element)
                return
            
            for i in dic[digits[0]]: # a b c
                element += i
                dfs(element, digits[1:])
                element = element[:len(element)-1]
                
        dfs("", digits)
        return result
                
