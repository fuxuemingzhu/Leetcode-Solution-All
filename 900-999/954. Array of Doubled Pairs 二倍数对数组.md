
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/array-of-doubled-pairs/description/


## 题目描述

Given an array of integers ``A`` with even length, return ``true`` if and only if it is possible to reorder it such that ``A[2 * i + 1] = 2 * A[2 * i]`` for every ``0 <= i < len(A) / 2``.

 

Example 1:

    Input: [3,1,3,6]
    Output: false

Example 2:

    Input: [2,1,2,6]
    Output: false

Example 3:

    Input: [4,-2,2,-4]
    Output: true
    Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].

Example 4:

    Input: [1,2,4,16,8,4]
    Output: false
 

Note:

1. 0 <= A.length <= 30000
1. A.length is even
1. -100000 <= A[i] <= 100000


## 题目大意

问能不能重新对数组进行某种排列，使得``A[2 * i + 1] = 2 * A[2 * i]``对于``0 <= i < len(A) / 2``恒成立。

## 解题方法

题目的意思是奇数位置的数字能不能安排成它左边的那个位置的二倍。

使用的方法是统计次数、然后遍历查找的方式，和Two Sum之类的很类似。需要注意的是，我们对数组进行了排序，这样保证下面的遍历是从小到大开始的。另外，由于排序之后，对于负数而言，小数字是大数字的2倍，所以，需要做一个正负的判断。

对于负数来说，我们找出它的1/2是不是在数组中；对于正数来说，我们找出它的2倍是不是在数组中。如果找到了要找的数字之后，把它的次数减去当前的数字的次数，以方便后面的统计。所以，如果所有的数字都满足条件的话，那么就一波一波的都消除掉了。

```python
class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        A.sort()
        N = len(A)
        count = collections.Counter(A)
        for i in range(N):
            if A[i] == 0 or A[i] not in count: continue
            elif A[i] < 0:
                if A[i] % 2 == 1 or count[A[i] / 2] == 0:
                    return False
                else:
                    count[A[i] / 2] -= count[A[i]]
                    if count[A[i] / 2] == 0:
                        del count[A[i] / 2]
                    del count[A[i]]
            else:
                if count[A[i] * 2] == 0:
                    return False
                else:
                    count[A[i] * 2] -= count[A[i]]
                    if count[A[i] * 2] == 0:
                        del count[A[i] * 2]
                    del count[A[i]]
        return True
```



## 日期

2018 年 12 月 9 日 —— 周赛懵逼了



  [1]: https://leetcode.com/static/images/courses/range_sum_query_2d.png
  [2]: https://leetcode.com/static/images/courses/sum_od.png
  [3]: https://leetcode.com/static/images/courses/sum_ob.png
  [4]: https://leetcode.com/static/images/courses/sum_oc.png
  [5]: https://leetcode.com/static/images/courses/sum_oa.png
  [6]: https://blog.csdn.net/fuxuemingzhu/article/details/79253036
