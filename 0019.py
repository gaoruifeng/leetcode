# 19. Remove Nth Node From End of List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr = head
        temp = head
        while n != 0:
            curr = curr.next
            n -= 1
        if curr is None:
            return head.next

        while curr.next is not None:
           curr = curr.next
           temp = temp.next
        temp.next = temp.next.next

        return head

if __name__ == '__main__':
    b = ListNode(1)
    b.next = ListNode(2)
    b.next.next = ListNode(3)
    b.next.next.next = ListNode(4)
    b.next.next.next.next = ListNode(5)
    s = Solution()
    ll = s.removeNthFromEnd(b, 5)
    while ll:
        print(ll.val)
        ll = ll.next
