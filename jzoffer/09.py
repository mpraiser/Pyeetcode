class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        result = -1 if not self.stack2 else self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return result

obj = CQueue()
obj.appendTail(3)
print(obj.deleteHead())
print(obj.deleteHead())