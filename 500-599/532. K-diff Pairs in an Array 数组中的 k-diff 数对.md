
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/k-diff-pairs-in-an-array/description/


## 题目描述

Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:

    Input: [3, 1, 4, 1, 5], k = 2
    Output: 2
    Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
    Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:

    Input:[1, 2, 3, 4, 5], k = 1
    Output: 4
    Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:

    Input: [1, 3, 1, 5, 4], k = 0
    Output: 1
    Explanation: There is one 0-diff pair in the array, (1, 1).

Note:

1. The pairs (i, j) and (j, i) count as the same pair.
1. The length of the array won't exceed 10,000.
1. All the integers in the given input belong to the range: [-1e7, 1e7].

## 题目大意

找出一个数组中有多少对数，使得这对数差的绝对值等于k。相同的一对数字只计算一次。

## 解题方法

### 字典

遇到数组中某数的和或者差在不在数组中都是用``字典``去算啊！这个题使用字典和set就能求出有多少个差为k的了，set能保证不重复计算相同的元素。

```python
import collections
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        answer = 0
        counter = collections.Counter(nums)
        for num in set(nums):
            if k > 0 and num + k in counter:
                answer += 1
            if k == 0 and counter[num] > 1:
                answer += 1
        return answer
```

二刷的时候，同样地使用字典，只不过是先对k进行了一个判断，这样当k是正数的时候，直接用set就解决了。所以这个速度打败了100%的提交。

```python
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        if k < 0: return 0
        elif k == 0:
            count = collections.Counter(nums)
            for n, v in count.items():
                if v >= 2:
                    res += 1
            return res
        else:
            nums = set(nums)
            for num in nums:
                if num + k in nums:
                    res += 1
            return res
```

C++版本的代码如下：

```cpp
class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        unordered_map<int, int> m;
        for (int num : nums) {
            m[num]++;
        }
        int res = 0;
        for (const auto &it : m) {
            if (k == 0 && it.second >= 2) {
                res ++;
            } else if (k > 0 && m.count(it.first + k)) {
                res ++;
            }
        }
        return res;
    }
};
```

## 日期

2018 年 2 月 4 日 
2018 年 11 月 27 日 —— 最近的雾霾太可怕
