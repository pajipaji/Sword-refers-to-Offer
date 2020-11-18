# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def buildTree(self, preorder, inorder) -> TreeNode:
#         if not preorder or not inorder:
#             return None
#         print(preorder)
#         node = TreeNode(preorder.pop(0))
#         ans = inorder.index(node.val)
#         pant = preorder.index(inorder[ans-1])
#         iant = preorder.index(inorder[ans-1])+1
#         print(pant, iant, preorder, 11111)
#         node.left = self.buildTree(preorder[ 0: pant], inorder[ : ans])
#         node.right = self.buildTree(preorder[iant+1: ], inorder[ans+1 : ])
#         return node

# a = Solution()
# b = [3,9,20,15,7]
# c = [9,3,15,20,7]
# d = a.buildTree(b,c)
# print(d)



def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            a = target - nums[i]
            for j in range(i+1,len(nums)):
                if a == nums[j]:
                    return [i,j]
nums = [3,2,4]
target = 6
a = twoSum(nums,target)
print(a)