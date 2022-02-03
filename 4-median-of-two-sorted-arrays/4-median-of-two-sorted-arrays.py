class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n,m = len(nums1), len(nums2)
        length = n+m
        median = length/2
        median_i = length//2
        # print(median*10%10) # 나머지가 5일시 length 홀수, 0일시 length 짝수
        # 길이 4일때 median : 2,    중간값 인덱스는 (0 ~ 3) 중에 (1,2)
        # 길이 5일때 median : 2.5,  중간값 인덱스는 (0 ~ 4) 중에 (2)
        i,j = 0,0
        array = []
        while i+j <= median:
            if i == n or j == m:
                break
            if nums1[0] <= nums2[0]:    # nums1 < nums2
                array.append(nums1[0])
                del nums1[0]
                i += 1
            elif nums1[0] > nums2[0]:   # nums2 < nums1
                array.append(nums2[0])
                del nums2[0]
                j += 1
        array += nums1
        array += nums2
        if median*10%10 == 5:   # length odd 
            return array[median_i]
        elif median*10%10 == 0: # length even
            return (array[median_i-1]+array[median_i])/2