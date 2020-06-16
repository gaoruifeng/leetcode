# 25. Reverse Nodes in k-Group

# Definition for singly-linked list.
from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # if list is empty or k is 1
        if head is None or k==1: return head

        prev = dummy = ListNode(val=0, next=head)

        # initialize queue to hold k nodes
        count, k_nodes = 0, deque()
        while head is not None:
            k_nodes.append(head)
            head, count = head.next, count+1
            if count == k:
                # first node of the queue will be the last in its batch
                # set its next node to be the 1st node of next batch
                k_nodes[0].next = head

                # pop from queue and append to list
                while count != 0:
                    prev.next, count = k_nodes.pop(), count-1
                    prev = prev.next
            
        return dummy.next

if __name__ == '__main__':
    b = ListNode(1)
    b.next = ListNode(2)
    b.next.next = ListNode(3)
    b.next.next.next = ListNode(4)
    b.next.next.next.next = ListNode(5)

    s = Solution()
    ll = s.reverseKGroup(b, 3)
    while ll:
        print(ll.val)
        ll = ll.next
