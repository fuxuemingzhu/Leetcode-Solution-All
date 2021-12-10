作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/beautiful-array/description/


## 题目描述

For some fixed N, an array A is beautiful if it is a permutation of the integers 1, 2, ..., N, such that:

For every ``i < j``, there is no k with ``i < k < j`` such that ``A[k] * 2 = A[i] + A[j]``.

Given N, return any beautiful array A.  (It is guaranteed that one exists.)

 

Example 1:

    Input: 4
    Output: [2,1,4,3]

Example 2:
    
    Input: 5
    Output: [3,1,2,5,4]
 

Note:

1. 1 <= N <= 1000



## 题目大意

给出从1到N的数组的一个排列，使得任意两个数字之间不存在他们的平均数。


## 解题方法

### 构造法

因为题目要求任意两个数的平均数不能在他们中间，如果一个数字左边都是奇数，右边都是偶数，那么肯定这个数字的二倍是偶数，肯定不会存在``A[k] * 2 = A[i] + A[j]``。

若数组A满足上面的条件，那么很容易从线性关系中看出来，对于A中的每个元素做``[2 * i for i in A]``后者``[2 * i - 1 for i in A]``依然满足上面的条件。

所以我们从最简单的[1]开始推导，构造奇数+偶数拼接在一起成为新的数组，然后继续这个操作，就能使得得到的一直是满足条件的数组。最后当数组的长度满足条件就结束。因为结果数组的长度是2的整数次方，所以最后要把结果中小于等于N的留下来就行了。

时间复杂度是O(NlogN)，空间复杂度是O(N).打败100%。

```python
class Solution(object):
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        res = [1]
        while len(res) < N:
            res = [2 * i - 1 for i in res] + [2 * i  for i in res]
        return [i for i in res if i <= N]
```


### 递归

可以把上面的方法改成递归写法。思想是类似的，只不过要注意的是因为N可能是偶数也可能是奇数，当是奇数的时候除以二的时候可能丢失了一个奇数，所以小于N的奇数个数是``N / 2 + N % 2``.

时间复杂度是O(NlogN)，空间复杂度是O(NlogN).打败25%。

```python
class Solution(object):
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        if N == 1: return [1]
        odd = [i * 2 - 1 for i in self.beautifulArray(N / 2 + N % 2)]
        even = [i * 2 for i in self.beautifulArray(N / 2)]
        return odd + even
```

## 相似题目


## 参考资料

推荐寒神的视频：https://www.youtube.com/watch?v=9L6bPGDfyqo&t=41s

## 日期

2018 年 10 月 30 日 —— 啊，十月过完了


  [1]: https://leetcode.com/static/images/courses/range_sum_query_2d.png
  [2]: https://leetcode.com/static/images/courses/sum_od.png
  [3]: https://leetcode.com/static/images/courses/sum_ob.png
  [4]: https://leetcode.com/static/images/courses/sum_oc.png
  [5]: https://leetcode.com/static/images/courses/sum_oa.png
  [6]: https://blog.csdn.net/fuxuemingzhu/article/details/79253036
