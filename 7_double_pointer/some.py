class ListNode(object):
    """Definition for singly-linked list"""
    def __init__(self, x):
        self.val = x
        self.next = None


class FastSlow(object):
    def __init__(self, head):
        """
        initialize fast and slow pointer equal head
        :param head: 头结点
        """
        self.fast = head
        self.slow = head
        self.head = head

    def hasCucel(self):
        fast, slow = self.fast, self.slow

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True
        return False
    
    def detectCycle(self):
        fast, slow = self.fast, self.slow

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                break

        slow = self.head
        while slow is not fast:
            fast = fast.next
            slow = slow.next
        return slow

    def getMiddle(self):
        fast, slow = self.fast, self.slow
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def getNode(self, k):
        """
        get the reverse k_th Node's pointer
        :param k: input
        :return:
        """
        fast, slow = self.fast, self.slow
        for i in range(k):
            fast = fast.next
        while fast is not None:
            fast = fast.next
            slow = slow.next
        return slow


class LeftRight(object):
    def __init__(self, array, target):
        """
        initialize some variable
        :param array:
        """
        self.array = array
        self.length = len(array)
        self.target = target

    def binarySearch(self):
        left, right = 0, self.length - 1
        array, target = self.array, self.target
        while left <= right:
            mid = left + (right-left) / 2
            if  array[mid] == target:
                return mid
            elif array[mid] < target:
                left = mid + 1
            elif array[mid] > target:
                right = mid - 1
        return -1
