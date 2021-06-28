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
        head = ListNode(0, None)
        node = head
        last_node = None

        for n in values:
            node.val = n
            if last_node:
                last_node.next = node

            last_node = node
            node = ListNode(0, None)
        return head

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
