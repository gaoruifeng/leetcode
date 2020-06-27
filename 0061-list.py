# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None: return None

        # add nodes to list
        nodes = []
        while head is not None:
            nodes.append(head)
            head = head.next

        k = k % len(nodes)
        nodes[-1].next = nodes[0]
        nodes[-1*k-1].next = None
        return nodes[-1*k]
        
        
if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)

    ll = s.rotateRight(l1, 2)
    while ll:
        print(ll.val)
        ll = ll.next
