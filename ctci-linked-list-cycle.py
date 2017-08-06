"""
// Linked List: Detecting Cycles
// Cracking the Coding Interview Challenge
// https://www.hackerrank.com/challenges/ctci-linked-list-cycle
 
Process is tortoise and hare solution. One pointer moves twice as fast as the other pointer. Return false for cycle if fast pointer reaches the end. Return true for cycle if slow pointer == fast pointer. Detects in O(n) time. 
Also can find point where cycle begins by moving slow back to start and then stepping through until slow = fast. Check out https://cs.stackexchange.com/questions/10360/floyds-cycle-detection-algorithm-determining-the-starting-point-of-cycle for explanation
"""

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if head.next is None:
        return False
    fast, slow = head.next, head.next
    while fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast.data == slow.data:
            return True
    return False
    
