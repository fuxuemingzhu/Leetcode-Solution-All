
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/top-k-frequent-elements/description/

## 题目描述

Given a non-empty array of integers, return the k most frequent elements.

For example,

	Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 

1. You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
1. Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

## 解题方法

把出现次数最大的前k个数输出。

## 解题方法

### 字典

这个题要求时间复杂度是O(nlogn)，就可以按照出现的次数先排个序，然后找到出现最多的k个就好。Counter类有most_common()函数，能按出现的次数进行排序。返回的是个列表，列表中每个元素都是一个元组，元组的第一个元素是数字，第二个数字是出现的次数。

```python
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = Counter(nums).most_common()
        return [counter[i][0] for i in range(k)]
```

### 优先级队列

使用优先级队列来让出现次数多的优先弹出来，当然需要字典统计次数。

```cpp
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> m;
        for (int n : nums) m[n] ++;
        priority_queue<pair<int, int>> p;
        for (auto a : m)
            p.push({a.second, a.first});
        vector<int> res;
        for (int i = 0; i < k; i++) {
            res.push_back(p.top().second); p.pop();
        }
        return res;
    }
};
```


## 日期

2018 年 2 月 8 日 
2018 年 12 月 14 日 —— 12月过半，2019就要开始

