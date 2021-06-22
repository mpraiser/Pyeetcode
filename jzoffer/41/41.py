from collections import deque


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.n = 0
        self.buffer = []
    
    @property
    def nIsEven(self):
        return self.n % 2 == 0

    def addNum(self, num: int) -> None:
        self.n += 1
        self.buffer.append(num)

    def findMedian(self) -> float:
        if self.n <= 0:
            return None
        self.buffer.sort()
        if self.nIsEven:
            return (self.buffer[(self.n-1)//2] + self.buffer[(self.n-1)//2 + 1]) / 2
        else:
            return self.buffer[(self.n-1)//2]
        

obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()