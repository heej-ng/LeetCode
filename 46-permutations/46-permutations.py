class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        storage = []
        
        def dfs(element):
            if len(element) == 0:
                result.append(storage[:])
                
            for e in element:
                storage.append(e)
                
                next_element = element[:]
                next_element.remove(e)
                
                dfs(next_element)
                storage.pop()
                
        dfs(nums)
        return result
            
            
            
        