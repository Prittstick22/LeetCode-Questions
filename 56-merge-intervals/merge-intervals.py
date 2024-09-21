class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0]) # sort smallest to biggest looking at the first element in the sublist
        merged = []
        for interval in intervals:
            
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                #fix the last interval 
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
        