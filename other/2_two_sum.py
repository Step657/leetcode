"""
2. 两数相加
    给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
    如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
    您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
示例：
    输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 0 -> 8
    原因：342 + 465 = 807
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def llen(l):
    length = 0
    while l:
        l = l.next
        length += 1
    return length


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """结果存储在l1中，提前将l1换成最长的"""
        if llen(l1) < llen(l2):
            l1, l2 = l2, l1
        head1 = l1
        length = max(llen(l1), llen(l2))
        carry = 0

        for i in range(length):
            # l2（较短）的还没结束
            if l2:
                val1, val2 = l1.val, l2.val
                l1.val = (val1 + val2 + carry) % 10
                carry = (val1 + val2 + carry) // 10
                l2 = l2.next
            else:
                val1 = l1.val
                l1.val = (val1 + carry) % 10
                carry = (val1 + carry) // 10
            # 如果l1为最后一个节点，并且还有进位，则新建一个节点
            if not l1.next and carry == 1:
                l1.next = ListNode(carry)
                l1 = l1.next
            l1 = l1.next
        return head1


if __name__ == '__main__':
    list1 = [5]
    list2 = [5]
    head1, head2 = ListNode(0), ListNode(0)
    l1, l2 = head1, head2
    for i in list1:
        l1.next = ListNode(i)
        l1 = l1.next
    for i in list2:
        l2.next = ListNode(i)
        l2 = l2.next

    solution = Solution()
    solution.addTwoNumbers(head1.next, head2.next)
