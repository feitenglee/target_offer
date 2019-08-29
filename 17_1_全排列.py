# 2019-08-26 REFUCE
# by lifeiteng@live.com
# 全排列，递归解法
#  遗留问题，不懂
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
