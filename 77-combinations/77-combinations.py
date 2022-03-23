class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def dfs(element, start: int, k: int):
            # leaf node인 경우
            if k == 0:
                result.append(element[:])
                return
            
            for i in range(start, n+1): # start ~ n
                element.append(i)
                dfs(element, i+1, k-1)
                element.pop()
                
        dfs([],1,k)
        return result