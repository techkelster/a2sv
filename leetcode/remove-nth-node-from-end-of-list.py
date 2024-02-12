# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        fast = dummy 
        slow = dummy
        while fast:
            if n == -1:
                slow = slow.next
                fast = fast.next
            else:
                n -= 1
                fast = fast.next
        if slow and slow.next:
            slow.next = slow.next.next
        else:
            slow.next = None 
        return dummy.next


        