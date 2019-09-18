#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-17 10:20:31
@LastEditTime: 2019-09-17 15:12:20
@Description: 股票按照价格先后顺序放在数组中，只有买入之后才能卖出，有顺序之分
思路1：蛮力法，双重遍历数组，记录所有利润，取最大的利润，时间复杂度O(n^2)
思路2: 固定卖出价，寻找前面数组的最小值作为买入价，此时利润最大。只需要遍历一次数组，时间复杂度O(n)
->: 辅助数 卖出价之前的min_val，最大利润max_diff
@State: PYTHON35 PASS
'''
import sys
def max_money(lis):
    if not isinstance(lis, list):
        print("input is not list type!")
        sys.exit(1)
    if not lis:
        print("input is empyt!")
        sys.exit(1)
    min_val = lis[0]
    max_diff = lis[1]-min_val
    for i in range(2,len(lis)):
        if lis[i] < min_val:
            min_val = lis[i]
        tmp = lis[i] - min_val
        if tmp > max_diff:
            max_diff = tmp
    return max_diff

if __name__ == "__main__":
    lis = [9,11,8,5,7,12,16,14]
    print(max_money(lis))