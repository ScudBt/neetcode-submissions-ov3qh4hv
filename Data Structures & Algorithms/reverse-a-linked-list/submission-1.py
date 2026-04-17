# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp1 = None
        tmp2 = head
        while tmp2:
            tmp3 = tmp2.next
            tmp2.next = tmp1
            tmp1, tmp2 = tmp2, tmp3
        return tmp1