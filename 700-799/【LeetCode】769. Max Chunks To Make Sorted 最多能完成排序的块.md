
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/max-chunks-to-make-sorted/description/

## 题目描述

Given an array ``arr`` that is a permutation of ``[0, 1, ..., arr.length - 1]``, we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

Example 1:
    
    Input: arr = [4,3,2,1,0]
    Output: 1
    Explanation:
    Splitting into two or more chunks will not return the required result.
    For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
    
Example 2:
    
    Input: arr = [1,0,2,3,4]
    Output: 4
    Explanation:
    We can split into two chunks, such as [1, 0], [2, 3, 4].
    However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.

Note:

1. arr will have length in range [1, 10].
1. arr[i] will be a permutation of [0, 1, ..., arr.length - 1].

## 题目大意

一个数组，其数组是``[0, 1, ..., arr.length - 1]``打乱次序的一种组合。我们要把它进行划分成若干chunks，使得每个chunks进行排序并拼接之后得到的总数组是有序的。求最多多少个chunks.

## 解题方法

为什么新题总是那么相似？这个题也是只需要遍历一次即可。

思考一个问题，如果想要每个chunk排序拼接之后，得到的总chunk有序，那么说明每个chunk里面数字应该在某个区间内才可以。否则在chunk内进行排序，拼接之后会和其他的chunk的元素顺序不匹配。

因为所有数字是``[0, 1, ..., arr.length - 1]``的一个排列，很容易想到，一个区间内的最大的数字，不应该大于这个区间最右的index。

因此，我们从左向右进行遍历，如果已经观测到的最大值小于等于这个区间的index，那么就可以划分区间了。

举例子：

    对于：[1,0,2,3,4]
    从左到右遍历：
    1       目前最大值1，index = 0， 不可划分
    0       目前最大值1，index = 1， 可划分
    2       目前最大值2，index = 2， 可划分
    3       目前最大值3，index = 3， 可划分
    4       目前最大值3，index = 4， 可划分

代码如下：

```python
class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        chunks = 0
        pre_max = 0
        for i, num in enumerate(arr):
            if num > pre_max:
                pre_max = num
            if pre_max == i:
                chunks += 1
        return chunks
```

二刷，使用的方法和上面一样。需要注意的是，第二个if并不是if else，因为我们要时刻保持当前的最大值，当最大值等于当前的索引的时候，把结果+1.

```cpp
class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        const int N = arr.size();
        int res = 0;
        int preMax = 0;
        for (int i = 0; i < N; i++) {
            if (arr[i] > preMax)
                preMax = arr[i];
            if (i == preMax)
                res++;
        }
        return res;
    }
};
```

## 日期

2018 年 5 月 28 日 —— 太阳真的像日光灯～
2018 年 12 月 18 日 —— 改革开放40周年
