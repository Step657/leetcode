"""
用栈实现队列
     从栈s1搬运元素到s2之后，元素在s2中就变成了队列的先进先出顺序，这个特性有点类似负负得正。
"""


class Stack:
    s = []

    def push(self, x: int):
        self.s.append(x)

    def pop(self):
        return self.s.pop()

    def isEmpty(self):
        return len(self.s) == 0

    def peek(self):
        return self.s[-1]


class MyQueue:
    s1, s2 = None, None

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x: int):
        """添加元素到队尾"""
        self.s1.push(x)

    def pop(self) -> int:
        """删除队头元素并返回"""
        # 先调用peek保证s2非空
        self.s2.peek()
        return self.s2.pop()

    def peek(self) -> int:
        """返回队头元素"""
        if self.s2.isEmpty():
            while not self.s1.isEmpty():
                self.s2.push(self.s1.pop())
        return self.s2.peek()

    def empty(self) -> bool:
        """判断队列是否为空"""
        return self.s1.isEmpty() and self.s2.isEmpty()
