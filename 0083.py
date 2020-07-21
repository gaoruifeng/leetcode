# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        curr = head
        while curr is not None and curr.next is not None:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)

    ll = s.deleteDuplicates(l1)
    while ll:
        print(ll.val)
        ll = ll.next
