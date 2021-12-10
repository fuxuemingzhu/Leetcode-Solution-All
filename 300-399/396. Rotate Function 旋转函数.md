作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/rotate-function/description/

## 题目描述：

Given an array of integers ``A`` and let n to be its length.

Assume ``Bk`` to be an array obtained by rotating the array ``A`` k positions clock-wise, we define a "rotation function" ``F`` on ``A`` as follow:

    F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].

Calculate the maximum value of ``F(0), F(1), ..., F(n-1)``.

Note:

- n is guaranteed to be less than 10^5.

Example:

    A = [4, 3, 2, 6]
    
    F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
    F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
    F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
    F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
    
    So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.



## 题目大意

给出了一个数组A，定义了一个旋转函数，``F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1]``，公式是对数组旋转的，也就是因子的开始位置会遍历到数组的每个位置。

## 解题方法

看了数据规模是10^5，可以知道时间复杂度是O(N)量级，这就难办了。看了Related Topics，知道这是个数学题。好吧，只能用数学的方法解决了，不能靠暴力。下面的内容来自Grandyang.

我们为了找规律，先把具体的数字抽象为A,B,C,D，那么我们可以得到：

    F(0) = 0A + 1B + 2C +3D
    
    F(1) = 0D + 1A + 2B +3C
    
    F(2) = 0C + 1D + 2A +3B
    
    F(3) = 0B + 1C + 2D +3A

那么，我们通过仔细观察，我们可以得出下面的规律：

    F(1) = F(0) + sum - 4D
    
    F(2) = F(1) + sum - 4C
    
    F(3) = F(2) + sum - 4B

那么我们就找到规律了, ``F(i) = F(i-1) + sum - n * A[n-i]``，是个递推公式。我们最后求的是这个所有F(i)中的最大值。

时间复杂度是O(N)，空间复杂度是O(1). 

代码如下：

```python
class Solution:
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        _sum = 0
        N = len(A)
        f = 0
        for i, a in enumerate(A):
            _sum += a
            f += i * a
        res = f
        for i in range(N - 1, 0, -1):
            f = f + _sum - N * A[i]
            res = max(res, f)
        return res
```

参考资料：

http://www.cnblogs.com/grandyang/p/5869791.html

## 日期

2018 年 10 月 10 日 ———— 冻成狗


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/51291936
