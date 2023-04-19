# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode()
        dummy.next = head

        ## two counters dummy is an extra one created and placed at the start. This helps with identifying the elemnts before the nth one to set the pointer correctly

        pnt1, pnt2 = dummy, head
        for _ in range(n):
            pnt2 = pnt2.next

        while pnt2:
            pnt1, pnt2 = pnt1.next, pnt2.next
        
        pnt1.next = pnt1.next.next
        return dummy.next