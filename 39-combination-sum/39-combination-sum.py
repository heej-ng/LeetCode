class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(temp, value: int, start: int):
            if value > target:
                return
            
            if value == target:
                result.append(temp[:])
                return
            
            for i in range(start, len(candidates)):
                dfs(temp+[candidates[i]], value+candidates[i], i)
                
        dfs([], 0, 0)
        return result