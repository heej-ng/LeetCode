class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs(element, start: int):
            if start == len(nums):
                return
            
            
            
            for i in range(start, len(nums)):
                temp = element+[nums[i]]
                print("i : "+str(i))
                print(temp)
                result.append(temp[:])
                
                dfs(temp, i+1)
                
                
        dfs([],0)
        result.append([])
        return result