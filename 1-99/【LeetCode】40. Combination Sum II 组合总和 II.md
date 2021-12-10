
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/combination-sum-ii/description/


## 题目描述

Given a collection of candidate numbers (``candidates``) and a target number (``target``), find all unique `combinations` in ``candidates`` where the candidate numbers sums to ``target``.

Each number in candidates may only be used once in the combination.

Note:

1. All numbers (including target) will be positive integers.
1. The solution set must not contain duplicate combinations.

Example 1:

	Input: candidates = [10,1,2,7,6,1,5], target = 8,
	A solution set is:
	[
	  [1, 7],
	  [1, 2, 5],
	  [2, 6],
	  [1, 1, 6]
	]

Example 2:

	Input: candidates = [2,5,2,1,2], target = 5,
	A solution set is:
	[
	  [1,2,2],
	  [5]
	]

## 题目大意

使用候选集的数字，能有多少种不同的组合，使得每个组合的和都是target。但是这里给出的数字有重复，要求结果里面，相同的组合只能出现一次。

## 解题方法

### 方法一：DFS

这个题和之前的[39. Combination Sum](https://blog.csdn.net/fuxuemingzhu/article/details/79322462) 基本相同，这个题不允许一个数字多次出现，所以每次递归需要比上一轮开始的位置向后移动一个。

另外这个题一直做不出来的原因是把dfs的i写成了index...要注意内层递归的时候，传入的位置是i不是index.

输入:

[10,1,2,7,6,1,5]
8

结果：

[1, 1, 2, 5, 6, 7, 10]
[1, 1, 6]
[[1, 1, 6]]
[1, 2, 5]
[[1, 1, 6], [1, 2, 5]]
[1, 7]
[[1, 1, 6], [1, 2, 5], [1, 7]]
[2, 6]
[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

```python
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        print(candidates)
        res = []
        self.dfs(candidates, target, 0, res, [])
        return res

    def dfs(self, nums, target, index, res, path):
        if target < 0:
            return
        elif target == 0:
            res.append(path)
            return
        for i in xrange(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, target - nums[i], i + 1, res, path + [nums[i]])
```

### 方法二：回溯法

这个题的回溯法也很简单，代码没有什么大变化，需要改变的是，在递归的for循环里加上if (i > start && candidates[i] == candidates[i - 1]) continue; 这样可以防止res中出现重复项，然后就在递归调用helper里面的参数换成i+1，这样就不会重复使用数组中的数字了。

```cpp
class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        sort(candidates.begin(), candidates.end());
        helper(candidates, res, {}, target, 0);
        return res;
    }
    void helper(vector<int>& candidates, vector<vector<int>>& res, vector<int> path, int target, int start) {
        if (target < 0) return;
        if (target == 0) {
            res.push_back(path);
        }
        for (int i = start; i < candidates.size(); i++) {
            if (i > start && candidates[i] == candidates[i - 1])
                continue;
            path.push_back(candidates[i]);
            helper(candidates, res, path, target - candidates[i], i + 1);
            path.pop_back();
        }
    }
};
```

参考资料：

http://www.cnblogs.com/grandyang/p/4419386.html

## 日期

2018 年 2 月 21 日 
2018 年 12 月 19 日 —— 感冒了，好难受
