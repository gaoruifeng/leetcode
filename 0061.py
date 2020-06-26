class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None: return None

        # get list length
        curr, leng = head, 0
        while curr is not None:
            curr, leng = curr.next, leng+1

        # advance tail k times to the right
        k = k % leng
        tail = head
        while k != 0:
            tail, k = tail.next, k-1

        # distance of curr and tail is k
        # advance them until tail reaches end of the list
        curr = head
        while tail.next is not None:
            curr, tail = curr.next, tail.next

        # set head as the next node of tail
        tail.next = head
        # curr.next is the new head
        res = curr.next
        # curr is the new tail, set it's next to None
        curr.next = None
        return res
        
        
if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    #l1.next.next.next = ListNode(4)
    #l1.next.next.next.next = ListNode(5)

    ll = s.rotateRight(l1, 4)
    while ll:
        print(ll.val)
        ll = ll.next
