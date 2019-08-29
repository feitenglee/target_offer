# 2019-08-28
# by lifieteng@live.com
# 二维矩阵上的回溯问题，leetcode-#51
# 题目描述：n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 输入输出：给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
# 示例：
# 输入: 4
# 输出: [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]

def NQueen(n):
    """
    args: n
    return res(list)
    """
    if n <= 0:
        return []
    if n == 1:
        return ["Q"]
    Q = ["."*n for i in range(n)]
    for row in range(n):
        for col in range(n):
            return back_track(n, row, col,Q)


def back_track(n, i, j,Q):
    Q[i][j] = 'Q'
    if len(lis) == n:
        res.append(lis)
    
    for x in range(n):
        for y in range(n):
            if check(i,j,x,y):
                Q[x][y] = 'Q'
                back_track(n, x, y, Q)

    return res

def check(i,j,k,l):
    if k != i or l != j or abs(k-i) != abs(l-j):
        return True
    return False


if "__name__" == "__main__":
    print(NQueen(4))
    print(NQueen(8))