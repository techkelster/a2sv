# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        list_length, current_node = 0, root

        while current_node:
            list_length += 1
            current_node = current_node.next
    
        current_node = root

        part_size, extra_nodes = divmod(list_length, k)

        result = [None for _ in range(k)]

        for i in range(k):
            part_head = current_node
            current_part_size = part_size + (i < extra_nodes)

            for j in range(current_part_size - 1):
                if current_node:
                    current_node = current_node.next
          
            
            if current_node:
                next_part = current_node.next
                current_node.next = None
                current_node = next_part
    
            result[i] = part_head
        return result
      
            
