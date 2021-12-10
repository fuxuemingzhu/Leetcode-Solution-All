
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 公众号：负雪明烛
- 本文关键词：LeetCode，力扣，算法，算法题，交替合并字符串，Merge Strings Alternately，刷题群

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/merge-strings-alternately/

# 题目描述



有 `n` 个盒子。给你一个长度为 `n`  的二进制字符串 `boxes` ，其中 `boxes[i]` 的值为 '0' 表示第 i 个盒子是 空 的，而 `boxes[i]` 的值为 '1' 表示盒子里有 一个 小球。

在一步操作中，你可以将 一个 小球从某个盒子移动到一个与之相邻的盒子中。第 `i` 个盒子和第 `j` 个盒子相邻需满足 `abs(i - j) == 1` 。注意，操作执行后，某些盒子中可能会存在不止一个小球。

返回一个长度为 `n` 的数组 `answer` ，其中 `answer[i]` 是将所有小球移动到第 `i` 个盒子所需的 最小 操作数。

每个 `answer[i]` 都需要根据盒子的 初始状态 进行计算。

示例 1：

	输入：boxes = "110"
	输出：[1,1,3]
	解释：每个盒子对应的最小操作数如下：
	1) 第 1 个盒子：将一个小球从第 2 个盒子移动到第 1 个盒子，需要 1 步操作。
	2) 第 2 个盒子：将一个小球从第 1 个盒子移动到第 2 个盒子，需要 1 步操作。
	3) 第 3 个盒子：将一个小球从第 1 个盒子移动到第 3 个盒子，需要 2 步操作。将一个小球从第 2 个盒子移动到第 3 个盒子，需要 1 步操作。共计 3 步操作。

示例 2：
	
	输入：boxes = "001011"
	输出：[11,8,5,4,3,4]
 

提示：

1. `n == boxes.length`
2. `1 <= n <= 2000`
3. `boxes[i]` 为 '0' 或 '1'

# 解题思路

## 暴力

本题的数据规模为 2000，用 $O(N^2)$ 的解法竟然能过。这个方法比较简单，直接对每个位置向左右两边统计具体各个 1 的位置之和。

Python 代码如下：

```python
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        N = len(boxes)
        res = [0] * N
        for i in range(N):
            left = [i - j for j in range(i) if boxes[j] == "1"]
            right = [j - i for j in range(i + 1, N) if boxes[j] == "1"]
            res[i] = sum(left) + sum(right)
        return res
```

## 动态规划

这个才是我在周赛上提交的代码，时间复杂度是 $O(N)$，运行时间是上面 $O(N ^ 2)$代码的 $1/ 100$。

这个思路是：我们先找到把所有的 1 移到下标为 0 的起始位置需要的最小操作数为 $res[0]$。然后其余**把所有 1 移到 $i$ 位置的操作数 = 把所有 1 移到 $i - 1$ 位置的的操作数 -（右边的所有 1） + （左边的所有 1）**，即转移方程是：

$$res[i] = res[i - 1] - (ones - visited) + visited$$

原理是什么呢？因为把所有位置移动到 $res[i]$ 位置相对于 $res[i - 1]$ 位置来说，所有它右边位置的 1 少移动了一次，它左边位置的 1 多移动了一次。

时间复杂度：$O(N)$，空间复杂度：$O(1)$.

```python
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        N = len(boxes)
        start = 0
        ones = 0
        for i, box in enumerate(boxes):
            if box == "1":
                start += i
                ones += 1
        res = [0] * N
        visited = 0
        for i in range(len(boxes)):
            if i == 0:
                res[0] = start
            else:
                res[i] = res[i - 1] - (ones - visited) + visited
            if boxes[i] == "1":
                visited += 1
        return res
```



# 欢迎加入组织

算法每日一题是个互相帮助、互相监督的力扣打卡网站，其地址是 [https://www.ojeveryday.com/](https://www.ojeveryday.com/)

想加入千人刷题群的朋友，可以复制上面的链接到浏览器，然后在左侧点击“加入组织”，提交力扣个人主页，即可进入刷题群。期待你早日加入。

欢迎关注我的公众号：每日算法题

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210129111056950.jpg#pic_center)


# 日期

2021 年 2 月 21 日 —— 好久不打周赛了，发现手已经非常生。
