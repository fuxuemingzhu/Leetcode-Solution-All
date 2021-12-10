作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/number-of-equivalent-domino-pairs/

## 题目描述

Given a list of dominoes, `dominoes[i] = [a, b]` is equivalent to `dominoes[j] = [c, d]` if and only if either (`a==c and b==d`), or (`a==d and b==c`) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs `(i, j)` for which `0 <= i < j < dominoes.length`, and `dominoes[i]` is equivalent to `dominoes[j]`.
 
Example 1:

    Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
    Output: 1
 

Constraints:

1. 1 <= dominoes.length <= 40000
1. 1 <= dominoes[i][j] <= 9


## 题目大意

多米诺骨牌上有两个数字，只要这两个数字相等（不用在乎位置是否对应），那么两个多米诺骨牌就是相等的。问有多少组相等的多米诺骨牌。

## 解题方法

### 字典统计

第一感觉是可以暴力求解：两两判断二元组是否相等，该方法的时间复杂度是 O(N ^ 2)。但可行性被输入数组的长度最大为 40000 而打破了。介绍一下估算时间复杂度的方法：


- 已知 N = 40000, 时间复杂度为 O(N ^ 2)，则需要计算 40000 ^ 2 = 16 0000 0000 次。而 力扣 平台上对于一个题目允许使用的计算量一般是 1亿 次。所以对于改题目来说，O(N ^ 2)的方法会超时。


必须要用时间复杂度更低的方法。

从最简单的一个数组中有多少对相等元素说起：从数组 a = [1, 1, 2, 2, 2, 3] 中抽取两个元素，总共有多少种相等的情况呢？

我们发现只用计算相同的元素中有多少组合数，然后加在一起即可。
- 从 [1, 1] 中抽取两个元素，共有 1 种组合。
- 从 [2, 2, 2] 中抽取两个元素，共有 3 种组合。
所以从数组 a 中抽取相等的两个元素，总的有 1 + 3 种组合。

高中排列组合告诉我们：从长度为 x 的数组中抽取两个元素，总共有 `x * (x - 1) / 2` 种抽法。
对于输入的数组 a 来说，我们需要统计 a 中各元素的出现次数 x，然后累加每个元素能构成的相同元素数 `x * (x - 1) / 2` 。

解决问题的思路已经有了，力扣的这个题目，不就是把判断数组中的元素变成了二元组了么？只要我们能把二元组当做一个元素进行处理，就可以直接套用上面的思路！

我们可以使用映射：把相等的二元组映射成同一个元素，不同的二元组映射成不同的元素。比如把二元组`[a, b]`映射成一个0~99的数字：如果`a < b`，则映射成 `10 * a + b`，否则映射成 `10 * b + a`。对于二元组`[b, a]` ，使用上述映射方法，也会映射成相等的数字。但对于 `[c, d]`，只要该二元组不和 `[a, b]`相等，它就不可能映射成和 `[a, b]` 相同的数字。

综上，解决本题的思路已经有了：先统计 `dominoes` 中相等的二元组出现的个数，然后遍历每个二元组出现的个数 `x`，累加 `x * (x - 1) / 2` 。


## 代码




使用映射的思路，有了下面的第一版代码（Python）：

```python
class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        count = dict()
        for domi in dominoes:
            hash_ = domi[0] * 10 + domi[1] if domi[0] < domi[1] else domi[1] * 10 + domi[0]
            if hash_ in count:
                count[hash_] += 1
            else:
                count[hash_] = 1
        res = 0
        for v in count.values():
            res += v * (v - 1) / 2
        return res
```

上面的写法，是为了照顾各个语言的读者，因此写的比较通用。对于使用 Python 刷题的同学来说，我认为使用简单的 Python 函数，让代码更加 Pythonic 是有必要的。

分享本题可以使用的更 Pythonic 的函数：

- `map(f, x)`：该函数返回 `f(x)`。

- `collections.Counter(arr)`：该函数统计数组 `arr` 中各元素出现的次数，本质是个 dict，即字典。

- `sum(arr)`：该函数对数组 `arr` 进行求和。


另外，分享一个 Python 的语法是 数组`array` ，用方括号`[]`表示，是可变对象，不能作为字典的 key。但是 元组`tuple`，用圆括号()表示，是不可变对象，可以作为字典的 `key`。并且 `array` 和 `tuple` 可以相互转化。

我们可以把输入的二元组排序之后，映射成 tuple，作为字典的 key!

综上，我写了一个更简短的 Python 代码，留给读者把玩。

```python
class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        dominoes = map(tuple, map(sorted, dominoes))
        count = collections.Counter(dominoes)
        values = map(lambda v : v * (v - 1) / 2, count.values())
        return sum(values)
```

## 复杂度分析

- 时间复杂度是O(N)，因为每个元素只需要遍历一遍。
- 这两种写法的空间复杂度都是O(1)，因为只会映射到0~99，字典中最多100个key，不会随着输入dominoes的增加而增加。



## 日期

2019 年 7 月 28 日 —— kickstart完败
2021 年 1 月 26 日 —— 持续更新微信公众号的第2天
