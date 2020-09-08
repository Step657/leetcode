"""
    菜鸟编程大本营 公众号
    Python 30 道高频面试题及详细解答
"""

# 1.用一行代码生成奇数列
nums = [i * 2 + 1 for i in range(10)]
nums = [i for i in range(20) if i % 2 == 1]


# 2. 写一个等差数列
def array(a0, d, n):
    return [i for i in range(a0, a0 + n * d, d)]


# 3.一行代码求1到1000内的整数和
res = sum(range(1, 1001))
from functools import reduce

s = reduce(lambda x, y: x + y, range(1, 1001))

# 4.字典按照value排序并返回新字典
d = {'a': 100, 'b': 98, 'c': 101}
sorted_d = dict(sorted(d.items(), key=lambda item: item[1]))

# 5. 打乱一个列表
import random

nums = list(range(10))
nums = random.shuffle(nums)

# 6. 如何删除list里面重复的元素并保证顺序不变
nums = [5, 3, 3, 3, 6, 7]


def del_duplicated_nums(nums):
    res = []
    for i in nums:
        if i not in res:
            res.append(i)
    return res


# 7. 字符串处理成字典
s = 'a0:10|a1:20|a2:30|a3:40'
items = map(lambda x: x.split(':'), s.split('|'))
res = {item[0]: item[1] for item in items}

# 8. 怎么找出两个列表的相同元素和不同元素
a = [1, 2, 2, 3, 6]
b = [5, 3, 3, 3, 6, 7]


def find_nums(a, b):
    aset, bset = set(a), set(b)
    same = aset.intersection(bset)
    diff = aset.difference(bset).union(bset.difference(aset))
    print('same:', same)
    print('diff:', diff)


# 9.输入一个日期，判断这一天是今年的哪一天
from datetime import datetime


def find_day_of_year(y, m, d):
    return datetime(y, m, d).date().timetuple().tm_yday


# 10. 遍历目录内子目录，抓取zip文件
import os


def find_files(dir, ext='zip'):
    res = []
    for root, dirs, files in os.walk(dir):
        for f_name in files:
            name, suf = os.path.splitext(f_name)
            if suf == ext:
                res.append(os.path.join(root, f_name))
    return res


# 11.如果你的PC是4G内存，如何处理1个10G的csv文件
import pandas as pd


def read_bigfile(filename, sep=',', chunksize=5):
    reader = pd.read_csv(filename, sep=sep, chunksize=chunksize)
    while True:
        try:
            yield reader.get_chunk()
        except StopIteration:
            print('Read finish')
            break


# 12.统计一个单词本里面频次最高的10个单词
from collections import Counter, defaultdict
import re

d = defaultdict(int)


def read_line(fname):
    """
    使用yield进行数据读取逐行读取， 然后用正则进行清洗， 最后保存到default对象中
    :param fname:
    :return:
    """
    with open(fname, 'r', encoding='utf-8') as rf:
        for line in rf:
            yield line


def process(line):
    #     使用yield进行数据读取逐行读取， 然后用正则进行清洗， 最后保存到default对象中
    for w in re.sub('\w', " ", line).split():
        d[w] + 1


most10 = Counter(d).most_common(10)

