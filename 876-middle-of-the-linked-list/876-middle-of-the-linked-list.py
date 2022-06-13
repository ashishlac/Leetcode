# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 0
        temp=head
        while temp is not None:
            count += 1
            temp = temp.next
        count =  (count / 2) + 1
        while count is not 1:
            count -= 1
            head = head.next
            
        return head