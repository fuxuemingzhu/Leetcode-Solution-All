
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 公众号：负雪明烛
- 本文关键词：LeetCode，力扣，算法，算法题，字符串，并查集，刷题群

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/get-equal-substrings-within-budget/

# 题目描述



给你两个长度相同的字符串， `s` 和 `t`  。


将 `s` 中的第 `i` 个字符变到 `t` 中的第 `i` 个字符需要 `|s[i] - t[i]|` 的开销（开销可能为 0），也就是两个字符的 ASCII 码值的差的绝对值。


用于变更字符串的最大预算是 `maxCost` 。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。


如果你可以将 `s` 的子字符串转化为它在 `t` 中对应的子字符串，则返回可以转化的最大长度。


如果 `s` 中没有子字符串可以转化成 `t` 中对应的子字符串，则返回 0。


## 示例


> 输入：s = "abcd", t = "bcdf", maxCost= 3
>
> 输出：3
>
> 解释：s 中的 "abc" 可以变为 "bcd"。开销为 3，所以最大长度为 3。



# 解题思路

## 滑动窗口



今天这个题目比较难理解，我需要再解释一下。


两个长度相等字符串的 `s` 和 `t` ，把 `i` 位置的 `s[i]` 转成 `t[i]` 的开销是两者 ASCII 码之差的绝对值。题目给出了允许的最大预算 `maxCost` ，求不超过预算的情况下能够转换的**最长子串**。


比如，对于 `s = "abcd", t = "bcdf", cost = 3` 而言，我们使用 `costs[i]` 表示从 `s[i]`  转成 `t[i]` 的开销，那么 `costs = [1, 1, 1, 2]` 。由于 maxCost = 3， 所以最多允许其前面三个字符进行转换。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210205090023625.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Z1eHVlbWluZ3podQ==,size_16,color_FFFFFF,t_70)




于是题目变成了：**已知一个数组 costs ，求：和不超过 maxCost 时最长的子数组的长度**。


上面的表达方式跟题目是等价的。对题目抽象之后，是不是跟昨天的每日一题「643. 子数组最大平均数 I」非常像了？也和「424. 替换后的最长重复字符」非常像。这就是坚持刷每日一题的作用，大家继续坚持啊！


抽象之后，我们知道这是一个区间题，求**子区间**经常使用的方法就是**滑动窗口**。我在[「424. 替换后的最长重复字符」的题解](https://leetcode-cn.com/problems/longest-repeating-character-replacement/solution/fen-xiang-zhen-cang-de-shuang-zhi-zhen-m-fdsk/)中已经分享了我珍藏的**滑动窗口**模板，由于模板是通用的，因此我把当时的题解再拿过来分享给大家。

---

《挑战程序设计竞赛》这本书中把**滑动窗口**叫做「虫取法」，我觉得非常生动形象。因为**滑动窗口**的两个指针移动的过程和虫子爬动的过程非常像：**前脚不动，把后脚移动过来；后脚不动，把前脚向前移动**。


我分享一个**滑动窗口的模板**，能解决大多数的**滑动窗口**问题：


```python
def findSubArray(nums):
    N = len(nums) # 数组/字符串长度
    left, right = 0, 0 # 双指针，表示当前遍历的区间[left, right]，闭区间
    sums = 0 # 用于统计 子数组/子区间 是否有效，根据题目可能会改成求和/计数
    res = 0 # 保存最大的满足题目要求的 子数组/子串 长度
    while right < N: # 当右边的指针没有搜索到 数组/字符串 的结尾
        sums += nums[right] # 增加当前右边指针的数字/字符的求和/计数
        while 区间[left, right]不符合题意：# 此时需要一直移动左指针，直至找到一个符合题意的区间
            sums -= nums[left] # 移动左指针前需要从counter中减少left位置字符的求和/计数
            left += 1 # 真正的移动左指针，注意不能跟上面一行代码写反
        # 到 while 结束时，我们找到了一个符合题意要求的 子数组/子串
        res = max(res, right - left + 1) # 需要更新结果
        right += 1 # 移动右指针，去探索新的区间
    return res
```


滑动窗口中用到了左右两个指针，它们移动的思路是：**以右指针作为驱动，拖着左指针向前走。右指针每次只移动一步，而左指针在内部 while 循环中每次可能移动多步。右指针是主动前移，探索未知的新区域；左指针是被迫移动，负责寻找满足题意的区间。**


模板的整体思想是：


1. 定义两个指针 `left` 和 `right` 分别指向区间的开头和结尾，注意是闭区间；定义 `sums` 用来统计该区间内的各个字符出现次数；
1. 第一重 `while` 循环是为了判断 `right` 指针的位置是否超出了数组边界；当 `right` 每次到了新位置，需要增加 `right` 指针的求和/计数；
1. 第二重 `while` 循环是让 `left` 指针向右移动到 `[left, right]` 区间符合题意的位置；当 `left` 每次移动到了新位置，需要减少 `left` 指针的求和/计数；
1. 在第二重 `while` 循环之后，成功找到了一个符合题意的 `[left, right]` 区间，题目要求最大的区间长度，因此更新 `res` 为 `max(res, 当前区间的长度)` 。
1. `right` 指针每次向右移动一步，开始探索新的区间。



模板中的 `sums` 需要根据题目意思具体去修改，本题是求和题目因此把`sums` 定义成整数用于求和；如果是计数题目，就需要改成字典用于计数。当左右指针发生变化的时候，都需要更新 `sums` 。

另外一个需要根据题目去修改的是内层 while 循环的判断条件，即： **区间[left, right]不符合题意 **。对于本题而言，就是该区内的**和** `sums` 超过了 `maxCost` 。

# 代码


我记住了上面的模板，在输入框里快速敲了一遍，直接点提交就通过了。

使用 Python2 写的代码如下。

```python
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        N = len(s)
        costs = [0]* N
        for i in range(N):
            costs[i] = abs(ord(s[i]) - ord(t[i]))
        left, right = 0, 0
        res = 0
        sums = 0
        while right < N:
            sums += costs[right]
            while sums > maxCost:
                sums -= costs[left]
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res
```


- 时间复杂度： `O(N)` ，因为两个指针分别都只把每个元素遍历了一次。
- 空间复杂度： `O(N)` ，因为使用了 costs 数组用于保存每个字符转换的开销。

# 刷题心得



1. 读了题目之后，要反应过来这是求一个最长区间的问题，从而想到滑动窗口。
1. 滑动窗口是有模板的，理解之后，形成肌肉记忆，下次直接敲出来。
1. 坚持刷每日一题，会发现自己在潜移默化中进步。


# 欢迎加入组织

算法每日一题是个互相帮助、互相监督的力扣打卡网站，其地址是 [https://www.ojeveryday.com/](https://www.ojeveryday.com/)

想加入千人刷题群的朋友，可以复制上面的链接到浏览器，然后在左侧点击“加入组织”，提交力扣个人主页，即可进入刷题群。期待你早日加入。

欢迎关注我的公众号：每日算法题

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210129111056950.jpg#pic_center)


# 日期

2021 年 2 月 5 日 —— 小年了，加油
