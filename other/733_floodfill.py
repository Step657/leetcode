"""
733. 图像渲染
    有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。
    给你一个坐标 (sr, sc) 表示图像渲染开始的像素值（行 ，列）和一个新的颜色值 newColor，让你重新上色这幅图像。
    为了完成上色工作，从初始坐标开始，记录初始坐标的上下左右四个方向上像素值与初始坐标相同的相连像素点，
    接着再记录这四个方向上符合条件的像素点与他们对应四个方向上像素值与初始坐标相同的相连像素点，……，重复该过程。
    将所有有记录的像素点的颜色值改为新的颜色值。
    最后返回经过上色渲染后的图像。
示例 1:
    输入:
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1, sc = 1, newColor = 2
    输出: [[2,2,2],[2,2,0],[2,0,1]]
    解析:
    在图像的正中间，(坐标(sr,sc)=(1,1)),
    在路径上所有符合条件的像素点的颜色都被更改成2。
    注意，右下角的像素没有更改为2，
    因为它不是在上下左右四个方向上与初始点相连的像素点。
构建框架：
    颜色填充、消消乐，都可以抽象成一个二维数组（图片其实就是像素点矩阵），然后从某个点开始向四周扩展，直到无法扩展为止。
    矩阵可以抽象为一幅图，这就是一个图的遍历问题，也就是类似一个N叉树遍历的问题。
"""
from typing import List


def fill(x: int, y: int):
    """
    可以解决所有在二维矩阵中遍历的问题，说得高端一点，这就叫深度优先搜索(Depth First Search, DFS), 四叉树遍历框架
    :param x:
    :param y:
    :return:
    """
    fill(x - 1, y)  # 上
    fill(x + 1, y)  # 下
    fill(x, y - 1)  # 左
    fill(x, y + 1)  # 右


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        origColor = image[sr][sc]
        self.fill(image, sr, sc, origColor, newColor)
        return image

    def fill_0(self, image: List[List[int]], x: int, y: int, origColor: int, newColor: int):
        # 出界：超过边界索引
        if not self.inArea(image, x, y):
            return
        if image[x][y] != origColor:
            return
        image[x][y] = newColor
        self.fill(image, x, y + 1, origColor, newColor)
        self.fill(image, x, y - 1, origColor, newColor)
        self.fill(image, x + 1, y, origColor, newColor)
        self.fill(image, x - 1, y, origColor, newColor)

    def fill(self, image: List[List[int]], x: int, y: int, origColor: int, newColor: int):
        """
        细节：当origColor 和 newColor 相同时，会陷入无限递归
        处理：最容易想到的就是用一个和image一样大小的二维bool数组记录走过的地方，一旦发现重复立即return
            更好的算法利用回溯算法。
        :param image:
        :param x:
        :param y:
        :param origColor:
        :param newColor:
        :return:
        """
        # 出界：超过边界索引
        if not self.inArea(image, x, y):
            return
        # 碰壁：遇到其他颜色，超出origColor区域
        if image[x][y] != origColor:
            return
        if image[x][y] == -1:
            return

        # choose：打标记，以免重复
        image[x][y] = -1
        self.fill(image, x, y + 1, origColor, newColor)
        self.fill(image, x, y - 1, origColor, newColor)
        self.fill(image, x + 1, y, origColor, newColor)
        self.fill(image, x - 1, y, origColor, newColor)
        # unchoose:将标记替换为newColor
        image[x][y] = newColor

    def inArea(self, image: List[List[int]], x: int, y: int) -> bool:
        return 0 <= x <  len(image) and 0 <= y < len(image[0])
