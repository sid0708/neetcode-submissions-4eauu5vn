class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverseList(node):
            prev, curr = None, node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        # Reverse the list
        head = reverseList(head)

        # Delete nth from start (because reversed)
        dummy = ListNode(0, head)
        curr = dummy
        for _ in range(n - 1):
            curr = curr.next

        curr.next = curr.next.next

        # Reverse back
        head = reverseList(dummy.next)

        return head
