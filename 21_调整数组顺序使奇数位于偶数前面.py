#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-08-29 11:05:13
@LastEditTime: 2019-08-29 15:16:29
@Description: 
# 可询问是否可借助辅助内存，还是在原数组基础上进行更改
# 1、双指针
# 2、增加代码复用，传入判断函数，主函数题不需要变动
@State: PYTHON35 PASS
'''

def reorder_odd_even(num,fcn=None):
    if not isinstance(num, list):
        print("Input must be list type!")
        return
    if len(num) <= 0:
        return []
    if len(num) == 1:
        return num
    left, right = 0, len(num)-1#lem是数字的长度，比索引值大一
    while(left < right):
        while num[left] % 2 == 1 and left < right: # 如果一直是奇数一直+1，不能是if，if只前进一次
            left += 1
        while num[right] % 2 == 0 and left < right:# 如果一直是偶数一直-1
            right -= 1
        # num[left], num[right] = num[right], num[left]
        tmp = num[left] 
        num[left] = num[right]
        num[right] = tmp    
    return num

def reorder_odd_even2(num,fcn):
    """
    args:list fcn:function
    """
    if not isinstance(num, list):
        print("Input must be list type!")
        return
    if len(num) <= 0:
        return []
    if len(num) == 1:
        return num
    left, right = 0, len(num)-1#lem是数字的长度，比索引值大一
    while(left < right):
        while fcn(num[left]) and left < right: # 传入函数
            left += 1
        while not fcn(num[right]) and left < right:# 
            right -= 1
        # num[left], num[right] = num[right], num[left]
        tmp = num[left] 
        num[left] = num[right]
        num[right] = tmp    
    return num
def my_fcn1(n):
    if n >= 0: return True
    if n < 0: return False
def my_fcn2(n):
    if n % 3 == 0: return True
    if n % 3 != 0: return False
if __name__ == "__main__":
    lis1 = [1,2,3,4,5]
    lis2 = [1,1,2,2,4,5,7]
    lis3 = [1]
    lis4 = []
    lis5 = [0,1,-1,2,-2,-3,3]
    lis5 = [0,1,-6,9,-2,-3,3]
    print(reorder_odd_even(lis1))
    print(reorder_odd_even(lis2))
    print(reorder_odd_even(lis3))
    print(reorder_odd_even(lis4))
    print(reorder_odd_even2(lis5,my_fcn1))
    print(reorder_odd_even2(lis5,my_fcn2))

