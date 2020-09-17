"""
Union-Find算法解决的是图的动态连通性问题。
"""
class UF:
    count = 0
    parent = []
    size = []

    def __init__(self, nums):
