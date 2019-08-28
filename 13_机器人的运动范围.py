# 2019-08-27
# by lifieteng@live.com
# 回溯法求解可到达的格子个数
# 1、考虑边界情况 j-1<=0, i-1<=0
# 2、不用考虑不满足条件从根节点重新出发的问题

def moving_count(rows,cols,threshold):
    """
    args: rows, cols and threshold
    return: counts (int)
    """
    if rows <=0 or cols <=0 or threshold <0:
        return 0
    visited = [[0]*cols for i in range(rows)]
    counts = back_track(rows, cols, threshold, 0, 0, visited)
    return counts

def back_track(rows, cols, threshold, i, j, visited):
    counts = 0   
    if check(rows, cols, threshold, i, j, visited):
        visited[i][j] = True
        counts = 1 + back_track(rows,cols,threshold,i+1,j,visited) \
                   + back_track(rows,cols,threshold,i-i,j,visited) \
                   + back_track(rows,cols,threshold,i,j+1,visited) \
                   + back_track(rows,cols,threshold,i,j-1,visited)   
    return counts

def check(rows, cols, threshold, i, j, visited):
    if i>=0 and i < rows and j >=0 and j < cols and get_item_sum(i,j) <= threshold and not visited[i][j]:
        return True
    return False

#计算数位之和，将数字转换成字符串
def get_item_sum(i,j):
    sum = 0
    for x in str(i):
        sum += int(x)
    for y in str(j):
        sum += int(j)
    return sum

if __name__ == "__main__":
    print(moving_count(10,10,10))

