'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/Target-Offer
@Date: 2019-08-28 14:52:23
@LastEditTime: 2019-08-29 15:04:38
@Description: 大数问题,避免输出特别大的数，使用字符串代替int型数字
@State: PYTHON35 PASS
'''

def print_num(n):
    if n <= 0:
        print("n must be positive!")
        return
    number = ['0']*n
    index = 0
    while not Increment(number):
        print_define(number)
        index += 1
        if index % 10 == 0:
            print()
        

def Increment(number):
    # 实现字符串加1，并判断有没有溢出，溢出返回true,不溢出返回false
    # number 是list
    if not isinstance(number,list):
        return
    is_overflow = False
    take_over = 0
    length = len(number)
    for i in range(length)[::-1]:# 遍历数字的个位数到最高位
        nsum = int(number[i]) + take_over
        if i == length - 1: # 个位+1
            nsum += 1
        if nsum >= 10:#发生进位
            if i == 0:#最高位为0，如两位数 00
                is_overflow = True
            else:
                nsum -= 10
                take_over = 1
                number[i] = str(nsum)
        else:#未发生进位
            number[i] = str(nsum)
            break #各位+1且不进位，不对高位进行操作，终结循环
    return is_overflow

def print_define(number):
    if not isinstance(number,list):
        print("number must be str!")
    is_begin_0 = True
    
    for i in range(len(number)):
        if number[i] != '0':
            is_begin_0 = False
        if not is_begin_0:
            print(number[i],end='')
    print('',end=' ')
    
if __name__ == "__main__":
    # print_num(3)
    # print_num(1)
    print_num(0)
    # print_num(3)