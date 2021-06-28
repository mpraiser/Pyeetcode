from typing import List


class ListNode:
    """
    Definition for singly-linked list.
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def parse(values: List):
        if len(values) == 0:
            return None
        sentinel = ListNode(0, None)
        node = sentinel

        for n in values:
            node.next = ListNode(n, None)
            node = node.next

        return sentinel.next

    def serialize(self) -> List:
        result = []
        node = self
        while node:
            result.append(node.val)
            node = node.next
        return result


if __name__ == "__main__":
    x = ListNode.parse([1, 2, 3])
    print(x.serialize())
