# 【LeetCode】779. K-th Symbol in Grammar 解题报告（Python）

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/k-th-symbol-in-grammar/description/

## 题目描述：

On the first row, we write a ``0``. Now in every subsequent row, we look at the previous row and replace each occurrence of ``0`` with ``01``, and each occurrence of ``1`` with ``10``.

Given row ``N`` and index ``K``, return the ``K``-th indexed symbol in row ``N``. (The values of ``K`` are 1-indexed.) (1 indexed).

    Examples:
    Input: N = 1, K = 1
    Output: 0
    
    Input: N = 2, K = 1
    Output: 0
    
    Input: N = 2, K = 2
    Output: 1
    
    Input: N = 4, K = 5
    Output: 1
    
    Explanation:
    row 1: 0
    row 2: 01
    row 3: 0110
    row 4: 01101001

Note:

1. N will be an integer in the range [1, 30].
1. K will be an integer in the range [1, 2^(N-1)].


## 题目大意

第一行有个0，以后的每一行是把上一行的0替换成01，把上一行的1替换成10。求第N行的第K个数是什么。注意K是按照1开始数的。

## 解题方法

恩，数据空间这么大，一看就是找规律的题目，没想到这么简单就过了。

把题目样例再多写一行：

    row 1: 0
    row 2: 01
    row 3: 0110
    row 4: 01101001
    row 5: 0110100110010110

基本可以看出规律了：每一行前面一半是和上一行完全一样的，后一半是和上一行完全相反的。

所以，求解的方法就是计算第K个数是在第N行的前面一半还是后面一半，计算方式是K和2^(N - 2)比较，即``K <= (1 << (N - 2))``。如果在前半部分，那么在上一行中寻找第K个数；如果在后半部分，那么在上一行中寻找第K - (1 << (N - 2))个数。

用递归实现的终止条件是当K == 1，或者N == 1，返回0.

时间复杂度是O(N)，空间复杂度是O(1)的变量空间，O(N)的栈空间.

代码如下：

```python
class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if K == 1:
            return 0
        if K <= (1 << (N - 2)):
            return self.kthGrammar(N - 1, K)
        else:
            return 1 - self.kthGrammar(N - 1, K - (1 << (N - 2)))
```

参考资料：


## 日期

2018 年 9 月 26 日 —— 美好的一周又快要过去了。。
