
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/check-if-all-1s-are-at-least-length-k-places-away/


# 题目描述

给你一个由若干 `0` 和 `1` 组成的数组 `nums` 以及整数 `k`。如果所有 `1` 都至少相隔 `k` 个元素，则返回 `True` ；否则，返回 `False` 。


示例 1：

![此处输入图片的描述][1]

    输入：nums = [1,0,0,0,1,0,0,1], k = 2
    输出：true
    解释：每个 1 都至少相隔 2 个元素。

示例 2：

![此处输入图片的描述][2]

    输入：nums = [1,0,0,1,0,1], k = 2
    输出：false
    解释：第二个 1 和第三个 1 之间只隔了 1 个元素。

示例 3：

    输入：nums = [1,1,1,1,1], k = 0
    输出：true

示例 4：

    输入：nums = [0,1,0,1], k = 1
    输出：true
     

提示：

1. `1 <= nums.length <= 10^5`
1. `0 <= k <= nums.length`
1. `nums[i]` 的值为 `0` 或 `1`



# 题目大意

判断给出的数组中，是否所有的 1 的间隔都至少为 k.

# 解题方法

## 指针

看一眼题目给出的 nums 的长度，我们知道必须用 O(1) 的时间复杂度解决。

使用一次遍历，在遍历的过程中，使用 left_1 指针保存当前遍历位置左边的最后一个 1。如果当前遍历的数字也是 1，则判断一下和左边最后一个 1 的距离是否 >= k + 1。

Python 代码如下：

```python
class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        left_1 = float("-inf")
        for i, num in enumerate(nums):
            if num == 1:
                if i - left_1 < k + 1:
                    return False
                left_1 = i
        return True
```

**欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**

# 日期

2020 年 5 月 3 日 —— 天气好热，瞬间入夏


  [1]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/03/sample_1_1791.png
  [2]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/03/sample_2_1791.png
