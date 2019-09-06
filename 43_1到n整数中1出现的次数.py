#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-03 20:29:06
@LastEditTime: 2019-09-03 21:14:46
@Description: 统计1-n中数字1出现的次数
思路1:遍历1-n，分别判断每个数是否包含1，例如11包含两个1
->1:遍历1-n，调用contain1函数
->2:包含1算法，对10取余是否为1，再整数10更新n
@State: PYTHON35 PASS
'''
import sys
def nums_1_and_n(n):
    if not isinstance(n, int):
        print("input is not int type")
        sys.exit(1)
    if n < 1:
        print("n must be not less than 1")
        sys.exit(1)
    nums = 0
    for i in range(1,n+1):
        nums += nums_of_1(i)
    return nums
def nums_of_1(n):
    nums = 0
    while n:
        if n % 10 == 1:
            nums += 1
        n = n / 10
    return nums

if __name__ == "__main__":
    # n = 12
    # print(nums_1_and_n(12))
    print(nums_1_and_n(1))
    print(nums_1_and_n(11))