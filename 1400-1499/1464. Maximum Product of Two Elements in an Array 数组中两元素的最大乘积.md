

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/maximum-product-of-two-elements-in-an-array/


# 题目描述


给你一个整数数组 `nums`，请你选择数组的两个不同下标 `i` 和 `j`，使 `(nums[i]-1)*(nums[j]-1)` 取得最大值。

请你计算并返回该式的最大值。

示例 1：

    输入：nums = [3,4,5,2]
    输出：12 
    解释：如果选择下标 i=1 和 j=2（下标从 0 开始），则可以获得最大值，(nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12 。 

示例 2：

    输入：nums = [1,5,4,5]
    输出：16
    解释：选择下标 i=1 和 j=3（下标从 0 开始），则可以获得最大值 (5-1)*(5-1) = 16 。

示例 3：

    输入：nums = [3,7]
    输出：12

提示：

1. `2 <= nums.length <= 500`
1. `1 <= nums[i] <= 10^3`

# 题目大意

略。

# 解题方法

## 暴力

首先想到暴力解法，即两重循环，时间复杂度是 `O(N^2)`，题目给出的数组大小只有 500，因此满足要求。


Python 代码如下：

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = 0
        N = len(nums)
        for i in range(N):
            for j in range(i + 1, N):
                res = max(res, (nums[i] - 1) * (nums[j] - 1))
        return res
```
耗时：932 ms

## 找最大次大

题目给出的数字全部是正数，因此要求的乘积最大就是 **(最大数 - 1) * (次大数 - 1)**。题目化为求最大值和次大值的问题。

第一种想法是排序，时间复杂度是 `O(N * log(N))`.

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-2] - 1) * (nums[-1] - 1)
```
耗时：52 ms


第二种想法是遍历一遍，时间复杂度是 `O(N)`

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first = 0
        second = 0
        for num in nums:
            if num > first:
                second = first
                first = num
            elif first >= num > second:
                second = num
        return (first - 1) * (second - 1)
```
耗时：40 ms

**欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**



# 日期

2020 年 6 月 1 日 —— 6月的开始，儿童节快乐！


  [1]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/30/graph.png
  [2]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/30/graph.png
  [3]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/30/graph-1.png
