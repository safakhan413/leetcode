"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

"""




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        # Use a current pointer to build the new list
        cur = dummy
        # print('im dummy')
        # While both lists are non-empty, compare and attach the smaller node
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next  # Move the current pointer
        
        # Attach the remaining nodes from either list
        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2
        
        # Return the merged list starting at dummy.next
        return dummy.next



        # print(list1.val)
        # print(list1.next)

        # print(list1.val, list2.val)
        # for i in list1:
        #     print(i.data)
