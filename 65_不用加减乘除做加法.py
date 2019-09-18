#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-17 15:12:39
@LastEditTime: 2019-09-17 16:01:34
@Description: 二进制的位运算代替加法
思路：
->1:二进制的加法可以看成异或运算，这时没有考虑进位
->2:进位可以看成是与运算，然后左移一位
->3:将异或运算，与运算结果相加，重复步骤1，2，直到异或没有进位，进行或运算
@State: PYTHON35 PASS
'''
import sys
def add_without_exp(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        print("input is not int type!")
        sys.exit(1)
    #python中位运算的输入直接是10进制整数，不需要先转换成二进制
    while b != 0:
        sum_ = a^b #异或运算
        carry = (a&b)<<1 #与运算, 注意左移的优先级比与高，需要加括号
        a = sum_
        b = carry
    return sum_

if __name__ == "__main__":
    print(add_without_exp(5,17))
    print(add_without_exp(15,17))
    print(add_without_exp(2,3))
    print(add_without_exp(0,17))
    print(add_without_exp(-1,17))# 负数位运算不支持
    
