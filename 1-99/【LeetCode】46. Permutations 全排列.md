- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)


---
@[TOC](目录)

题目地址：https://leetcode.com/problems/permutations/description/


## 题目描述

Given a collection of distinct numbers, return all possible permutations.

For example,

    [1,2,3] have the following permutations:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]

## 解题方法

### 方法一：库函数

使用python自带的permutations函数，直接进行全排列。

```python
from itertools import permutations
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(permutations(nums))
```

C++中也有next_permutation函数，但是注意需要先排序。

```cpp
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        do {
            res.push_back(nums);
        } while (next_permutation(nums.begin(), nums.end()));
        return res;
    }
};
```

### 方法二：递归

如果仔细观察题目全排列的输出结果就会发现，所谓全排列就是以每个nums中每个数字为起始位置，将剩余的数字全排列。所以可以使用递归求解。

想解决递归问题，必须对函数的定义十分了解。代码中定义的`dfs()`是对nums进行全排列，已有的排列结果放到path中，当nums为空时说明递归完成，把path放入res中。

Python代码如下：

```python
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, res, [])
        return res
        
    def dfs(self, nums, res, path):
        if not nums:
            res.append(path)
        else:
            for i in xrange(len(nums)):
                self.dfs(nums[:i] + nums[i + 1:], res, path + [nums[i]])
```

-----

### 方法三：回溯法

回溯法是解决排列问题的经典方法，速度也能明显加快。

回溯法的含义是对每个可能的结果进行遍历，如果某个数字已经使用则跳过，如果没有使用则放入path中。这个“回溯”怎么理解？我认识是在递归的过程中使用了一个数组path来保存自己走过的路，如果沿着这条路走完了全部的解，则需要弹出path中的最后一个元素，相当于向后回退，于是叫做回溯法。

下面的做法中，使用了visited数组来保存是否经历过这个位置。


C++版本的代码如下：

```cpp
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        const int N = nums.size();
        vector<vector<int>> res;
        vector<int> path;
        vector<int> visited(N, 0);
        dfs(nums, 0, visited, res, path);
        return res;
    }
private:
    void dfs(vector<int>& nums, int pos, vector<int>& visited, vector<vector<int>>& res, vector<int>& path) {
        const int N = nums.size();
        if (pos == N) {
            res.push_back(path);
            return;
        }
        for (int i = 0; i < N; i++) {
            if (!visited[i]) {
                visited[i] = 1;
                path.push_back(nums[i]);
                dfs(nums, pos + 1, visited, res, path);
                path.pop_back();
                visited[i] = 0;
            }
        }
    }
};
```

Python代码如下：

```python
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        visited = [0] * len(nums)
        res = []
        
        def dfs(path):
            if len(path) == len(nums):
                res.append(path)
            else:
                for i in range(len(nums)):
                    if not visited[i]:
                        visited[i] = 1
                        dfs(path + [nums[i]])
                        visited[i] = 0
        
        dfs([])
        return res
```


## 日期


2018 年 2 月 24 日 
2018 年 12 月 14 日 —— 12月过半，2019就要开始
2019 年 9 月 25 日 —— 做梦都在秋招，这个秋天有毒

  [1]: http://img.blog.csdn.net/20150926195427474
