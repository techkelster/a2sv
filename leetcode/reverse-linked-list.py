class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            tmpNext = cur.next  
            cur.next = prev     
            prev = cur           
            cur = tmpNext       

        return prev  
