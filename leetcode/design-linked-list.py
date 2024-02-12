class MyLinkedList:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if index < 0 or not self.head:
            return -1

        tmp = self.head
        i = 0

        while tmp:
            if index == i:
                return tmp.val
            i += 1
            tmp = tmp.next

        return -1

    def addAtHead(self, val: int) -> None:
        new_head = self.Node(val)
        new_head.next = self.head
        self.head = new_head
        print()

    def addAtTail(self, val: int) -> None:
        new_node = self.Node(val)
        if not self.head:
            self.head = new_node
            return

        tmp = self.head
        while tmp.next:
            tmp = tmp.next

        tmp.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            self.addAtHead(val)
            return

        new_node = self.Node(val)
        tmp = self.head
        i = 0

        while tmp and i < index - 1:
            tmp = tmp.next
            i += 1

        if not tmp:
            return

        new_node.next = tmp.next
        tmp.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or not self.head:
            return

        if index == 0:
            self.head = self.head.next
            return

        tmp = self.head
        i = 0

        while tmp and i < index - 1:
            tmp = tmp.next
            i += 1

        if not tmp or not tmp.next:
            return

        tmp.next = tmp.next.next