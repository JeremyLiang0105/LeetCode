# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head
        
        while cur and cur.next:
            # we want to make sure we have at least two nodes to reverse
            nxtPair = cur.next.next
            nxt = cur.next
            nxt.next = cur
            cur.next = nxtPair
            prev.next = nxt
            
            prev = cur
            cur = nxtPair
        
        return dummy.next
