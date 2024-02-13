class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_chain = ListNode()
        tmp = new_chain

        while list1 and list2:
            if list1.val == list2.val:
                new_chain.next = list1
                list1 = list1.next
            elif list1.val > list2.val:
                new_chain.next = list2
                list2 = list2.next
            else:
                new_chain.next = list1
                list1 = list1.next
            new_chain = new_chain.next

        if list1:
            new_chain.next = list1
        if list2:
            new_chain.next = list2

        return tmp.next
