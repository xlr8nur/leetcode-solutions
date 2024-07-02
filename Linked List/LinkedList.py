''' 
Question;
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
'''

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
