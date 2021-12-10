- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/check-if-all-1s-are-at-least-length-k-places-away/


# 题目描述

给你一个整数数组 `nums` ，和一个表示限制的整数 `limit`，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 `limit` 。

如果不存在满足条件的子数组，则返回 `0` 。
 

示例 1：

    输入：nums = [8,2,4,7], limit = 4
    输出：2 
    解释：所有子数组如下：
    [8] 最大绝对差 |8-8| = 0 <= 4.
    [8,2] 最大绝对差 |8-2| = 6 > 4. 
    [8,2,4] 最大绝对差 |8-2| = 6 > 4.
    [8,2,4,7] 最大绝对差 |8-2| = 6 > 4.
    [2] 最大绝对差 |2-2| = 0 <= 4.
    [2,4] 最大绝对差 |2-4| = 2 <= 4.
    [2,4,7] 最大绝对差 |2-7| = 5 > 4.
    [4] 最大绝对差 |4-4| = 0 <= 4.
    [4,7] 最大绝对差 |4-7| = 3 <= 4.
    [7] 最大绝对差 |7-7| = 0 <= 4. 
    因此，满足题意的最长子数组的长度为 2 。

示例 2：

    输入：nums = [10,1,2,4,7,2], limit = 5
    输出：4 
    解释：满足题意的最长子数组是 [2,4,7,2]，其最大绝对差 |2-7| = 5 <= 5 。

示例 3：

    输入：nums = [4,2,2,2,4,4,2,2], limit = 0
    输出：3
 

提示：

1. `1 <= nums.length <= 10^5`
1. `1 <= nums[i] <= 10^9`
1. `0 <= limit <= 10^9`



# 题目大意

找出一个最长的连续子数组，这个子数组中的最大值和最小值的差 <= limit。

# 解题方法

## 滑动窗口

看了数据的范围是 `10 ^ 5`，我们就知道要用 `O(N)` 的解法，又解决的是连续数组的最大最小问题，因此最终想到滑动窗口。

滑动窗口使用两个指针：left, right，我定义的是闭区间，即判断 `[left, right]`区间。

窗口维护思路是：

1. 找这个区间的最大值和最小值的差 `cur = max_ - min_`；
2. 如果 cur 大于 limit，说明当前窗口已经不满足条件，必须将 left 右移；
3. 如果 cur 小于 limit，说明满足条件，把 right 右移，尝试更大的窗口是否满足条件。

使用 res 保存最大窗口的大小，当 cur < limit 时，更新res.

整体的思路到上面就结束了。但是直接提交超时，为什么呢？因为 计算 max_ 和 min_ 直接调用库函数 max() 和 min()，这两者的时间复杂度是 O(N) 的，导致超时。

优化的重点是快速地求数组区间 max() 和 min()，即滑动窗口的最大值和最小值。可以用的方法有：
1. C++ 使用 multiset，可以允许出现重复元素。并且自动排序。
2. C++ 使用 map，保存出现次数，可自动排序。当一个数字的次数为0的时候，要erase掉。
3. 使用二分维护一个排序数组。
4. 使用两个优先级队列找最大和最小。

我用了一个简单的方法，判断区间内数字是不是都是相同的数字，如果都相同，那么不计算 max_ - min_ 了直接设置为0。就这样简单的方法就成功通过了。

Python 代码如下：

```python
class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        N = len(nums)
        left, right = 0, 0
        res = 0
        visited = set()
        visited.add(nums[0])
        while right < N:
            if (len(visited) != 1):
                max_ = max(nums[left : right + 1])
                min_ = min(nums[left : right + 1])
                cur = max_ - min_
            else:
                cur = 0
            if cur > limit:
                left += 1
            else:
                visited.add(nums[right])
                res = max(res, right - left + 1)
                right += 1
        return res
```

**欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**

# 日期

2020 年 5 月 3 日 —— 天气好热，瞬间入夏


  [1]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/03/sample_1_1791.png
  [2]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/03/sample_2_1791.png
