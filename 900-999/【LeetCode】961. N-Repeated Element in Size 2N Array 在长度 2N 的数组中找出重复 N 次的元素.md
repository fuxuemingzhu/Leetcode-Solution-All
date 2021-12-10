
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/n-repeated-element-in-size-2n-array/


## 题目描述

In a array ``A`` of size ``2N``, there are ``N+1`` unique elements, and exactly one of these elements is repeated N times.

Return the element repeated ``N`` times.

 
Example 1:

    Input: [1,2,3,3]
    Output: 3

Example 2:

    Input: [2,1,2,5,3,2]
    Output: 2

Example 3:

    Input: [5,1,5,2,5,3,5,4]
    Output: 5
 

Note:

1. 4 <= A.length <= 10000
1. 0 <= A[i] < 10000
1. A.length is even


## 题目大意

一个数组有2N个数字，其中有N+1个不同的数字。在这里边恰好有一个数字重复了N次，找出这个重复了N次的数字是什么。

## 解题方法

### 字典

只要是和次数有关的题目，可以直接使用字典解决。这个题直接统计每个数字出现的次数，然后把次数等于N的返回即可。

python代码如下：

```python
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A) / 2
        count = collections.Counter(A)
        for k, v in count.items():
            if v == N:
                return k
        return 0
```


C++代码如下：

```cpp
class Solution {
public:
    int repeatedNTimes(vector<int>& A) {
        const int N = A.size() / 2;
        unordered_map<int, int> m;
        for (int a : A) {
            m[a] ++;
        }
        for (auto x : m) {
            if (x.second == N) {
                return x.first;
            }
        }
        return 0;
    }
};
```


## 日期

2018 年 12 月 23 日 —— 周赛成绩新高


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79368360
