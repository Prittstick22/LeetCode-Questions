
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}

        for index, num in enumerate(nums):
            result = target - num
            if result in hashmap:
                return [hashmap[result], index]
            else:
                hashmap[num] = index
        return []
