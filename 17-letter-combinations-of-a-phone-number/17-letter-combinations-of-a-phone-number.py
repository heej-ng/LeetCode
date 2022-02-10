class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        dic = { "2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz" }
        result = [""]
        for i in digits:
            digit = dic[i]
            print(digit)
            list = []
            for j in digit:     # j : (d or e or f)
                for k in range(len(result)):
                    temp = result[k]
                    temp += j
                    list.append(temp)
            result = list
        return result