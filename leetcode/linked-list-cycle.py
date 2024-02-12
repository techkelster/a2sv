# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visted = {}
        cur = head
        while cur:
            if cur in visted:
                return True
            else:
                visted[cur] = "seen"
            cur = cur.next
        return False
        