# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        alreadyPath = set()
        curr = head
        while (curr):
            if (curr in alreadyPath):
                return True
            alreadyPath.add(curr)
            curr = curr.next
        return False
        