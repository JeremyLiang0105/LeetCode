class ListNode:
    def __init__(self, val, nxt, prev):
        self.val, self.next, self.prev = val, nxt, prev
    
class MyLinkedList:
    def __init__(self):
        self.left = ListNode(0, None, None)
        self.right = ListNode(0, None,self.left)
        self.left.next = self.right
        self.cnt = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.cnt:
            return -1
        cur = self.left
        while index != 0:
            cur = cur.next
            index -= 1
        return cur.next.val

    def addAtHead(self, val: int) -> None:
        cur = ListNode(val, self.left.next, self.left)
        self.left.next.prev = cur
        self.left.next = cur
        self.cnt += 1

    def addAtTail(self, val: int) -> None:
        cur = ListNode(val, self.right, self.right.prev)
        self.right.prev.next = cur
        self.right.prev = cur
        self.cnt += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if 0 <= index < self.cnt:
            cur = self.left
            while index != 0:
                cur = cur.next
                index -= 1
            new = ListNode(val, cur.next, cur)
            cur.next.prev = new
            cur.next = new
            self.cnt += 1
        elif index == self.cnt:
            self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.cnt:
            cur = self.left
            while index != 0:
                cur = cur.next
                index -= 1
            cur = cur.next
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            self.cnt -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
