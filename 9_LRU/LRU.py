"""
LRU: Least Recently used
    首先要接受一个capacity参数作为缓存的最大容量，然后实现两个API， 一个是put(key,val)方法存入键值对，
    另一个是get(key)方法获取key对应的val， 如果key不存在，则返回-1。
    get 和 put 方法必须都是O(1)的时间复杂度。
        其数据结构必要的条件: 查找快、插入快、删除快、有顺序之分
        哈希表：查找快、但是数据没有固定的顺序；
        链表：有顺序之分、删除插入快，但是查找慢；
        所以结合一下，形成一种新的数据结构：哈希链表（双向链表 + 哈希表）
"""


class Node:
    """以 int 类型为例"""
    key, val = 0, 0
    # 指针域n:next, p:pre
    n, p = None, None

    def __init__(self, k = 0, v = 0):
        self.key = k
        self.val = v


class DoubleList:
    __length = 0
    __head = Node()
    __tail = Node()
    def addFirst(self, x: Node):
        """
        在链表头部添加结点x， 时间复杂度为O(1)
        :param x:
        :return: None
        """
        x.n = self.__head.n
        x.p = self.__head
        self.__head.n = x
        self.__head.p = None
        self.__length += 1

    def remove(self, x: Node):
        """
        删除链表中的x节点（x一定存在）
        由于是双链表且给的目标Node节点，时间复杂度为O(1)
        :param x:
        :return: None
        """
        x.n.p = x.p
        x.p.n = x.n
        self.__length -= 1

    def removeLast(self) -> Node:
        """
        删除链表中最后一个节点，并返回该节点， 时间复杂度O(1)
        :return: Node
        """
        x = self.__tail.p
        x.p.n = self.__tail
        self.__tail.p = x.p
        self.__length -= 1
        return x


    def size(self) -> int:
        """
        返回链表长度， 时间复杂度为O(1)
        :return:
        """
        return self.__length

class LRUCache:
    __hash_map = {}
    __cache = DoubleList()
    cap = 0

    def __init__(self, capacity: int):
        """
        init a LRUCache
        :param capacity:
        """
        self.cap = capacity

    def get(self, key: int) -> int:
        """
        获得key对应的value
        :param key:
        :return: value of the key-value,
        """
        if key not in self.__hash_map:
            return -1
        val = self.__hash_map[key].val
        self.put(key, val)
        return val

    def put(self, k: int, v: int):
        """
        增加一个节点Node
        :param k: key
        :param v: value
        :return: Node
        """
        x = Node(k, v)
        if k in self.__hash_map:
            # 删除旧的节点，新的插入到头部
            self.__cache.remove(x)
            self.__cache.addFirst(x)
            # 更新 __hash_map中对应的数据
            self.__hash_map[k] = x
        else:
            if self.cap == self.__cache.size():
                # 删除__cache链表最后一个数据
                last = self.__cache.removeLast()
                self.__hash_map.pop(last.k)
            # 直接添加到头部
            self.__cache.addFirst(x)
            self.__hash_map[k] = x
