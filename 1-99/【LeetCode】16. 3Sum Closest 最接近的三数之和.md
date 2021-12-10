
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)
- 个人公众号：负雪明烛
- 本文关键词：3sum, three sum, 三数之和，题解，leetcode, 力扣，Python, C++, Java

---

题目地址: https://leetcode.com/problems/3sum-closest/description/

## 题目描述：

Given an array ``nums`` of n integers and an integer ``target``, find three integers in ``nums`` such that the sum is closest to ``target``. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:
    
    Given array nums = [-1, 2, 1, -4], and target = 1.
    
    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

## 题目大意

在给定的数组中判断是否存在三个数的和是0，返回所有的组合，但是返回的组合中不能有重复。

## 解题方法

### 方法：原数组排序+双指针

这个题和[15. 3Sum][1]基本一样，而且这个题更简单一点。

想要得到三个数字的和，要求这个和尽可能的靠近target，那么同样需要先排序，然后使用一个指针遍历，另外两个指针分别指向下一个元素和最后一个元素然后向中间靠拢的方式。在靠拢的过程中如果当前的和与target的差距比要返回的结果与target更小，那么更新要返回的结果。

指针的移动策略是如果和比目标值大，说明我们需要把这个和调小一点；如果和比目标小，那么需要把和调大一点。如果相等那么就返回结果。

时间复杂度是O(N^2)，空间复杂度是O(1)。

```python
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = len(nums)
        nums.sort()
        res = float('inf') # sum of 3 number
        for t in range(N):
            i, j = t + 1, N - 1
            while i < j:
                _sum = nums[t] + nums[i] + nums[j]
                if abs(_sum - target) < abs(res - target):
                    res = _sum
                if _sum > target:
                    j -= 1
                elif _sum < target:
                    i += 1
                else:
                    return target
        return res
```



参考资料：


## 日期

2018 年 10 月 17 日 —— 今又重阳，战地黄花分外香


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/83115850
