class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        dic = {}
        k = 0
        i = 0
        while i < length:
            if nums[i] in dic:          # dic 안에 nums[i] key가 이미 존재
                if dic[nums[i]] >= 2:   # nums[i](value)가 2번 이미 존재
                    nums.pop(i)
                    length -= 1
                else:                   # value가 1번만 존재했던 경우
                    dic[nums[i]] = 2
                    i += 1
                    k += 1
            else:
                dic[nums[i]] = 1
                i += 1
                k += 1
        return i
