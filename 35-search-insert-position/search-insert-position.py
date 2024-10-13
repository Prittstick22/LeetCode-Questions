class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        
        
        def binarySearch(nums, target, l, r):
            if l > r:
                return l
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                return binarySearch(nums, target, mid + 1, r)
            else:
                return binarySearch(nums, target, l, mid - 1)
    
        return binarySearch(nums, target, 0, len(nums) - 1)

    



