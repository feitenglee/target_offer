#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-01 18:52:12
@LastEditTime: 2019-09-03 09:55:39
@Description: 打印字符串的全排列
@State: NO PASS
'''

def perm(lis):
    permulation(lis,0)

def permulation(lis, n):
    if n >= len(lis):
        print(''.join(lis))
    for i in range(n, len(lis)):
        lis[i], lis[n] = lis[n], lis[i]
        permulation(lis,n+1)
        lis[i], lis[n] = lis[n], lis[i]

if __name__ == "__main__":
    lis = ['1','2']
    perm(lis)
