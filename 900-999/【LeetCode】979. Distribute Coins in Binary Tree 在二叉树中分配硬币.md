作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/distribute-coins-in-binary-tree/


## 题目描述

Given the ``root`` of a binary tree with ``N`` nodes, each ``node`` in the tree has ``node.val`` coins, and there are ``N`` coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.

 

Example 1:

![此处输入图片的描述][1]

    Input: [3,0,0]
    Output: 2
    Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.

Example 2:

![此处输入图片的描述][2]

    Input: [0,3,0]
    Output: 3
    Explanation: From the left child of the root, we move two coins to the root [taking two moves].  Then, we move one coin from the root of the tree to the right child.

Example 3:

![此处输入图片的描述][3]

    Input: [1,0,2]
    Output: 2

Example 4:

![此处输入图片的描述][4]

    Input: [1,0,0,null,3]
    Output: 4
     

Note:

1. 1<= N <= 100
1. 0 <= node.val <= N

## 题目大意

题目给出了一个二叉树，每个节点都有个数字代表当前节点有多少个金币，保证所有节点的金币数量之和等于节点个数。现在要求把金币平分到每个节点，使得每个节点都只放1个金币。问需要的移动次数是多少？

## 解题方法

### 递归

看到二叉树的题目我们一般想到递归，这个题也是如此。这个题是个难的的好题，确实很新颖。

首先，给定了一个二叉树的状态，只要不做重复移动，那么可以证明，移动是无状态的。也就是说，最终的移动次数不会因为先给谁后给谁，或者先移动几个再移动几个，再或者把某些金币移动到近的节点把另外一些金币移动到远的节点而有所不同。总之，我们可以放心大胆地，把金币移动到位，而不需要考虑把具体地金币移动到哪个确切的位置。

所以，我的思路就是分别统计左右子树缺少的金币个数，然后把每个节点和其子树总体的金币分配到位。累计所有节点和其子树所需要的移动次数就是结果。

每个子树缺少的金币数，等于节点数 - 金币数。因为题目确保了所有金币的和等于所有节点数，所以左子树缺少的金币数+该节点缺少的金币数+右子树缺少的金币数=0.我们每次把每个节点和其子树搞平衡，即左子树、该节点、右子树的节点数都等于金币数。注意此时，虽然左右子树总的不缺金币，但是内部仍然分配不均。所以，记录把这个节点搞平衡需要移动的金币数，然后累加上左子树和右子树搞平衡需要移动的金币数即为所求。

下面考虑，如果知道了左右子树需要的金币数，将他们搞平衡需要多少移动步数？答案是左右子树需要的金币数的绝对种子和。这个怎么理解？其实就是需要把子树多的金币挪给根节点，然后再从根节点分配给另一个缺少金币的子树对应的金币。举个栗子：

![此处输入图片的描述][5]

对于上面的树，左子树缺少-2个金币，右子树缺少1个金币。所以先把左子树多的那两个金币移动到根节点，然后根节点再给右子树分配缺的1个金币即可。因此总的移动次数是左右子树缺少的金币的和。

具体到代码，我们需要一个统计某个子树需要多少金币的函数need()；需要计算把自身，左右子树都平衡，需要移动的coins个数的函数helper()。

因为代码比较简单，已经有注释，我就不讲代码了。

c++代码如下：

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
    int distributeCoins(TreeNode* root) {
        int res = 0;
        helper(root, res);
        return res;
    }
    // 统计把自身，左右子树都平衡，需要移动的coins个数
    void helper(TreeNode* root, int& res) {
        if (!root) return;
        // 左、右子树缺多少
        int left = need(root->left);
        int right = need(root->right);
        //左，右子树和自身都平衡需要的移动数
        res += abs(left) + abs(right);
        helper(root->left, res);
        helper(root->right, res);
    }
    // 为了使该子树均匀，需要的coins数
    // 节点数 - coins
    int need(TreeNode* root) {
        if (!root) return 0;
        if (count_.count(root))
            return count_[root];
        int res = need(root->left) + 1 - root->val + need(root->right);
        count_[root] = res;
        return res;
    }
private:
    unordered_map<TreeNode*, int> count_;
};
```


## 日期

2019 年 1 月 20 日 —— 这次周赛有点简单


  [1]: https://assets.leetcode.com/uploads/2019/01/18/tree1.png
  [2]: https://assets.leetcode.com/uploads/2019/01/18/tree2.png
  [3]: https://assets.leetcode.com/uploads/2019/01/18/tree3.png
  [4]: https://assets.leetcode.com/uploads/2019/01/18/tree4.png
  [5]: https://assets.leetcode.com/uploads/2019/01/18/tree2.png
