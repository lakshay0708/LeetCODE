# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        temp = head
        prev = head
        l = []
        while temp != None:
            if temp.val not in l:
                l.append(temp.val)
                prev = temp
                temp = temp.next
            else:
                temp = temp.next
                prev.next = temp
        return head        

