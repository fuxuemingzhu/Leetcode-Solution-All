- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)


---
@[TOC](目录)


题目地址：[https://leetcode.com/problems/combination-sum/description/][1]


## 题目描述


Given a ``set`` of candidate numbers (candidates) (``without duplicates``) and a target number (``target``), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

- All numbers (including target) will be positive integers.
- The solution set must not contain duplicate combinations.

Example 1:

	Input: candidates = [2,3,6,7], target = 7,
	A solution set is:
	[
	  [7],
	  [2,2,3]
	]

Example 2:

	Input: candidates = [2,3,5], target = 8,
	A solution set is:
	[
	  [2,2,2,2],
	  [2,3,3],
	  [3,5]
	]

## 题目大意

使用候选集的数字，能有多少种不同的组合，使得每个组合的和都是target。

## 解题方法

### 方法一：递归

使用递归解法，这个递归方法是，依次遍历每个元素，判断其与剩余数字的大小，如果比剩余target小，那么就放入到路径path中，并且，把剩余元素target减去当前元素。

理解递归最重要的当然是递归函数的定义：以index为起始元素，在candidates的index元素和其之后的元素中，抽取一定的元素，能否构成和为target的路径Path。

Python代码如下：

```python
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, res, [])
        return res
    
    
    def dfs(self, nums, target, index, res, path):
        if target < 0:
            return
        elif target == 0:
            res.append(path)
            return
        for i in xrange(index, len(nums)):
            if nums[index] > target:
                return
            self.dfs(nums, target - nums[i], i, res, path + [nums[i]])
```

### 方法二：回溯法

上面的DFS虽说也是递归，但是和回溯还是有区别的。因为回溯的含义，此路不通就倒着走回去，而上面的DFS是进行了全集的搜索。

这个回溯还是很好写的，需要一个新的函数，含义是从候选集的start位置开始向后寻找和为target的路径。如果target等于０了就是我们终止的一个条件，即正好搜索到了一条合适的路径。

需要注意的是path后面的插入元素和弹出元素操作。向path中添加元素i后进行后面的搜索，搜索完之后说明i位置的所有结果都已经结束了，故向后退一步即弹出最后的元素。

另外就是题目允许每个数字使用多次，所以for循环开始的地方是start，而往回溯函数里面传递的i的也是start.

C++代码如下：

```cpp
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> path;
        helper(candidates, 0, res, path, target);
        return res;
    }
    void helper(vector<int>& candidates, int start, vector<vector<int>>& res, vector<int>& path, int target) {
        if (target < 0) return; 
        if (target == 0) {
            res.push_back(path);
        }
        for (int i = start; i < candidates.size(); ++i) {
            path.push_back(candidates[i]);
            helper(candidates, i, res, path, target - candidates[i]);
            path.pop_back();
        }
    }
};
```

## 日期

2018 年 2 月 13 日 
2018 年 12 月 19 日 —— 感冒了，好难受
2019 年 9 月 25 日 —— 做梦都在秋招，这个秋天有毒
