# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # At the end of the loop, prev will point to the new head of the reversed list
        reversed_head = prev

        # Print the reversed linked list
        while reversed_head:
            print(reversed_head.val)
            reversed_head = reversed_head.next

        return prev  # Return the new head of the reversed list


