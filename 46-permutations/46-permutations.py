class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        storage = []
        
        def dfs(element):
            print(element)
            if len(element) == 0:
                result.append(storage[:])
            
            for e in element:
                next_element = element[:]
                next_element.remove(e)

                storage.append(e)
                dfs(next_element)
                storage.pop()
                
        dfs(nums)
        
        return result
        