class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur:
            tmp = cur.next
            while tmp and cur.val == tmp.val:
                tmp = tmp.next
            if tmp:
                cur.next = tmp
            else:
                cur.next = None 
            cur = cur.next

        return head
