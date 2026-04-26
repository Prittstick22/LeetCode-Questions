class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandies = max(candies)
        ans = [False] * len(candies)
        for i in range(0,len(candies)):
            if candies[i] + extraCandies >= maxcandies:
                ans[i] = True
            
        return ans
