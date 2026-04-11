# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        # create a arr
        arr = []
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next
        # now create two pointers
        i, j = 0 , len(arr) -1
        while i<j:
            arr[i].next =arr[j]
            i +=1
            if i == j:
                break
            arr[j].next = arr[i]
            j -=1
        # terminate the node
        arr[i].next = None