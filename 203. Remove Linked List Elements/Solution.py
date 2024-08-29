# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        def answer(l1):
            if not l1 :
                return None
            l1.next = answer(l1.next)
            if l1.val == val:
                return l1.next
            return l1
        return answer(head)
       
        
        