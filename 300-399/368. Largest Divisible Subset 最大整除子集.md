作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/largest-divisible-subset/description/

## 题目描述：

Given a set of distinct positive integers, find the largest subset such that every pair ``(Si, Sj)`` of elements in this subset satisfies:

``Si % Sj = 0 or Sj % Si = 0``.

If there are multiple solutions, return any subset is fine.

Example 1:

    Input: [1,2,3]
    Output: [1,2] (of course, [1,3] will also be ok)
    Example 2:
    
    Input: [1,2,4,8]
    Output: [1,2,4,8]


## 题目大意


找出一个数组中最长的可以互相整除的集合。互相整除的含义是，在数组中随便抽出两个数字，其中一个是另一个的约数。

## 解题方法

是否想起了Longest Increase Sequence？这两个题非常相似啊，所以做题一定要把融会贯通才行。

首先需要对题目给出的数组进行排序，这样的作用是我们从左到右遍历一次，每次只看后面的数字能不能被前面的整除就行。

问题分成了两个部分：

1. 寻找最长的满足题目的数组
2. 输出整个结果

使用一个一维DP，其含义是题目要求的数组，DP[i]的含义是，从0~i位置满足题目的最长数组。先用i遍历每个数字，然后用j从后向前寻找能被nums[i]整除的数字，这样如果判断能整除的时候，再判断dp[i] < dp[j] + 1，即对于以i索引结尾的最长的数组是否变长了。在变长的情况下，需要更新dp[i]，同时使用parent[i]更新i的前面能整除的数字。另外还要统计对于整个数组最长的子数组长度。

知道了对于每个位置最长的子数组之后，我们也就知道了对于0~n区间内最长的满足题目条件的数组，最后需要再次遍历，使用parent就能把正儿个数组统计输出出来。因为这个最大的索引mx_index是对n而言的，所以输出是逆序的。

总感觉语言是乏力的，明白LIS对这个题有好处。

注意

    注意这个case：
    [1,2,4,8,9,72]
    到72的时候，往前找到9，可以整除，更新dp[5]为max(1, 2 + 1) = 3,
    注意此时应该继续往前找，不能停，直到找到8,发现dp[3] + 1 = 5 > 3，于是更新dp[i]
    注意就是不能停，找到一个能整除并不够，前面有可能有更大的啊~~

时间复杂度是O(N^2)，空间复杂度是O(N). 

代码如下：

```python
class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        N = len(nums)
        nums.sort()
        dp = [0] * N #LDS
        parent = [0] * N
        mx = 0
        mx_index = -1
        for i in range(N):
            for j in range(i - 1, -1 , -1):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
                    if dp[i] > mx:
                        mx = dp[i]
                        mx_index = i
        res = list()
        for k in range(mx + 1):
            res.append(nums[mx_index])
            mx_index = parent[mx_index]
        return res[::-1]
```

参考资料：

https://segmentfault.com/a/1190000005922634
http://www.cnblogs.com/grandyang/p/5625209.html

## 日期

2018 年 10 月 12 日 —— 又要到周末了！


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/51291936
