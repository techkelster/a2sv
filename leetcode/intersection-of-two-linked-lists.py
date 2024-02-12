# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        refer_dic = {}
        while headA:
            refer_dic[headA] = "visted"
            headA = headA.next
        while headB:
            if headB in refer_dic:
                return headB
            headB = headB.next
        return None