
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/


# 题目描述


给你两个长度相同的整数数组 `target` 和 `arr` 。

每一步中，你可以选择 `arr` 的任意 非空子数组 并将它翻转。你可以执行此过程任意次。

如果你能让 `arr` 变得与 `target` 相同，返回 `True`；否则，返回 `False` 。


示例 1：

    输入：target = [1,2,3,4], arr = [2,4,1,3]
    输出：true
    解释：你可以按照如下步骤使 arr 变成 target：
    1- 翻转子数组 [2,4,1] ，arr 变成 [1,4,2,3]
    2- 翻转子数组 [4,2] ，arr 变成 [1,2,4,3]
    3- 翻转子数组 [4,3] ，arr 变成 [1,2,3,4]
    上述方法并不是唯一的，还存在多种将 arr 变成 target 的方法。

示例 2：

    输入：target = [7], arr = [7]
    输出：true
    解释：arr 不需要做任何翻转已经与 target 相等。

示例 3：

    输入：target = [1,12], arr = [12,1]
    输出：true

示例 4：

    输入：target = [3,7,9], arr = [3,7,11]
    输出：false
    解释：arr 没有数字 9 ，所以无论如何也无法变成 target 。

示例 5：

    输入：target = [1,1,1,1,1], arr = [1,1,1,1,1]
    输出：true
 

提示：

1. `target.length == arr.length`
1. `1 <= target.length <= 1000`
1. `1 <= target[i] <= 1000`
1. `1 <= arr[i] <= 1000`

# 题目大意

通过翻转子数组，是否能让 arr 变化为 target。

# 解题方法

## 判断排序后是否相等

这个题有很强的迷惑性。如果不看题目的难易程度是 Easy 的话，那么确实不知道怎么解决。

实际上，我们只需要把 `target` 和 `arr` 分别排序，然后判断排序后的数组是否相等即可。为什么呢？

题目说了可以任意多次的交换 `arr` 中的子数组，如果把子数组的长度设置为 2 ，即可以任意多次翻转连续的两个元素，是不是可以对 `arr` 完成冒泡排序呢？假设排序后的 `arr` 为 `sorted(arr)`。

同理，如果我也可以通过翻转连续的两个元素对 `target` 也冒泡排序，假设排序后的 `target` 为 `sorted(target)`。

如果`sorted(arr) == sorted(target)` ，我们把`sorted(arr)`按照 `target`翻转得到`sorted(target)`的操作步骤 **反过来操作一遍**就可以还原得到`target`。

因此只要两个数组如果排序后相等，那么`arr` 可以通过翻转转化成 `target`。

即操作步骤为：

    arr ==sort==> sorted(arr) == sorted(target) ==revert-sort==> target



Python 代码如下：

```python
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)
```


## 统计字符出现次数

根据上面的分析，我们也可以判断 `arr` 和 `targtet` 两个数组中的字符出现次数是否相等。如果相等，那么排序后一定也相等。

```python
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)
```

**欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**

# 日期

2020 年 5 月 31 日 —— 转眼 5 月过去了


  [1]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/03/sample_1_1791.png
  [2]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/03/sample_2_1791.png
