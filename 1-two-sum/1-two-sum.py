class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, value in enumerate(nums):
            remain = target - value
            
            if remain in map:
                return [i, map[remain]]
            
            map[value] = i