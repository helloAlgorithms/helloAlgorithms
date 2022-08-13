# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while (curr and curr.next):
            while (curr.val == curr.next.val):
                curr.next = curr.next.next
                if (not curr or not curr.next):
                    break
            curr = curr.next
        return (head)
