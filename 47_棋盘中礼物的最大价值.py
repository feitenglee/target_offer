#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-05 10:38:24
@LastEditTime: 2019-09-05 10:53:51
@Description: 
公式f(x,y) = max(f(i-1,j),f(i,j-1)) + val(i,j)
辅助数组 棋盘每个位置(i,j)的最大值矩阵
@State: PYTHON35 PASS
'''
def max_value_of_gift(values):
    if not values:
        return 0
    rows, cols = len(values),len(values[0])
    max_value = [[0 for i in range(cols)] for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            left,up = 0,0
            if i > 0:
                up = max_value[i-1][j]
            if j > 0:
                left = max_value[i][j-1]
            max_value[i][j] = max(up,left) + values[i][j]
    print(max_value)
    return max_value[rows-1][cols-1]


if __name__ == "__main__":
    values = [[1,10,3,8],
              [12,2,9,6],
              [5,7,4,11],
              [3,7,16,5]]
    print(max_value_of_gift(values))