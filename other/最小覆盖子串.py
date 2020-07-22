def miniWindow(s, t):
    need = {}
    window = {}
    INT_MAX = len(s) + 1 

    for char in list(t):
        need[char] = need.get(char,0) + 1

    left,right,valid = 0,0,0

    # 记录最小覆盖子串的起始索引及长度
    start, len = 0, INT_MAX

    while(right < len(s)):
        # c是将移入窗口的字符
        c = s[right]
        # 右移窗口
        right += 1
        # 进行窗口内数据的一系列更新
        if ():
