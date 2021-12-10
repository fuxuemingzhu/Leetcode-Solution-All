
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/search-a-2d-matrix/description/

## 题目描述

A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.

Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]… By that analogy, we stop adding right before a duplicate element occurs in S.

Example 1:

    Input: A = [5,4,0,3,1,6,2]
    Output: 6
    Explanation: 
    A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.
    
    One of the longest S[K]:
    S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}

Note:

1. N is an integer within the range [1, 20,000].
1. The elements of A are all distinct.
1. Each element of A is an integer within the range [0, N-1].
    
## 题目大意

给出了一个数组，找出从任意位置出发，把该位置的数字当做下一个索引的位置，最后肯定会终止于环路。找出最长的环长。

## 解题方法

本身思路很简单，就是用一个数组来保存某个位置是否被访问过，如果被访问过说明就是成了一个环，终止并记录最大环长。

直接这么做会超时，一个很机智的做法是，把visited数组放到for循环的外边，这样可以当新的环路计算的时候，如果以前的环访问过该位置的话，就不再计算了。道理是，给出的数组nums的数字范围是``0~N-1``，也就是说没有重复的数字，那么前面访问过的一个串的长度不会小于后面。

比如题目中给出的例子，在对以index = 0开始的串进行遍历的时候，会对0,5,6,2这几个位置进行标记过已经访问了。当index = 5,6,2时，以index开头的串的长度不会超过以0开头的串的长度。

    A = [5,4,0,3,1,6,2]
    One of the longest S[K]:
    S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}

代码：

```python
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 放在这里
        visited = [False] * len(nums)
        ans = 0
        for i in xrange(len(nums)):
            road = 0
            while not visited[i]:
                road += 1
                # 下面两行的顺序不能变
                visited[i] = True
                i = nums[i]
            ans = max(ans, road)
        return ans
```

C++代码如下：

```cpp
class Solution {
public:
    int arrayNesting(vector<int>& nums) {
        int res = 0;
        const int N = nums.size();
        vector<bool> visited(N, false);
        for (int i = 0; i < N; i ++) {
            int path = 0;
            while (!visited[i]) {
                visited[i] = true;
                path += 1;
                i = nums[i];
            }
            res = max(res, path);
        }
        return res;
    }
};
```

## 日期

2018 年 3 月 6 日 
2018 年 12 月 15 日 —— 今天四六级

  [1]: http://blog.csdn.net/fuxuemingzhu/article/details/79459200
