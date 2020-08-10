class Node(object):
    def __init__(self, val):
        self.val = val


class BinaryHeap(object):
    """
        二叉堆
    """

    def __init__(self, root):
        self.root = root

    def parent(self):
        """父节点"""
        return self.root // 2

    def left(self):
        """左节点"""
        return self.root * 2

    def right(self):
        """右节点"""
        return self.root * 2 + 1


class MaxPQ(object):
    """
    优先队列（以大顶堆为例）
    """

    def __init__(self, N, cap):
        """
        初始化
        :param N: 当前priority queue 中的元素个数
        :param cap: pq 的容量
        """
        self.pq = [Node() for i in range(cap + 1)]  # index 0 is't use
        self.N = N

    def max(self):
        """返回当前队列中的最大元素"""
        return self.pq[1]

    def insert(self, e):
        """插入元素 e """
        self.N += 1
        self.pq[self.N] = e     # 先把元素加到最后
        self.__swim(self.N)     # 然后让它上浮到正确的位置

    def delMax(self):
        """删除并返回当前队列中的最大元素"""
        max = self.pq[1]    # 最大堆的堆顶就是最大元素
        self.__exchange(1, self.N)
        self.pq[self.N] = None
        self.N -= 1
        self.__sink(1)
        return max


    def __swim(self, k):
        """上浮第 k 个元素，以维护最大堆的性质"""
        # 如果浮到堆顶，就不能再上浮了
        while k > 1 and self.__less(self.__parent(k), k):
            self.__exchange(self.__parent(k), k)
            k = self.__parent(k)

    def __sink(self, k):
        """下沉第 k 个元素，以维护最大堆的性质"""
        # 如果下沉到堆底，就沉不下去了
        while self.__left(k) <= self.N:
            # 先假设左边节点较大
            older = self.__left(k)
            # 如果右边节点存在，比一下大小
            if self.__right(k) <= self.N and self.__less(older, self.__right(k)):
                older = self.__right(k)
            if self.__less(older, k):
                break
            self.__exchange(k, older)
            k = older

    def __exchange(self, i, j):
        """交换数组的两个元素"""
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]

    def __less(self, i, j):
        """pq[i] 是否比 pq[j] 小"""
        return self.pq[i] < self.pq[j]

    def __parent(self, k):
        """父节点"""
        return k // 2

    def __left(self, k):
        """左节点"""
        return k * 2

    def __right(self, k):
        """右节点"""
        return k * 2 + 1
