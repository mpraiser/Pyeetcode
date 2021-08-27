import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lower = []
        self.higher = []
        heapq.heapify(self.lower)
        heapq.heapify(self.higher)

    def addNum(self, num: int) -> None:
        if len(self.lower) == len(self.higher):
            if len(self.lower) > 0 and num > - self.lower[0]:
                heapq.heappush(self.higher, num)
            else:
                tmp = heapq.heappushpop(self.lower, -num)
                heapq.heappush(self.higher, -tmp)
        else:
            if num > self.higher[0]:
                tmp = heapq.heappushpop(self.higher, num)
                heapq.heappush(self.lower, -tmp)
            else:
                heapq.heappush(self.lower, -num)

    def findMedian(self) -> float:
        if len(self.lower) == 0 and len(self.higher) == 0:
            return None

        if len(self.lower) == len(self.higher):
            return (- self.lower[0] + self.higher[0]) / 2
        else:
            return self.higher[0]


cases = [
    (
        ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
         "addNum", "findMedian"],
        [[], [-1], [], [-2], [], [-3], [], [-4], [], [-5], []]
    )
]


def judge(ops, args):
    ret = []
    obj = None
    for i in range(len(ops)):
        if ops[i] == "MedianFinder":
            obj = MedianFinder()
            ret.append(None)
        elif ops[i] == "addNum":
            obj.addNum(*args[i])
            ret.append(None)
        elif ops[i] == "findMedian":
            ret.append(
                obj.findMedian()
            )
    return ret


for case in cases:
    ans = judge(*case)
    print(ans)
