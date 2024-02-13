# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        leftHead = left = ListNode()
        rightHead = right = ListNode()
        cur = head
        while cur:
            if cur.val >= x:
                right.next = cur
                right = right.next
            else:
                left.next = cur
                left = left.next
            cur = cur.next
            left.next = rightHead.next
            right.next = None
        
        return leftHead.next
                    


            
        

        