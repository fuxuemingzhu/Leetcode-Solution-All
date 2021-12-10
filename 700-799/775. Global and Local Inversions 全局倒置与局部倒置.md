作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/global-and-local-inversions/description/

## 题目描述：

We have some permutation A of ``[0, 1, ..., N - 1]``, where N is the length of A.

The number of (global) inversions is the number of ``i < j`` with ``0 <= i < j < N`` and ``A[i] > A[j]``.

The number of local inversions is the number of i with ``0 <= i < N`` and ``A[i] > A[i+1]``.

Return true if and only if the number of global inversions is equal to the number of local inversions.

Example 1:

    Input: A = [1,0,2]
    Output: true
    Explanation: There is 1 global inversion, and 1 local inversion.

Example 2:

    Input: A = [1,2,0]
    Output: false
    Explanation: There are 2 global inversions, and 1 local inversion.

Note:

1. A will be a permutation of [0, 1, ..., A.length - 1].
1. A will have length in range [1, 5000].
1. The time limit for this problem has been reduced.


## 题目大意

如果存在``i < j`` with ``0 <= i < j < N`` and ``A[i] > A[j]``，称之为一个全局翻转。
如果存在``0 <= i < N`` and ``A[i] > A[i+1]``，称之为一个局部翻转。
判断一个由0～N - 1组成的一个乱序数组中，全局翻转的个数与局部翻转的个数是否相等。

## 解题方法

首先当j = i + 1时，可以看出，一个局部翻转就是一个全局翻转。那么如果要使得局部翻转和全局翻转的个数相等，那么必须要求全局翻转也是一个局部翻转。所以，对于任意的j > i + 1，不能存在A[i] > A[j]，即需要满足A[i] <= A[j].

从上面的关系可以看出，我们必须使max(A[:i]) <= A[i + 2]。

最坏情况下的时间复杂度是O(N)，空间复杂度是O(1)。

```python
class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        cmax = 0
        for i in range(len(A) - 2):
            cmax = max(cmax, A[i])
            if cmax > A[i + 2]:
                return False
        return True
```

上面的想法并没有好好的利用题目给出的数字是0~N-1这个条件。所以我们继续思考，如果原来的顺序是0~N-1，那么如何交换两个数字才能满足局部翻转的个数等于全局翻转呢？答案当然是只翻转相邻的两个元素。否则会构造出来一个不是局部翻转的全剧翻转。所以i的位置上只能放A[i-1],A[i],A[i+1]。

```python
class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        for i, a in enumerate(A):
            if abs(a - i) > 1:
                return False
        return True
```


参考资料：

https://leetcode.com/problems/global-and-local-inversions/discuss/113644/Easy-and-Concise-Solution-C++JavaPython

## 日期

2018 年 10 月 1 日 —— 欢度国庆！
