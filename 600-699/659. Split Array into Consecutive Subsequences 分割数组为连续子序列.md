# 【LeetCode】659. Split Array into Consecutive Subsequences 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/split-array-into-consecutive-subsequences/description/

## 题目描述：

You are given an integer array sorted in ascending order (may contain duplicates), you need to split them into several subsequences, where each subsequences consist of at least 3 consecutive integers. Return whether you can make such a split.

Example 1:

    Input: [1,2,3,3,4,5]
    Output: True
    Explanation:
    You can split them into two consecutive subsequences : 
    1, 2, 3
    3, 4, 5

Example 2:

    Input: [1,2,3,3,4,4,5,5]
    Output: True
    Explanation:
    You can split them into two consecutive subsequences : 
    1, 2, 3, 4, 5
    3, 4, 5

Example 3:

    Input: [1,2,3,4,4,5]
    Output: False

Note:

- The length of the input is in range of [1, 10000]


## 题目大意

把一个升序的数组，分割成几个连续的递增的整数序列。如果能分割，且分割后的每个序列的长度都至少为3，那么认为成功，否则失败。

## 解题方法

这就是所谓的扑克牌算法，必须全部弄成“顺子”。一个“顺子”至少3张连续的牌。方法是使用优先级队列，优先把当前的牌放入到更短的“顺子”里（贪心）。

> 这个题的思想就是贪心+优先级队列

首先判断以（num-1）为结尾的序列是否存在，

如果存在，获取长度最小值len并出栈，创建以num为结尾的数组，并设置长度为len + 1，推入优先队列；

如果不存在，创建新的序列，以num为结尾，并且长度为1，推入优先队列，创建新的键值对（num，currentPriorityQueue）推入map中。

1，2，3，3，4，4，5，5


    num	last	        len	    current	        map
    1	null->(0,[ ])	0	    (1, [1])	(0,[ ] ) (1, [1])
    2	(1, [1])	    1	    (2, [2])	(0,[ ] ) (1, [ ])(2, [2])
    3	(2, [2])	    2	    (3, [3])	(0,[ ] ) (1, [ ])(2, [ ])(3, [3])
    3	(2, [ ])	    0	    (3, [1])	(0,[ ] ) (1, [ ])(2, [ ])(3, [3])(3, [1])
    4	(3, [1])	    1	    (4, [2])	(0,[ ] ) (1, [ ])(2, [ ])(3, [3])(3, [ ])(4, [2])
    4	(3, [3])	    3	    (4, [4])	(0,[ ] ) (1, [ ])(2, [ ])(3, [ ])(3, [ ])(4, [2])(4, [4])
    5	(4, [2])	    2	    (5, [3])	(0,[ ] ) (1, [ ])(2, [ ])(3, [ ])(3, [ ])(4, [ ])(4, [4])(5, [3])
    5	(4, [4])	    4	    (5, [5])	(0,[ ] ) (1, [ ])(2, [ ])(3, [ ])(3, [ ])(4, [ ])(4, [ ])(5, [3])(5, [5])


代码如下：

```python
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        saved = collections.defaultdict(list)
        for num in nums:
            last = saved[num - 1]
            _len = 0 if (not last) else heapq.heappop(last)
            current = saved[num]
            heapq.heappush(current, _len + 1)
        for values in saved.values():
            for v in values:
                if v < 3:
                    return False
        return True

```

参考资料：

1. https://blog.csdn.net/sunday0904/article/details/78174122

## 日期

2018 年 8 月 29 日 ———— 还是要早起才行啊！
