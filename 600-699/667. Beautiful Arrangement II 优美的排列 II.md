作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/beautiful-arrangement-ii/description/

## 题目描述

Given two integers ``n`` and ``k``, you need to construct a list which contains n different positive integers ranging from 1 to n and obeys the following requirement: 
Suppose this list is ``[a1, a2, a3, ... , an]``, then the list ``[|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|]`` has exactly k distinct integers.

If there are multiple answers, print any of them.

Example 1:

    Input: n = 3, k = 1
    Output: [1, 2, 3]
    Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.

Example 2:

    Input: n = 3, k = 2
    Output: [1, 3, 2]
    Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.

Note:

1. The n and k are in the range 1 <= k < n <= 104.


## 题目大意

完美分配的变种。这种完美匹配的定义是指，给出一种排列，其相邻元素的差的绝对值有指定值k种。

## 解题方法

借鉴了大神的思路。

举例来说，``1 2 3 4 5 6 7 8 9 10``. 相邻元素的差值绝对值为1，出现了很多次。我们把后面部分的数字翻转一次，那么使得10和1临近到了一起，其他的数字的排列没有变化: ``1 10 9 8 7 6 5 4 3 2``，此时就有了2种不同的临近数字的差值绝对值. 继续做下去，把9到2的数字再翻转，就有了3种不同的临近数字的差值绝对值: ``1 10 2 3 4 5 6 7 8 9``.以此类推，找出k次即可。

```python
class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        a = list(range(1, n + 1))
        for i in range(1, k):
            a[i:] = a[:i-1:-1]
        return a
```

上面的python代码是靠不停地翻转得到的，其实，也可以不用翻转，而是我们每次选取一个数字放到结果数组里面。选取的方式是从两头向中间取，这样取的时候，能够保证每次取一个数字就会产生一个不同的差值，也就需要把k减去一。当k还剩1的时候，把后面的数字从小到大排列即可，这样后面的数字的差值是1.也就是说，我们最后产生了k个不同的差值。

```python
class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res = []
        l, r = 1, n
        while l <= r:
            if k > 1:
                if k % 2 == 1:
                    res.append(l)
                    l += 1
                else:
                    res.append(r)
                    r -= 1
                k -= 1
            else:
                res.append(l)
                l += 1
        return res
```

上面这个做法的C++代码如下：

```cpp
class Solution {
public:
    vector<int> constructArray(int n, int k) {
        vector<int> res;
        int l = 1, r = n;
        while (l <= r) {
            if (k > 1) {
                if (k % 2 == 1) {
                    res.push_back(l++);
                } else {
                    res.push_back(r--);
                }
                k --;
            } else {
                res.push_back(l++);
            }
        }
        return res;
    }
};
```

## 日期

2018 年 3 月 4 日 
2018 年 12 月 15 日 —— 今天四六级
