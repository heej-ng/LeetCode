class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        notval_endindex = len(nums)
        for i in range(len(nums)):
            if nums[i] != val:
                k += 1
            else:   # nums[i] == val case
                if notval_endindex-1 <= i:
                    break
                for j in range(notval_endindex-1,-1,-1):
                    if nums[j] != val and i < j:  # 뒤에서부터 val과 다른 값 search
                        ptr = nums[j]       # nums[i] <-> nums[j]
                        nums[j] = nums[i]
                        nums[i] = ptr
                        notval_endindex = j
                        k += 1
                        break
        return k