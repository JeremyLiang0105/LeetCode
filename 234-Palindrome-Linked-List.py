# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        new = []
        while head:
            new.append(head.val)
            head = head.next
        if new == new[::-1]:
            return True
        else:
            return False
          
    # time complexity: O(n)
    # space complexity: O(n)
