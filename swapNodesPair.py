
'''
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.
 
Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
'''


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        previous = ListNode(0)
        previous.next = head
        currentNode = previous
        while currentNode.next and currentNode.next.next:
            first = currentNode.next
            second = first.next
            currentNode.next, first.next, second.next = second, second.next, first
            currentNode = first
        return previous.next
