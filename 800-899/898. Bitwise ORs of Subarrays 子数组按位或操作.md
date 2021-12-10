
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/bitwise-ors-of-subarrays/description/


## 题目描述

We have an array ``A`` of non-negative integers.

For every (contiguous) subarray ``B = [A[i], A[i+1], ..., A[j]]`` (with ``i <= j``), we take the bitwise OR of all the elements in ``B``, obtaining a result ``A[i] | A[i+1] | ... | A[j]``.

Return the number of possible results.  (Results that occur more than once are only counted once in the final answer.)

 

Example 1:

    Input: [0]
    Output: 1
    Explanation: 
    There is only one possible result: 0.

Example 2:

    Input: [1,1,2]
    Output: 3
    Explanation: 
    The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
    These yield the results 1, 1, 2, 1, 3, 3.
    There are 3 unique values, so the answer is 3.

Example 3:

    Input: [1,2,4]
    Output: 6
    Explanation: 
    The possible results are 1, 2, 3, 4, 6, and 7.
 

Note:

1. ``1 <= A.length <= 50000``
1. ``0 <= A[i] <= 10^9``


## 题目大意

一个数组的所有子数组的异或结果，总共有多少个不同？


## 解题方法

### 动态规划

题目不是一般的难啊，如果是普通的DP方法，那么使用二维dp[i][j]表示子数组的起始和结束区间，能做到O(n^2)的时间复杂度，但是题目对时间复杂度要求的很死，必须O(N).

正确的做法也是动态规划，dp[i]表示以A[i]结尾的所有子数组的异或结果，其实是个set。

转移方程式``dp[i] = [b | A[i] for b in dp[i - 1]] + A[i]``，即以A[i]结尾的所有子数组异或结果等于以A[i-1]结尾的所有子数组异或结果，和当前的A[i]异或，再加上A[i]这个结果。

同时使用一个set保存所有的异或结果。最后返回这个结果set的长度。

![此处输入图片的描述][1]

dp[i]的大小至多是32个，即 |dp[i]| <= 32 的证明：

dp[i] = {A[i], A[i] | A[i - 1], A[i] | A[i - 1] | A[i - 2], ... , A[i] | A[i - 1] | ... | A[0]}，这个序列单调递增，通过把A[i]中的0变成1。A[i]最多有32个0。所以这个集合的大小 <= 32。

举例：最坏情况 A = [8, 4, 2, 1, 0] 都是2^k。
A[5] = 0，dp[5] = {0, 0 | 1, 0 | 1 | 2, 0 | 1 | 2 | 4, 0 | 1 | 2 | 4 | 8} = {0, 1, 3, 7, 15}.


时间复杂度是O(32*N)，空间复杂度是O(32N).

```python
class Solution(object):
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = set()
        cur = set()
        for a in A:
            cur = {n | a for n in cur} | {a}
            res |= cur
        return len(res)
```


## 相似题目


## 参考资料

https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-898-bitwise-ors-of-subarrays/

## 日期

2018 年 10 月 28 日 —— 10月份最后一个周一


  [1]: https://zxi.mytechroad.com/blog/wp-content/uploads/2018/09/898-ep222.png
  [2]: https://blog.csdn.net/happyaaaaaaaaaaa/article/details/51636861
