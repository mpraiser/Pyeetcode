import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smaller = []  # 大顶堆
        self.bigger = []  # 小顶堆
    
    @property
    def nIsEven(self):
        return self.n % 2 == 0

    def addNum(self, num: int) -> None:
        # when n == 0, send one element to bigger first
        if len(self.smaller) == len(self.bigger):
            heapq.heappush(self.bigger, -heapq.heappushpop(self.smaller, -num))
        else:
            heapq.heappush(self.smaller, -heapq.heappushpop(self.bigger, num))

    def findMedian(self) -> float:
        if len(self.smaller) == len(self.bigger):
            return (- self.smaller[0] + self.bigger[0]) / 2
        else:
            return self.bigger[0]

obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()