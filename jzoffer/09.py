class CQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def appendTail(self, value: int) -> None:
        self.stack_in.append(value)

    def deleteHead(self) -> int:
        if len(self.stack_out) > 0:
            return self.stack_out.pop()
        else:
            while len(self.stack_in) > 0:
                self.stack_out.append(self.stack_in.pop())
            if len(self.stack_out) > 0:
                return self.stack_out.pop()
            else:
                return -1

obj = CQueue()
obj.appendTail(3)
print(obj.deleteHead())
print(obj.deleteHead())