#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-05 11:23:20
@LastEditTime: 2019-09-05 14:40:08
@Description: 求从小到大的顺序第1500个丑数
丑数：只包含2,3,5因子的数。
思路1：判断每个整数是否是丑数，直到第index个数,缺点是判断丑数，时间代价极高
思路2：保存排好序的丑数数组，数组元素后面的元素是前面某个元素的2倍或3倍或5倍
->1:辅助数，丑数数组ugly_list=[1], 计数器num=0, 指针p2,p3,p5初始化为0
->2:外循环，向ugly_list添加2倍，3倍，5倍某数的最小值
->3:更新p2,p3,p5指针的位置为大于2倍，3倍，5倍的位置
@State: PYTHON35 PASS
'''

def ugly_num1(index):
    if index <= 0:
        return 0
    ugly_num = 0
    num = 0
    nums = []
    while ugly_num < index:
        num += 1
        if is_ugly(num):
            ugly_num += 1
            nums.append(num)
    print(nums)
    return num
def is_ugly(num):
    while num % 2 == 0:
        num = num // 2
    while num % 3 == 0:
        num = num // 3
    while num % 5 == 0:
        num = num // 5
    if num == 1: 
        return True
    return False

def ugly_num2(index):
    p2,p3,p5 = 0,0,0
    ugly_list= [1]
    num = 1
    while num < index:
        min_val = min(ugly_list[p2]*2,ugly_list[p3]*3,ugly_list[p5]*5)
        ugly_list.append(min_val)
        while ugly_list[p2] * 2 <= ugly_list[-1]:
            p2 += 1
        while ugly_list[p3] * 3 <= ugly_list[-1]:
            p3 += 1
        while ugly_list[p5] * 5 <= ugly_list[-1]:
            p5 += 1
        num += 1
    print(ugly_list)
    return ugly_list[-1]
    
if __name__ == "__main__":
    index = 1500
    # print(ugly_num1(1))
    # print(ugly_num1(2))
    # print(ugly_num1(10))
    print(ugly_num1(20))
    # print(ugly_num1(1500))
    print(ugly_num2(20))
    # print(ugly_num2(1500))