# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        string=[]
        count = 1
        while fast and fast.next:
            string.append(head.val)
            head = head.next
            fast = fast.next
            count += 1
            if not fast:
                break
            fast = fast.next
            if not fast:
                break
            count += 1
        if count % 2 == 1:
            head = head.next
                    
        while head:
            if head.val != string.pop():
                return False
            head = head.next
            
            
        return True