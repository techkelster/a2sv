# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next
        cur = head
        for i in range(size - 1, -1, -1):
            ans += cur.val * 2 ** i
            cur = cur.next

        return ans
            