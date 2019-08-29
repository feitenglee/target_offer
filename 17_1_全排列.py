'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/Target-Offer
@Date: 2019-08-28 20:05:50
@LastEditTime: 2019-08-29 15:05:11
@Description: 全排列，递归解法
@State: DONT PASS
'''

def perm(ls, start, end):
    if(start >= end):
        print(ls)
    else:
        for i in range(start, end + 1):
            ls[start], ls[i] = ls[i], ls[start]
            perm(ls, start + 1, end)
            ls[start], ls[i] = ls[i], ls[start]

def main():
    ls = [1,2,3,4]
    perm(ls, 0, 3)

if __name__ == "__main__":
    main()
