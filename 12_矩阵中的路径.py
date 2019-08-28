# 2019-08-27
# by lifieteng@live.com
# 回溯法搜索路径
# 1、考虑边界情况 j-1<=0, i-1<=0
# 2、考虑不能往回走

# import numpy as np

def has_path(lis,s):
    if not lis or not s:
        return False
    rows = len(lis)
    cols = len(lis[0])
    # flags = np.array((rows,cols))
    for i in range(rows):
        for j in range(cols):
            flags = [[False]*cols for i in range(rows)]#创建多维列表,对每次重新搜索将flags清0
            if lis[i][j] == s[0]:
                flags[i][j] = True
                if find_path(lis,s[1:],rows,cols,i,j,flags):
                    return True
    return False # 如果上面for循环内的判断都不成立，进入这一句，少了这一句，没有return, 返回None
def find_path(lis,s,rows,cols,i,j,flags):
    # flags[i][j] = True
    if not s:
        return True
    if j + 1 < cols and lis[i][j+1] == s[0] and flags[i][j+1] == False:
        flags[i][j+1] = True
        return find_path(lis,s[1:],rows,cols,i,j+1,flags)
    
    elif j - 1 >= 0 and lis[i][j-1] == s[0] and flags[i][j-1] == False:
        flags[i][j-1] = True
        return find_path(lis,s[1:],rows,cols,i,j-1,flags)
    
    elif i + 1 < rows and lis[i+1][j] == s[0] and flags[i+1][j] == False:
        flags[i+1][j] = True
        return find_path(lis,s[1:],rows,cols,i+1,j,flags)
    
    elif i - 1 <= 0 and lis[i-1][j] == s[0] and flags[i-1][j] == False:
        flags[i-1][j] = True
        return find_path(lis,s[1:],rows,cols,i-1,j,flags)
    
    else:
        return False
    

if __name__ == "__main__":
    list1 = [['a','b','t','g'],\
             ['c','f','c','s'],\
             ['j','d','e','h']]
    s1 = 'bfce'

    list2 = [list('abfe'),list('abcd'),list('adce')]
    s2 = 'bbb'# 特殊用例，折返路径
    s3 = 'bbfe'
    print(has_path(list1,s1))
    print(has_path(list2,s2))
    print(has_path(list2,s3))