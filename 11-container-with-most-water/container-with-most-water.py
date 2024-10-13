class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxim = 0
        start = 0
        end = len(height) - 1
        while start < end:
            if min(height[start],height[end]) * (end-start) > maxim:
                maxim = min(height[start],height[end]) * (end-start)
            if min(height[start], height[end]) == height[start]:
                start += 1
            else:
                end -= 1
        return maxim
        