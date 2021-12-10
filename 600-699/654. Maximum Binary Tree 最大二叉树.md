- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/maximum-binary-tree/description/

## 题目描述

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

1. The root is the maximum number in the array.
1. The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
1. The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.

Construct the maximum tree by the given array and output the root node of this tree.

Example 1:

	Input: [3,2,1,6,0,5]
	Output: return the tree root node representing the following tree:
	
		      6
		    /   \
		   3     5
		    \    / 
		     2  0   
		       \
		        1

Note:

- The size of the given array will be in the range [1,1000].


## 题目大意
根据数组的最大值分割进行构建二叉树。

## 解题方法
### 递归

找到数组中的最大值和最大值的位置，然后用切片的方式进行构建。如果数组为空，那么叶子为空。

Python代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        _max = max(nums)
        max_pos = nums.index(_max)
        root = TreeNode(_max)
        root.left = self.constructMaximumBinaryTree(nums[:max_pos])
        root.right = self.constructMaximumBinaryTree(nums[max_pos + 1:])
        return root
```

C++代码如下：

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        int N = nums.size();
        if (N == 0) return nullptr;
        int ind = 0, curMax = INT_MIN;
        for (int i = 0; i < N; i++) {
            if (nums[i] > curMax) {
                curMax = nums[i];
                ind = i;
            }
        }
        TreeNode* node = new TreeNode(curMax);
        vector<int> leftv = vector<int>(nums.begin(), nums.begin() + ind);
        vector<int> rightv = vector<int>(nums.begin() + ind + 1, nums.end());
        node->left = constructMaximumBinaryTree(leftv);
        node->right = constructMaximumBinaryTree(rightv);
        return node;
    }
};
```

## 日期

2018 年 2 月 5 日 
2018 年 12 月 2 日 —— 又到了周日
2019 年 9 月 27 日 —— 昨天面快手，竟然是纯刷题
