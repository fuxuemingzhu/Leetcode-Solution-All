
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/longest-harmonious-subsequence/description/][1]


## 题目描述

We define a harmonious array is an array where the difference between its maximum value and its minimum value is **exactly** 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its **possible** subsequences.

    Example 1:

    Input: [1,3,2,2,5,2,3,7]
    Output: 5
    Explanation: The longest harmonious subsequence is [3,2,2,2,3].

Note: The length of the input array will not exceed 20,000.

## 题目大意

一个和谐子序列是数组中的最大值和最小值的差值恰好是1，求给定数组的最长和谐子序列。


## 解题方法

### 统计次数

重点是对题目进行抽象，这个题可以把和谐子序列抽象成一个只存在相邻两个数字的数组，位置无所谓的。

那么，我们应该，先数每个数字出现的次数，然后对每个数字num，找num+1是否存在，如果存在就记录两个和的最大值。

```python
from collections import Counter
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)
        nums_set = set(nums)
        longest = 0
        for num in nums_set:
            if num + 1 in counter:
                longest = max(longest, counter[num] + counter[num + 1])
        return longest
```

二刷的时候写了同样的解法，并且更简单一点：

```python
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        res = 0
        for num in count.keys():
            if num + 1 in count:
                res = max(res, count[num] + count[num + 1])
        return res
```

C++代码如下：

```cpp
class Solution {
public:
    int findLHS(vector<int>& nums) {
        map<int, int> d;
        for (int n : nums) d[n] ++;
        int res = 0;
        for (auto n : d) {
            if (d.count(n.first + 1))
                res = max(res, n.second + d[n.first + 1]);
        }
        return res;
    }
};
```

## 日期

2018 年 2 月 1 日 
2018 年 11 月 19 日 —— 周一又开始了
2018 年 12 月 7 日 —— 恩，12月又过去一周了

  [1]: https://leetcode.com/problems/longest-harmonious-subsequence/description/
