class Solution:
    def canPlaceFlowers(self, flowerbed, n):

        count = 0
        zeros = 1

        for plot in flowerbed:
            if plot == 0:
                zeros += 1
            else:
                count += (zeros - 1) // 2
                zeros = 0

        zeros += 1
        count += (zeros - 1) // 2

        return count >= n