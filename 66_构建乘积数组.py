#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-09-17 16:03:30
@LastEditTime: 2019-09-18 10:21:25
@Description: A[0,1,...,n-1],构建乘积数组B[i] = A[0]A[1]..A[i-1]A[i+1]..A[n-1]，不能使用除法。
思路1：直接连乘，这时需要两层循环，时间复杂度O(n^2)
思路2：辅助数组C[i],D[i],B[i] = C[i]D[i]
@State: PYTHON35 PASS
'''
import sys

def multify_array(A):
    if not isinstance(A, list):
        print("Input is not list type!")
        sys.exit(1)
    B,C,D = [],[1]*len(A),[1]*len(A)
    for i in range(1,len(A)):
        C[i] = C[i-1] * A[i-1]
    for j in range(1,len(A))[::-1]:
        D[j-1] = D[j] * A[j]
    for k in range(len(A)):
        B.append(C[k]*D[k])
    return B

if __name__ == "__main__":
    A = [2,3,4,5]
    print(multify_array(A))