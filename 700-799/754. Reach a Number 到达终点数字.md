作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/reach-a-number/description/


## 题目描述

You are standing at position ``0`` on an infinite number line. There is a goal at position ``target``.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:

    Input: target = 3
    Output: 2
    Explanation:
    On the first move we step from 0 to 1.
    On the second step we step from 1 to 3.

Example 2:

    Input: target = 2
    Output: 3
    Explanation:
    On the first move we step from 0 to 1.
    On the second move we step  from 1 to -1.
    On the third move we step from -1 to 2.

Note:

- target will be a non-zero integer in the range [-10^9, 10^9].
 

## 题目大意

每次走的步数是增加1步，方向是可以向左或者向右，求通过多少步之后能到达target。


## 解题方法

### 数学

非常不喜欢数学题，所以花花酱和Grandyang大神的帖子粘在这里了。

花花酱：https://zxi.mytechroad.com/blog/math/leetcode-754-reach-a-number/
Grandyang大神：http://www.cnblogs.com/grandyang/p/8456022.html

```python
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        k = 0
        sum = 0
        while sum < target:
            k += 1
            sum += k
        d = sum - target
        if d % 2 == 0:
            return k
        return k + 1 + (k % 2)
```

C++版本如下：

```cpp
class Solution {
public:
    int reachNumber(int target) {
        target = abs(target);
        int k = 0;
        int sum = 0;
        while (sum < target) {
            sum += (++k);
        }
        const int d = sum - target;
        if (d % 2 == 0) return k;
        return k + 1 + (k % 2);
    }
};
```

## 日期

2018 年 11 月 26 日 —— 11月最后一周！


  [1]: http://zxi.mytechroad.com/blog/dynamic-programming/leetcode-730-count-different-palindromic-subsequences/
