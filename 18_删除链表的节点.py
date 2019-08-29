# 2019-08-26 PASS
# by lifeiteng@live.com
# O(1)时间删除单向链表中的某个节点，常规做法是遍历链表，找到待删除节点前一个节点，时间复杂度O（n）
# 考虑三种情况：1、链表中只有一个节点（不包括哑节点）2、待删除节点在中间3、待删除节点是尾节点

class Node:
    def __init__(self, data, p = None):
        self.data = data
        self.next = p
    def __del__(self):# 类的析构函数
        self.data = None
        self.next = None
        
class Chain:
    def __init__(self):
        self.head = Node(None)
    # def creat(self, data):
    #     if len(data) == 0:
    #         print('list is none!')
    #         return
    #     self.head.next = Node(data[0])
    #     p = self.head.next
    #     for i in data[1:]:
    #         p.next = Node(i)
    #         p = p.next
    def print(self):
        p = self.head.next
        while p != None:
            print(p.data,end='->')
            p = p.next
        print('None')#仅仅是打印换行键
def delete_node(chain, to_be_deleted):
    if not isinstance(chain,Chain) or not isinstance(to_be_deleted,Node):
        return
    # 待删除的节点不是尾节点
    if to_be_deleted.next != None:
        temp_node = to_be_deleted.next
        to_be_deleted.data = temp_node.data
        to_be_deleted.next = temp_node.next
    elif chain.head.next == to_be_deleted:
        chain.head.next = None
    else:
        p = chain.head.next
        # 待删除节点在尾节点，顺序遍历
        while p.next != to_be_deleted:
            p = p.next
        p.next = None

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    s = Chain()
    s.head.next = node1
    s.print()
    delete_node(s,node2)
    s.print()

    # s1 = Chain()
    # s1.creat([1,2,3,4])
    # s1.print()
    # delete_node(s1,node2)
    # s1.print()
        

