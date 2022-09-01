# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Runtime: 28 ms, faster than 99.53% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.4 MB, less than 55.75% of Python3 online submissions for Reverse Linked List.
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head != None:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev
