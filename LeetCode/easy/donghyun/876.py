# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        linked_list = head
        while linked_list:
            length += 1
            linked_list = linked_list.next
        for _ in range(length//2):
            head = head.next
        return head