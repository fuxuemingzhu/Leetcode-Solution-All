
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/find-largest-value-in-each-tree-row/#/description][1]


## 题目描述


You need to find the largest value in each row of a binary tree.

Example:

	Input: 
	
	          1
	         / \
	        3   2
	       / \   \  
	      5   3   9 
	
	Output: [1, 3, 9]

## 题目大意

找出二叉树每层的最大值元素。

## 解题方法

### BFS

BFS，可以背下来了。用一个队列保存每层的节点。记录下来每层的节点数目，把这个层的遍历结束，然后找出这个层的最大值。把每层的最大值保存下来，最后返回即可。

注意，level要在循环体里面初始化。

Python代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = collections.deque()
        res = []
        queue.append(root)
        while queue:
            size = len(queue)
            max_level = float("-inf")
            for i in range(size):
                node = queue.popleft()
                if not node: continue
                max_level = max(max_level, node.val)
                queue.append(node.left)
                queue.append(node.right)
            if max_level != float("-inf"):
                res.append(max_level)
        return res
```

C++代码如下。C++版本的如果按照python写就会把最后一层的叶子放进去，但是python版本就没有，没看懂为啥。另外C++使用了long型最小值，这样才能避免有INT_MIN的叶子节点存在。

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
    vector<int> largestValues(TreeNode* root) {
        queue<TreeNode*> q;
        vector<int> res;
        q.push(root);
        while (!q.empty()) {
            int size = q.size();
            long max_level = LONG_MIN;
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front(); q.pop();
                if (!node) continue;
                max_level = max(max_level, (long)node->val);
                q.push(node->left);
                q.push(node->right);
            }
            if (max_level != LONG_MIN)
                res.push_back(max_level);
        }
        return res;
    }
};
```

Java代码如下：

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public List<Integer> largestValues(TreeNode root) {
        List<Integer> ans = new ArrayList<Integer>();
        if(root == null){
            return ans;
        }
        int level;
        int size;
        Queue<TreeNode> tree = new LinkedList<TreeNode>();
        tree.offer(root);
        TreeNode curr = null;
        while(!tree.isEmpty()){
            level = Integer.MIN_VALUE;
            size = tree.size();
            for(int i = 0; i < size; i++){
                curr = tree.poll();
                level = Math.max(level, curr.val);
                if(curr.left != null){
                    tree.offer(curr.left);
                }
                if(curr.right != null){
                    tree.offer(curr.right);
                }
            }
            ans.add(level);
        }
        return ans;
    }
}
```

### DFS

使用DFS进行搜索代码就是层次遍历+每层取最大值。

Python代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        levels = []
        self.dfs(root, levels, 0)
        return [max(l) for l in levels]
    
    def dfs(self, root, levels, level):
        if not root: return
        if level == len(levels): levels.append([])
        levels[level].append(root.val)
        self.dfs(root.left, levels, level + 1)
        self.dfs(root.right, levels, level + 1)
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
    vector<int> largestValues(TreeNode* root) {
        dfs(root, levels, 0);
        vector<int> res;
        for (int i = 0; i < levels.size(); i++) {
            res.push_back(*max_element(levels[i].begin(), levels[i].end()));
        }
        return res;
    }
private:
    vector<vector<int>> levels;
    void dfs(TreeNode* root, vector<vector<int>>& levels, int level) {
        if (!root) return;
        if (levels.size() == level) levels.push_back({});
        levels[level].push_back(root->val);
        dfs(root->left, levels, level + 1);
        dfs(root->right, levels, level + 1);
    }
};
```

## 日期

2017 年 4 月 15 日 
2018 年 12 月 7 日 —— 恩，12月又过去一周了

  [1]: https://leetcode.com/problems/find-largest-value-in-each-tree-row/#/description
