class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        maxi = 0 
        
        for x in range(len(gain)):
            res += gain[x]
            if res > maxi:
                maxi = res

        return maxi

        