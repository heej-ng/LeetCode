class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        pre = nums[0]
        k = 1
        for i in range(1, len(nums)):
            if pre != nums[i]:      # pre != nums[i] 경우
                nums[k] = nums[i]
                pre = nums[i]
                k += 1      
        return k