# Queues: A Tale of Two Stacks
# Cracking the Coding Interview Challenge
# https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks

class MyQueue(object):
    def __init__(self):
        self.head = Node(None,None,None)
        self.tail = Node(None,None,None)
        self.head.next = self.tail
        self.tail.previous = self.head
    
    def peek(self):
        return self.head.next.value
        
    def pop(self):
        self.head.next = self.head.next.next
        self.head.next.previous = self.head
        
    def put(self, value):
        newNode = Node(value, self.tail, self.tail.previous)
        newNode.previous.next = newNode
        self.tail.previous = newNode
            
class Node(object):
    def __init__(self, value, nextNode, previousNode):
        self.value = value
        self.next = nextNode
        self.previous = previousNode
        

#----------------------- Provided -----------------------
queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
        
