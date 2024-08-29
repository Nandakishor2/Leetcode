# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        def addlist(l1,l2,carry):
            if not l1 and not l2 and carry is 0:
                return None
            sum = (l1.val if l1 else 0)+(l2.val if l2 else 0)+carry
            carry = sum//10
            lisval = sum%10
            newnode = ListNode(lisval)
            newnode.next = addlist(l1.next if l1 else None,l2.next if l2 else None,carry)
            return newnode
        return addlist(l1,l2,0)
        
    
        

        

        