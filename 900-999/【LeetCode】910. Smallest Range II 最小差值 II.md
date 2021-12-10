
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/smallest-range-ii/description/


## 题目描述

Given an array ``A`` of integers, for each integer ``A[i]`` we need to choose either ``x = -K`` or ``x = K``, and add ``x`` to ``A[i] (only once)``.

After this process, we have some array ``B``.

Return the smallest possible difference between the maximum value of ``B`` and the minimum value of ``B``.

 
Example 1:

    Input: A = [1], K = 0
    Output: 0
    Explanation: B = [1]

Example 2:

    Input: A = [0,10], K = 2
    Output: 6
    Explanation: B = [2,8]

Example 3:

    Input: A = [1,3,6], K = 3
    Output: 3
    Explanation: B = [4,6,3]
 
Note:

1. 1 <= A.length <= 10000
1. 0 <= A[i] <= 10000
1. 0 <= K <= 10000

## 题目大意

可以把一个数组的每个数字加上K或者减去K，求每个位置都做了这个操作之后，最后的数组的最大值和最小值的差的最小值。


## 解题方法

把一个数组的每个数字加上K或者减去K然后求最大值最小值的差，等价于，把一个数组的每个数字加上2×K或者不变然后求最大值最小值的差。

我们先把数组进行排序，然后把每一个位置都做加上2×k的操作，同时保存每个位置进行操作后，整个数组的最大值和最小值。容易得出：

最大值是A[i] + 2 * K和A[-1]之一；
最小值是A[i + 1]和A[0] + 2 * K之一；


所以遍历一遍，我们就得出了最后的结果。


Python代码如下：

```python
class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        N = len(A)
        mn, mx = A[0], A[-1]
        res = mx - mn
        for i in range(N - 1):
            mx = max(A[i] + 2 * K, mx)
            mn = min(A[i + 1], A[0] + 2 * K)
            res = min(mx - mn, res)
        return res
```

C++代码如下：

```cpp
class Solution {
public:
    int smallestRangeII(vector<int>& A, int K) {
        sort(A.begin(), A.end());
        const int N = A.size();
        int mn = A[0], mx = A[N - 1];
        int res = mx - mn;
        for (int i = 0; i < N - 1; i ++) {
            mx = max(mx, A[i] + 2 * K);
            mn = min(A[i + 1], A[0] + 2 * K);
            res = min(res, mx - mn);
        }
        return res;
    }
};
```


## 日期

2018 年 12 月 14 日 —— 12月过半，2019就要开始


  [1]: https://zxi.mytechroad.com/blog/wp-content/uploads/2018/06/856-ep198.png
  [2]: https://zxi.mytechroad.com/blog/wp-content/uploads/2018/06/856-ep198-2.png
