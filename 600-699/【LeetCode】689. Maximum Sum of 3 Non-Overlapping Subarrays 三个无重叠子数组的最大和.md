作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/description/

## 题目描述：

In a given array ``nums`` of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size ``k``, and we want to maximize the sum of all ``3*k`` entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

Example:

    Input: [1,2,1,2,6,7,5,1], 2
    Output: [0, 3, 5]
    Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
    We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.

Note:

1. nums.length will be between 1 and 20000.
1. nums[i] will be between 1 and 65535.
1. k will be between 1 and floor(nums.length / 3).


## 题目大意

把一个很长的数组，分成三个不重叠的子数组，要求每个子数组的长度都必须是k，最后的目的是三个子数组的和最大。

## 解题方法

看题目的数据知道需要用O(N)的解法，另外优化最值问题一般都是DP。具体怎么做呢？

把三个数组分别看做左侧，中间，右侧的数组。我们指定了中间数组的位置之后，就在这个位置左侧和右侧分别求一个和最大的子数组，然后三个数组和相加，就得到了总体最大的和。

使用sums数组保存到每个位置的累积和。这样做的好处是我们可以直接根据两个位置相减求出子数组的和。另外需要两个DP数组left和right。

> left[i]表示在区间[0, i]范围内长度为k且和最大的子数组的起始位置
> 
> right[i]表示在区间[i, n - 1]范围内长度为k且和最大的子数组的起始位置

left的求法是从左到右遍历，right的求法是从右到左遍历。遍历刚开始的K个位置内由于子数组长度小于k，所以left的值是0，right的值是N - k，代表的是能取子区间的边缘情况下索引。更新过程也不难，就是和已有的子数组最大和比较，然后更新索引位置就行了。

求出了每个位置左边和右边的长度为k的子数组之后，需要再次用一个窗口遍历数组，这个窗口就是我们中间的数组。这就成为了在确定中间数组位置的情况下，左边和右边的最大数组和问题，因为我们已经知道了left和right，那么就相当于查表得到位置。

这个题对sums是添加了头部0的，这样的好处是求到目前为止的和的时候可以直接从nums第0个数组开始找前面一个sums+当前的数字。

这个题最难的地方应该在于铺天盖地的索引值吧……反正我是被搞晕了。

时间复杂度是O(N)，空间复杂度是O(N)。

```python
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        N = len(nums)
        sums = [0]
        left = [0] * N
        right = [N - k] * N
        mx = 0
        res = [0, 0, 0]
        for i, num in enumerate(nums):
            sums.append(sums[-1] + num)
        total = sums[k] - sums[0]
        for i in range(k, N):
            if sums[i + 1] - sums[i - k + 1] > total:
                left[i] = i - k + 1
                total = sums[i + 1] - sums[i - k + 1]
            else:
                left[i] = left[i - 1]
        total = sums[N] - sums[N - k]
        for j in range(N - k - 1, -1, -1):
            if sums[j + k] - sums[j] >= total:
                right[j] = j
                total = sums[j + k] - sums[j]
            else:
                right[j] = right[j + 1]
        for i in range(k, N - 2 * k + 1):
            l, r = left[i - 1], right[i + k]
            total = (sums[i + k] - sums[i]) + (sums[l + k] - sums[l]) + (sums[r + k] - sums[r])
            if total > mx:
                mx = max(mx, total)
                res = [l, i, r]
        return res
```

参考资料：

https://www.cnblogs.com/grandyang/p/8453386.html

## 日期

2018 年 10 月 5 日 —— 转眼假期要结束了！！
