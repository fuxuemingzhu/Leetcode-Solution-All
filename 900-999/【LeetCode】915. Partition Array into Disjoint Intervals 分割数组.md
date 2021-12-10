作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/partition-array-into-disjoint-intervals/description/

## 题目描述：

Given an array A, partition it into two (contiguous) subarrays left and right so that:

1. Every element in left is less than or equal to every element in right.
1. left and right are non-empty.
1. left has the smallest possible size.

Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.

 

Example 1:

    Input: [5,0,3,8,6]
    Output: 3
    Explanation: left = [5,0,3], right = [8,6]

Example 2:

    Input: [1,1,1,0,6,12]
    Output: 4
    Explanation: left = [1,1,1,0], right = [6,12]
 

Note:

1. 2 <= A.length <= 30000
1. 0 <= A[i] <= 10^6
1. It is guaranteed there is at least one way to partition A as described.


## 题目大意

找出数组的一个分界点长度，使得这个分界点左边的元素都小于分界点右边的元素。

## 解题方法

有的题目就是那么烧脑，我现在还是不太能想通没见过的题目。这个题的范围超级大，所以只能用O(N)的算法。

这个题的做法是，我们记录当前已经遍历到的元素最大值和这个元素前面的最大值，如果当前元素比前面已经遇到的最大值更小，说明这个元素一定在左边的划分中（否则前面的最大值会大于这个值），我们的划分要更新到这个元素。

这个做法应该还是挺直观的，理解两个值：当前元素前面的最大值（不包括当前值），到目前元素为止所有值的最大值（包括当前值）。

最坏情况下的时间复杂度是O(N)，空间复杂度是O(1)。

```python
class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        disjoint = 0
        v = A[0]
        max_so_far = v
        for i in range(len(A)):
            max_so_far = max(max_so_far, A[i])
            if A[i] < v:
                v = max_so_far
                disjoint = i
        return disjoint + 1
```

参考资料：

https://leetcode.com/problems/partition-array-into-disjoint-intervals/discuss/175904/Explained-Python-simple-O(N)-time-O(1)-space

## 日期

2018 年 9 月 30 日 —— 9月最后一天啦！
