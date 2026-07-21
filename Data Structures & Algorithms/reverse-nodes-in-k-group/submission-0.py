class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        dummy = ListNode(0)
        dummy.next = head

        groupPrev = dummy

        while True:

            # Find kth node
            kth = groupPrev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            groupNext = kth.next

            # Reverse current group
            prev = groupNext
            curr = groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Connect reversed group
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp