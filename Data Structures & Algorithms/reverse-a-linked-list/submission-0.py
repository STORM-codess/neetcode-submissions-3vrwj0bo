# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st = []
        if not head:
            return

        curr = head

        while curr:
            st.append(curr.val)
            curr = curr.next

        start = ListNode(st.pop())
        curr = start
        
        while st:
            curr.next = ListNode(st.pop())
            curr = curr.next
        
        return start
            
            


        

            



        