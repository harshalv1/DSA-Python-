# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dum=ListNode()
        tail=dum

        while list1 and list2:
            if list1.val<list2.val:
                tail.next=list1
                list1=list1.next
            else:
                tail.next=list2
                list2=list2.next
            tail=tail.next
        
        if list1 is None:
            tail.next=list2
        elif list2 is None:
            tail.next=list1
        
        return dum.next

#t.c is o(n) we only iterate through both the lists once 
#s.c is o(1) dummy node doesn't take any space with respect to the size of the input 
#lists