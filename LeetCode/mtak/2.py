# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret = itr = ListNode(0)
        left = 0
        while l1 or l2 or left:
            left, val = divmod((l1.val if l1 else 0) + (l2.val if l2 else 0) + left , 10)
            print(left, val)
            itr.next = ListNode(val)
            itr = itr.next
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
        return ret.next
