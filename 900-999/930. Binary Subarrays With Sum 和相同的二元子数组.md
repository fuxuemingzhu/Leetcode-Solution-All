作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/binary-subarrays-with-sum/description/

## 题目描述

In an array ``A`` of ``0``s and ``1``s, how many **non-empty** subarrays have sum **S**?

 

Example 1:

    Input: A = [1,0,1,0,1], S = 2
    Output: 4
    Explanation: 
    The 4 subarrays are bolded below:
    [1,0,1,0,1]
    [1,0,1,0,1]
    [1,0,1,0,1]
    [1,0,1,0,1]
 

Note:

1. A.length <= 30000
1. 0 <= S <= A.length
1. A[i] is either 0 or 1.


## 题目大意

求有多少个子区间的和是S.

## 解题方法

悲剧啊！周赛第二个题都没做出来。我的想法是双指针，用虫取法的方式去做，但是发现了，当一个区间的前面或者后面都有0的时候，这时候移动前后指针都能达到下一个状态的和也是S。然后我就在上面吊死了。真正的做法如下。

### 二分查找

这个题考的不是虫取法，题目为什么只给了0和1呢？因为我们每次遇到一个1，整体的和只会增加1，求和的时候不会出现负数，所以如果从左到右求和的过程中是个递增的。

下面的做法有点类似Two sum，最开始先使用一个求和数组保存求和的过程，然后对求和数组tsum做一个遍历，遍历的过程中过程中，使用tsum[i] - S，这个结果remain就是我们要找的前面的部分和。也就是说remain出现的次数就是以i结尾的子数组满足题意的个数。

所以，下面的工作是找到这个remain在tsum中出现了多少次。使用二分查找的lowwer_bound和upper_bound就可以了。需要注意的是有个测试用例全部是0，这个情况下，如果upper_bound就直接找到最右边界了，所以我们得限制一下，upper_bound的索引不能超过当前的i.

时间复杂度是O(NlogN)，空间复杂度是O(N)。

```python
class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        N = len(A)
        tsum = [0] * (N + 1)
        for i in range(1, N + 1):
            tsum[i] = tsum[i - 1] + A[i - 1]
        res = 0
        for i in range(1, N + 1):
            remain = tsum[i] - S
            if remain < 0:
                continue
            left = bisect.bisect_left(tsum, remain)
            right = bisect.bisect_right(tsum, remain)
            right = min(i, right)
            res += right - left
        return res
```

### 字典

在上面的做法中，我们想到了要查找remain出现了多少次，那么我们肯定想起来了使用字典啊！如果用字典的话不能直接先求所有的累计和，然后统计每个和出现了多少次，因为那样的话对全0的输入又蒙了！所以我们需要知道截止到某个位置的时候，当前的和减去S**已经**出现了多少次。所以这个字典是保存每个和已经出现的次数的！

使用一个字典保存数组某个位置之前的数组和，然后遍历数组求和，这样当我们求到一个位置的和的时候，向前找sum-k是否在数组中，如果在的话，更新结果为之前的结果+1。同时，当前这个sum出现的次数就多了一次。

和[560. Subarray Sum Equals K][1]几乎一模一样的题目，为什么就是不会做呢？

```python
class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        N = len(A)
        res = 0
        preS = 0
        count = collections.Counter({0 : 1})
        for i in range(1, N + 1):
            preS += A[i - 1]
            res += count[preS - S]
            count[preS] += 1
        return res
```

## 相似题目

[560. Subarray Sum Equals K][1]

## 参考资料

https://leetcode.com/problems/binary-subarrays-with-sum/discuss/186683/C++JavaPython-Straight-Forward

## 日期

2018 年 10 月 28 日 —— 啊，悲伤的周赛


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/82767119
