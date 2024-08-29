# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        def sortarray(l1,l2):
            if not l1 and not l2 :
                return None
            newnode = ListNode()
            if (l1.val if l1 else 101) <= (l2.val if l2 else 101):
                newnode.val =l1.val
                newnode.next = sortarray(l1.next if l1 else None,l2 if l2 else None)
            else:
                newnode.val = l2.val
                newnode.next = sortarray(l1 if l1 else None,l2.next if l2 else None)
            return newnode
        return sortarray(list1, list2)

                
        