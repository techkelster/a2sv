# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next is None or left == right:
            return head
        
        dummy = ListNode()
        dummy.next = head

        pred = dummy
    

        for i in range(left - 1):
            pred = pred.next

        p = pred
        revStart = pred.next
        cur = revStart

        for i in range(right - left + 1):
            temp = cur.next
            cur.next = pred
            pred = cur
            cur = temp

        p.next = pred
        revStart.next = cur
        
        return dummy.next
        
      

        


