"""
剑指 Offer 24. 反转链表
    定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
示例:
    输入: 1->2->3->4->5->NULL
    输出: 5->4->3->2->1->NULL
限制：
    0 <= 节点个数 <= 5000
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """反转单链表的迭代实现不是一个困难的事情，但是递归实现就有点难度了，如果仅仅反转单链表中的一部分，又该怎么做.【&迭代解法，虽然时间复杂度都是O(N),
    但是迭代解法的空间复杂度是O(1),而递归解法需要堆栈，空间复杂度为O(N)】"""
    successor = None

    def reverseList(self, head: ListNode) -> ListNode:
        """递归反转整个链表"""
        # base case:如果链表只有一个节点的时候反转也是它自己，直接返回即可
        if not head or not head.next:
            return head
        # last：相当于反转链表的头结点
        last = self.reverseList(head.next)
        # head变成了最后一个节点，别忘了链表的末尾要指向null
        head.next.next = head
        head.next = None
        return last

    def reverseN(self, head: ListNode, n: int) -> ListNode:
        """反转链表前n个节点"""
        if n == 1:
            # 记录第n + 1个节点
            self.successor = head.next
            return head
        # 以head.next为起点，需要反转前n-1个节点
        last = self.reverseN(head.next, n - 1)
        # 让反转之后的head节点和后面的节点连起来
        head.next.next = head
        head.next = self.successor
        return last

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # base case
        if m == 1:
            return self.reverseN(head, n)
        head.next = self.reverseBetween(head.next, m-1, n-1)
        return head
