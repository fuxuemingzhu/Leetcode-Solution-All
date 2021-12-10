# 【LeetCode】228. Summary Ranges 解题报告（Python）

标签（空格分隔）： LeetCode

---

题目地址：https://leetcode.com/problems/summary-ranges/description/

## 题目描述：

Given a sorted integer array without duplicates, return the summary of its ranges.

    Example 1:
    Input: [0,1,2,4,5,7]
    Output: ["0->2","4->5","7"]

    Example 2:

    Input: [0,2,3,4,6,8,9]
    Output: ["0","2->4","6","8->9"]
    
## 题目大意

把一个有序的数组，合并区间。也就是两个相邻的数字之间的距离如果是1，那么就应该合并。

## 解题方法

完全是自己想出来的算法哈哈哈。两个while嵌套，第一个嵌套遍历Nums，第二个嵌套要往后走，看看后面的数字是不是比前面的数字大1，是的话就一直后移。根据i和j是否重叠来判断是加上一个数字还是加上一个区间。

代码：

```python
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums: return []
        res = []
        i = 0
        while i < len(nums):
            j = i
            while j < len(nums) - 1 and nums[j] == nums[j + 1] - 1:
                j += 1
            if j == i:
                res.append(str(nums[i]))
            else:
                res.append('%s->%s' % (str(nums[i]), str(nums[j])))
            i = j + 1
        return res
```

## 日期

2018 年 3 月 31 日 ———— 晚上睡不好，一天没精神啊