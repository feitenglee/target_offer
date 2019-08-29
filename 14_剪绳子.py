# 2019-08-28
# by lifieteng@live.com
# 1、动态规划解法
# 2、贪婪算法解法

def max_product(length):
    if length <= 1:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2
    # 存储最小子问题最优解
    products = [0]*(length+1)
    products[1] = 1
    products[2] = 2
    products[3] = 3
    for n in range(4,length+1):
        max_val = 0
        for i in range(1,int(n/2)+1):# 注意边界条件range是右开的！
            product = products[i] * products[n-i]#最优公式f(n)=f(i)*f(n-i)
            if product > max_val:
                max_val = product
        products[n] = max_val
    return products[length]
    # return products

if __name__ == "__main__":
    print(max_product(8))
    print(max_product(10))