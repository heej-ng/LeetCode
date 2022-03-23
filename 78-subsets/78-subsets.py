class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs(start: int, element):

            result.append(element)
            
            for i in range(start, len(nums)):
                temp = element+[nums[i]]
                # result.append(temp[:])
                dfs(i+1, temp)
                
        dfs(0,[])
        return result