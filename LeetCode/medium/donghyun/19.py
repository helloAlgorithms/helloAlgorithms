# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode
        dummy.next = head
        node = dummy
        q = deque()
        while node:
            q.append(node)
            if len(q) > n + 1:
                q.popleft()
            node = node.next
        q[0].next = q[-n].next
        return dummy.next