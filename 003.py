#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-17 20:37:15
@LastEditTime: 2019-09-17 20:54:44
@Description: 
@State: PYTHON35 PASS
'''

def main(lis,n):
    for i in range(4,n):
        tmp = sum(lis)-lis[1]
        lis.append(tmp)
        lis.pop(0)

    print(lis[-1])
    print(lis)

if __name__ == "__main__":
    a,b,c,d,index = input("").split()
    lis = []
    lis.append(int(a))
    lis.append(int(b))
    lis.append(int(c))
    lis.append(int(d))
    n = int(index)
    main(lis,n)