class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost = sorted(cost)
        n = len(cost) - 1
        total = 0
        if n == -1:
            return total 
        if n == 0:
            return cost[0]
        

        while n-2 >= 0:
            total += cost[n] + cost[n-1]
            n -= 3
        
        if n == 0:
            return total + cost[n]
        if n == 1:
            return total + cost[n] + cost[n-1]
        return total
        
        
        


        