- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/max-difference-you-can-get-from-changing-an-integer/

# 题目描述


给你一个整数 `num` 。你可以对它进行如下步骤恰好 两次 ：

- 选择一个数字 `x (0 <= x <= 9)`.
- 选择另一个数字 `y (0 <= y <= 9)` 。数字 `y` 可以等于 `x` 。
- 将 `num` 中所有出现 `x` 的数位都用 `y` 替换。
- 得到的新的整数 不能 有前导 `0` ，得到的新整数也 不能 是 `0` 。

令两次对 `num` 的操作得到的结果分别为 `a` 和 `b` 。

请你返回 `a` 和 `b` 的 最大差值 。

示例 1：

    输入：num = 555
    输出：888
    解释：第一次选择 x = 5 且 y = 9 ，并把得到的新数字保存在 a 中。
    第二次选择 x = 5 且 y = 1 ，并把得到的新数字保存在 b 中。
    现在，我们有 a = 999 和 b = 111 ，最大差值为 888

示例 2：

    输入：num = 9
    输出：8
    解释：第一次选择 x = 9 且 y = 9 ，并把得到的新数字保存在 a 中。
    第二次选择 x = 9 且 y = 1 ，并把得到的新数字保存在 b 中。
    现在，我们有 a = 9 和 b = 1 ，最大差值为 8

示例 3：

    输入：num = 123456
    输出：820000

示例 4：

    输入：num = 10000
    输出：80000

示例 5：

    输入：num = 9288
    输出：8700

提示：

1. `1 <= num <= 10^8`

# 题目大意

对 num 进行两次操作：把 num 中的所有 x 都替换成 y。两次操作分别得到 a 和 b，求 a 和 b 的最大差值。

# 解题方法

## 暴力

第一个感觉是找规律，比如是否可以考虑：
1. 把从左边开始第一个不是9的数字全部替换成9得到 a（变成最大的数）。
2. 若最高位不是 1， 把最高位对应的数字全部替换成 1，得到 b；若最高位是1，则把第二个位置对应的数字全部替换换成 0，得到 b（变成最小的数）。
3. 求 a - b。

上面的步骤我没有验证，我感觉太麻烦了，不如直接暴力解。

即：把 num 中的各个数字依次替换成 0~9 ，从替换结果中找最大 - 最小。

唯一需要注意的是题目说的条件，不能以 `0` 开头。

Python 代码如下：

```python
class Solution:
    def maxDiff(self, num: int) -> int:
        replaces = []
        num = str(num)
        for i in range(0, 10):
            for j in range(0, 10):
                rep_num = num.replace(str(i), str(j))
                if rep_num[0] != '0':
                    replaces.append(int(rep_num))
        return max(replaces) - min(replaces)
```

**欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**

# 日期

2020 年 5 月 2 日 —— 双周赛最后一题不会，是时候多练练hard题了


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79451733
