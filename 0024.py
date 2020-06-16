# 24. Swap Nodes in Pairs

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # if list is empty
        if head is None: return head

        dummy = ListNode(val=0, next=head)
        prev, n1, n2=dummy, head, head.next
        while n1 is not None and n2 is not None:
            # swap nodes
            prev.next, n2.next, n1.next = n2, n1, n2.next
            # advance prev and n1
            prev, n1 = n1, n1.next
            if n1 is not None: n2 = n1.next
        return dummy.next

if __name__ == '__main__':
    b = ListNode(1)
    b.next = ListNode(2)
    b.next.next = ListNode(3)
    #b.next.next.next = ListNode(4)

    s = Solution()
    ll = s.swapPairs(b)
    while ll:
        print(ll.val)
        ll = ll.next
