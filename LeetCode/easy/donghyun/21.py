# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        next_node = merged
        while list1 and list2:
            next_node.next = ListNode()
            next_node = next_node.next
            if list1.val < list2.val:
                next_node.val = list1.val
                list1 = list1.next
            else:
                next_node.val = list2.val
                list2 = list2.next
        if list1:
            next_node.next = list1
        if list2:
            next_node.next = list2
        return merged.next