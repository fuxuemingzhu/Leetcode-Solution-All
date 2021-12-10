作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

@[TOC](目录)


题目地址：https://leetcode.com/problems/2-keys-keyboard/description/

## 题目描述

Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

- Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
- Paste: You can paste the characters which are copied last time.

Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

Example 1:

    Input: 3
    Output: 3
    
    Explanation:
    Intitally, we have one character 'A'.
    In step 1, we use Copy All operation.
    In step 2, we use Paste operation to get 'AA'.
    In step 3, we use Paste operation to get 'AAA'.

Note:

1. The n will be in the range [1, 1000].


## 题目大意

给定两种操作，复制和粘贴。

- 复制：只能复制写字板上存在的所有字符。
- 粘贴：必须粘贴复制操作得到的所有字符。

给定一个初始的写字板上的字符’A’，问最少经过多少次操作（每次复制/粘贴分别算一次操作），写字板上’A’的个数才能为 n。 

注意不能手动敲一个'A'上去，必须复制粘贴！

## 解题方法

### 递归

我们先分析递归的方法，递归的思想是**由上向下**。

举个例子：当 n = 36 的时候。

	36 = 18 * 2 = 3 * 3 * 2 * 2

如果我们想获得 36 个相同的A，可以先获得 18 个`'A'`，然后复制 1 次，粘贴 1 次，于是就有了 36 个`'A'`。这就是 36 = 18 * 2 的含义。然后再思考怎么得到 18 个`'A'`，这就是递归。

当起始只有一个`'A'`的情况下，一种得到36个`'A'`的方案为：

1. 复制 1 次，粘贴 2 次，得到 `'AAA'`
2. 在上面的基础上，复制 1 次，粘贴 2 次，得到  `'AAAAAAAAA'`
3. 在上面的基础上，复制 1 次，粘贴 1 次，得到 18 个 `'A'`
4. 在上面的基础上，复制 1 次，粘贴 1 次，得到 36 个 `'A'`

因为复制和粘贴都算一次操作，所以上面得到了 3 * 3 * 2 * 2 = 36 个`'A'`。

我们可以得出结论：

1. 如果 `n` 是素数的话，我们只能通过复制 1 次A，然后粘贴 `n - 1` 次的方式才能得到 `n` 个A。总的操作了 `n` 次。
2. 如果 `n = i * j` 的话，最快得到 `n` 的方式是先得到 `i` ，复制 1 次，然后再粘贴 `j - 1` 次，总的就有了 `n` 个A。总的操作了 `minSteps(i) + 1 + j - 1 = minSteps(i) + j = minSteps(i) + n / i` 次。

于是就有了递归的解法。该解法是，先让 i 从 2 开始遍历找到 n  - 1，判断 i 是不是 n 的因子，如果 i 是 n 的因子，那么总的需要操作 `minSteps(i) + n / i`次。如果从 2 到 n - 1 没有 n 的因子，那么 n 是个素数，必须操作 n 次。

Python代码如下。

```python
class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        for i in range(2, n):
            if n % i == 0:
                return self.minSteps(n // i) + i
        return n
```

### 素数分解

上面已经给了递归的做法，看了 36 个 `'A'` 的分解之后，我们发现题目要求的就是 36 的所有**素因子**之和。素因子是指，该因子不可再次拆分。

为什么非得拆解成 素因子 呢？因为当一个因子还可以分解成更小的因子的时候，那么分解后的结果会更小。

比如 36 = 18 * 2，题目所求的最优结果是 18 + 2 = 20 么？显然不是，因为如果把18 拆开 36 = 3 * 6 * 2，此时复制粘贴的个数只需要 3 + 6 + 2 = 12 次。但这仍然不是最优结果，36 = 3 * 2 * 3 * 2，此时复制粘贴的个数只需要 3 + 2 + 3 + 2 = 10 次。此时已经是最优了。

具体证明就是要证明 m * n > m + n，等价于求 (m - 1)*(n - 1) > 1，当 m 和 n 大于 2 的时候上式永远成立。

至于代码，就是让我们求 n 能拆成哪些素因子。我们让 d 试探是否为因子从 2 开始递增，如果 n 能被 d 整除时，此时的 d 是 n 的一个素因子，求复制粘贴次数的结果中增加 d ；而且如果 d 是个素因子，那么要一次性把 n 中除掉所有的 d。

Python 代码如下。

```python
class Solution:
    def minSteps(self, n: int) -> int:
        res = 0
        d = 2
        while n > 1:
            while n % d == 0:
                res += d
                n //= d
            d += 1
        return res
```

参考：

https://leetcode-cn.com/problems/2-keys-keyboard/solution/zhi-you-liang-ge-jian-de-jian-pan-by-leetcode/

## 日期

2018 年 3 月 15 日 —— 雾霾消散，春光明媚
2020 年 5 月 30 日 —— 答辩顺利，心情大好
