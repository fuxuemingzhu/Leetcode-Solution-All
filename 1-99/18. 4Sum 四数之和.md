
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)
- 个人公众号：负雪明烛
- 本文关键词：four sum,  4sum, 四数之和，题解，leetcode, 力扣，Python, C++, Java

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/4sum/description/


## 题目描述

Given an array ``nums`` of n integers and an integer ``target``, are there elements a, b, c, and d in ``nums`` such that ``a + b + c + d = target``? Find all unique quadruplets in the array which gives the sum of ``target``.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:

    [
      [-1,  0, 0, 1],
      [-2, -1, 1, 2],
      [-2,  0, 0, 2]
    ]


## 题目大意

找出一个数组中所有的和为target的四个数字，要求返回的结果里面不准有重复的四元组。

## 解题方法

### 遍历

总结一下 K-sum 题目。

1. 首先先排序
2. 然后用 $K - 2$ 个指针做 `O(N^(K - 2))` 的遍历
3. 剩下 2 个指针从第 2 步的剩余区间里面找，找的方式是使用两个指针 p, q 分别指向剩余区间的首尾，判断两个指针的和与 target - 第2步的和的关系，对应的移动指针。即如果两个数的和大了，那么, q--；如果两个数的和小了，那么，p++；等于的话，输出结果。要时刻注意 p < q.
4. 用 p,q 查找剩余区间结束之后，需要移动前面的K-2个值，这里需要在移动的过程中做个去重，找到和前面不同的值继续查找剩余区间。

时间复杂度是O(N^3)，空间复杂度是O(1).

```python
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        N = len(nums)
        nums.sort()
        res = []
        i = 0
        while i < N - 3:
            j = i + 1
            while j < N - 2:
                k = j + 1
                l = N - 1
                remain = target - nums[i] - nums[j]
                while k < l:
                    if nums[k] + nums[l] > remain:
                        l -= 1
                    elif nums[k] + nums[l] < remain:
                        k += 1
                    else:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        while k < l and nums[k] == nums[k + 1]:
                            k += 1
                        while k < l and nums[l] == nums[l - 1]:
                            l -= 1
                        k += 1
                        l -= 1
                while j < N - 2 and nums[j] == nums[j + 1]:
                    j += 1
                j += 1 # 重要
            while i < N - 3 and nums[i] == nums[i + 1]:
                i += 1
            i += 1 # 重要
        return res
```


## 相似题目

[Two Sum][1]
[Two Sum II - Input array is sorted][2]
[15. 3Sum][3]
[16. 3Sum Closest][4]
[923. 3Sum With Multiplicity][5]
[454. 4Sum II][6]

## 参考资料

https://blog.csdn.net/MebiuW/article/details/50938326

## 日期

2018 年 10 月 30 日 —— 啊，十月过完了


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/72465759
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/70232518
  [3]: https://blog.csdn.net/fuxuemingzhu/article/details/83115850
  [4]: https://blog.csdn.net/fuxuemingzhu/article/details/83116781
  [5]: https://blog.csdn.net/fuxuemingzhu/article/details/83045983
  [6]: https://blog.csdn.net/fuxuemingzhu/article/details/79473739
