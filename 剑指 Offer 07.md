##### 剑指 Offer 07
###### 重建二叉树

`输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。`

```
例如，给出
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：
    3
   / \
  9  20
    /  \
   15   7
 
即输入：
[3,9,20,15,7]
[9,3,15,20,7]
输出：
[3,null,15]
预期：
[3,9,20,null,null,15,7]

限制：
0 <= 节点个数 <= 5000
```

##### 题解：
`考察对二叉树前中数组的排列规律`
```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if not preorder or not inorder:
            return None
        node = TreeNode(preorder.pop(0))
        ans = inorder.index(node.val)
        node.left = self.buildTree(preorder, inorder[ : ans])
        node.right = self.buildTree(preorder, inorder[ans+1 : ])
        return node
```
