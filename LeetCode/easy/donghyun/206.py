# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed = ListNode()
        next_node = reversed
        q = deque()
        while head:
            q.appendleft(head.val)
            head = head.next
        for num in q:
            next_node.next = ListNode()
            next_node = next_node.next
            next_node.val = num
        return reversed.next