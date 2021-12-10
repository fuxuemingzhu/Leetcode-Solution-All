# 【LeetCode】334. Increasing Triplet Subsequence 解题报告（Python）

标签（空格分隔）： LeetCode

---

题目地址：https://leetcode.com/problems/increasing-triplet-subsequence/description/

## 题目描述：

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

> Return true if there exists i, j, k  such that arr[i] < arr[j] < arr[k] 
> given 0 ≤ i < j < k ≤ n-1 else return false.

Your algorithm should run in O(n) time complexity and O(1) space complexity.

    Examples:
    Given [1, 2, 3, 4, 5],
    return true.
    
    Given [5, 4, 3, 2, 1],
    return false.

## 题目大意

判断一个无序的数组中是否包含长度为3的递增的序列。

## 解题方法

用LIS的解法一定能做出来的，但是不符合题目给出的O(n)的时间复杂度。看了别人的解法发现真的很巧妙。我们完全可以抛弃什么DP啊，dfs啊，老夫写代码就是一把梭，抓起键盘就是干！

既然要求我们从前到后遍历，那么在遍历的时候保存已经看到的最小值和次小值，然后再发现比这两个值大的的第3小的值存在的时候，那么就说明有长度为3的递增的子序列了。

当然，对于这种情况：

    4  5  1  2  6

长度为3递增子序列有两种，但是由于我们保存的是最小的优先，所以最后的结果求得的是1  2  6这组。

整体的思想其实是很灵活的，保存的是遍历时**见到的**最小和次小，因此千万不要使用一成不变的min和max函数。

代码：

```python
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first, second = float('inf'), float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
```

## 日期

2018 年 4 月 5 日 ———— 清明节假期开始，小长假真好～～


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79821305