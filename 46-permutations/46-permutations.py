class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        storage = []
        
        def dfs(elements):
            if len(elements) == 0:
                result.append(storage[:])
                
            for e in elements:
                storage.append(e)
                
                next_element = elements[:]
                next_element.remove(e)
                
                dfs(next_element)
                storage.pop()
                
        dfs(nums)
        return result
            
            
            
        