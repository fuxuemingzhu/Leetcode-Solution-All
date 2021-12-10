- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/the-k-strongest-values-in-an-array/


# 题目描述

给你一个整数数组 `arr` 和一个整数 `k` 。

设 `m` 为数组的中位数，只要满足下述两个前提之一，就可以判定 `arr[i]` 的值比 `arr[j]` 的值更强：

- `|arr[i] - m| > |arr[j] - m|`
- `|arr[i] - m| == |arr[j] - m|`，且 `arr[i] > arr[j]`

请返回由数组中最强的 `k` 个值组成的列表。答案可以以 **任意顺序** 返回。

**中位数** 是一个有序整数列表中处于中间位置的值。形式上，如果列表的长度为 `n` ，那么中位数就是该有序列表（下标从 `0` 开始）中位于 `((n - 1) / 2)` 的元素。

- 例如 `arr = [6, -3, 7, 2, 11]`，`n = 5`：数组排序后得到 `arr = [-3, 2, 6, 7, 11]` ，数组的中间位置为 `m = ((5 - 1) / 2) = 2` ，中位数 `arr[m]` 的值为 6 。
- 例如 `arr = [-7, 22, 17, 3]`，`n = 4`：数组排序后得到 `arr = [-7, 3, 17, 22]` ，数组的中间位置为 `m = ((4 - 1) / 2) = 1` ，中位数 `arr[m]` 的值为 3 。

示例 1：

    输入：arr = [1,2,3,4,5], k = 2
    输出：[5,1]
    解释：中位数为 3，按从强到弱顺序排序后，数组变为 [5,1,4,2,3]。最强的两个元素是 [5, 1]。[1, 5] 也是正确答案。
    注意，尽管 |5 - 3| == |1 - 3| ，但是 5 比 1 更强，因为 5 > 1 。

示例 2：

    输入：arr = [1,1,3,5,5], k = 2
    输出：[5,5]
    解释：中位数为 3, 按从强到弱顺序排序后，数组变为 [5,5,1,1,3]。最强的两个元素是 [5, 5]。

示例 3：

    输入：arr = [6,7,11,7,6,8], k = 5
    输出：[11,8,6,6,7]
    解释：中位数为 7, 按从强到弱顺序排序后，数组变为 [11,8,6,6,7,7]。
    [11,8,6,6,7] 的任何排列都是正确答案。

示例 4：

    输入：arr = [6,-3,7,2,11], k = 3
    输出：[-3,11,2]

示例 5：

    输入：arr = [-7,22,17,3], k = 2
    输出：[22,17]

提示：

1. `1 <= arr.length <= 10^5`
1. `-10^5 <= arr[i] <= 10^5`
1. `1 <= k <= arr.length`


# 题目大意

找出数组中 Top K 个数字，判断方式是各个数字与 中位数 的距离。

# 解题方法

# 自定义排序

本题需要注意的是按照题目所说去找中位数。这个中位数就是数组排序后的 `arr[(N - 1) // 2]`。

然后需要第二次排序，排序需要自定义 cmp 来比较与中位数的距离。

Python2 的自定义比较函数可以用 `cmp = 函数`，该比较函数是按照题目所说的比较规则。

最后需要注意的是排序后的 Top K 的位置在哪里，切片时不要切错。

Python 代码如下：

```python
class Solution(object):
    def getStrongest(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        N = len(arr)
        arr.sort()
        m = arr[(N - 1) // 2]
        def myCmp(x, y):
            if abs(x - m) > abs(y - m) or (abs(x - m) == abs(y - m) and x > y):
                return 1
            else:
                return -1
        arr.sort(cmp = myCmp, reverse = True)
        return arr[:k]
```

**欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**



# 日期

2020 年 6 月 21 日 —— 今晚争取也直播讲题


  [1]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/30/leetcode_max_area_2.png
  [2]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/30/leetcode_max_area_3.png
