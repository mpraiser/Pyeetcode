class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__stack = []
        self.__min_stack = []

    def push(self, x: int) -> None:
        self.__stack.append(x)
        if (not self.__min_stack) or (x <= self.__min_stack[-1]):
            self.__min_stack.append(x)

    def pop(self) -> None:
        x = self.__stack.pop()
        if x == self.__min_stack[-1]:
            self.__min_stack.pop()
        return x

    def top(self) -> int:
        return self.__stack[-1]

    def min(self) -> int:
        return self.__min_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()