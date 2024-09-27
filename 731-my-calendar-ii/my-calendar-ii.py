class MyCalendarTwo:

    def __init__(self):
        self.booking = []
        self.overlaps = []

    

    def book(self, start: int, end: int) -> bool:

        for booking in self.overlaps:
            if self.overlap(booking[0],booking[1], start, end):
                return False

        for booking in self.booking:
            if self.overlap(booking[0],booking[1], start, end):
                self.overlaps.append(self.getting_overlap(booking[0],booking[1], start, end))
        
        self.booking.append((start,end))
        return True
    
    def overlap(self, start1: int, end1: int, start2: int, end2: int) -> bool:
        return max(start1,start2) < min(end1,end2)
    
    def getting_overlap(self, start1: int, end1: int, start2: int, end2: int) -> tuple:
        return max(start1,start2),min(end1,end2)


        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)