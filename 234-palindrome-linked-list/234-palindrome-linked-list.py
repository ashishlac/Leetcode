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
        # rev records the first half, need to set the same structure as fast, slow, hence later we have rev.next
        rev = None
        # initially slow and fast are the same, starting from head
        slow = fast = head
        while fast and fast.next:
            # fast traverses faster and moves to the end of the list if the length is odd
            fast = fast.next.next

            # take it as a tuple being assigned (rev, rev.next, slow) = (slow, rev, slow.next), hence the re-assignment of slow would not affect rev (rev = slow)
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
           # fast is at the end, move slow one step further for comparison(cross middle one)
            slow = slow.next
        # compare the reversed first half with the second half
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next

        # if equivalent then rev become None, return True; otherwise return False 
        return not rev
