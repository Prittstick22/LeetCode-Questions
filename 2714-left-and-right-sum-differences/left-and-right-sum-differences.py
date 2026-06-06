class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        size = len(nums)
        leftsum = [0]*size
        rightsum = [0]*size
        for i in range(1, size):
            leftsum[i] = nums[i-1] + leftsum[i-1]
            #[10, 4, 8, 3]
            #[0, 10, 14, 22]

        for j in range(size-2,-1,-1):
            rightsum[j] = nums[j+1] + rightsum[j+1]
            #[10, 4, 8, 3]
            #[15, 11, 3, 0]
        
        for x in range(0,size):
            leftsum[x] = abs(leftsum[x] - rightsum[x])

        return leftsum


        