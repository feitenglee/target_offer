#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-17 18:20:13
@LastEditTime: 2019-09-17 18:46:09
@Description: 
@State: PYTHON35 PASS
'''

def find_flower(m, n):
    if m < 100 or m > 999 or n < 100 or n >999 or m >n:
        return 
    res = []
    for i in range(m, n+1):
        num_str = str(i)
        a,b,c = num_str[0],num_str[1],num_str[2]
        if i == pow(int(a),3) + pow(int(b),3) + pow(int(c),3):
            res.append(i)
    if len(res) == 0:
        print("no")
        return "no"
    for x in res:
        print(x, end=' ')

if __name__ == "__main__":
    # input_str = input("")
    # input_lis = input_str.split(" ")
    # m,n = int(input_lis[0]),int(input_lis[1])
    a,b = input("").split()
    m,n = int(a),int(b)
    find_flower(m,n)
    # a,b = input("").split()
    # print(a,b)