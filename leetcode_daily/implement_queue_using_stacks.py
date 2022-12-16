#EASY
# 232


'''     https://leetcode.com/problems/implement-queue-using-stacks/     '''


# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
# Implement the MyQueue class:
# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:
# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.


# Example 1:
# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]
# ---------------------------------------------------------------
# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false


class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        if len(self.stack1) == 0:
            self.stack1.append(x)
        else:
            for i in self.stack1[::-1]:
                self.stack2.append(i)

            self.stack1.clear()
            self.stack1.append(x)

            for i in self.stack2[::-1]:
                self.stack1.append(i)
            self.stack2.clear()

    def pop(self) -> int:
        e = self.stack1[-1]
        self.stack1.pop()
        return e

    def peek(self) -> int:
        return self.stack1[-1]

    def empty(self) -> bool:
        if len(self.stack1) == 0:
            return True
        else:
            return False

obj = MyQueue()
obj.push(x)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()