#!/usr/bin/env python
'''
@Author: lifeiteng@live.com
@Github: https://github.com/feitenglee/target_offer
@Date: 2019-08-29 21:20:30
@LastEditTime: 2019-08-31 14:45:39
@Description: 递归，遍历二叉树,比较树1中是否包含树2所有节点
@State: PYTHON35 PASS
'''
class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def has_subtree(root1,root2):
    if not isinstance(root1, TreeNode) or not isinstance(root2, TreeNode):
        return False
    res = False
    # if root1 and root2:
    if root1.data == root2.data:
        res = tree1_has_tree2(root1, root2)
    if not res:
        res = has_subtree(root1.left, root2)
    if not res:
        res = has_subtree(root1.right, root2)
    return res
     
def tree1_has_tree2(root1,root2):
    if not root2:# root2为空，说明已经遍历到root2的叶节点，说明上面的节点都相等
        return True
    if not root1:
        return False
    if root1.data != root2.data:
        return False
    return tree1_has_tree2(root1.left,root2.left) and \
           tree1_has_tree2(root1.right, root2.right)


if __name__ == "__main__":
    """
    树1
           8
         /   \
        8     7
       / \
      9   2
         / \
        4   7
     """
    node1 = TreeNode(8)
    node2 = TreeNode(8)
    node3 = TreeNode(7)
    node4 = TreeNode(9)
    node5 = TreeNode(2)
    node6 = TreeNode(4)
    node7 = TreeNode(7)

    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    node5.left, node5.right = node6, node7

    node8 = TreeNode(8)
    node9 = TreeNode(9)
    node10 = TreeNode(2)

    """
    树2
            8
           / \
          9   2
    """
    node8.left, node8.right = node9, node10
    print(has_subtree(node1, node8))
