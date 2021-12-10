
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 公众号：负雪明烛
- 本文关键词：LeetCode，力扣，算法，算法题，字符串，并查集，刷题群

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/similar-string-groups/

# 题目描述

如果交换字符串 `X`  中的**两个**不同位置的字母，使得它和字符串 `Y`  相等，那么称 `X` 和 `Y`  两个字符串相似。如果这两个字符串本身是相等的，那它们也是相似的。


例如，对于 ["tars", "rats", "arts", "star"] 这四个字符串而言：


- "**t**a**r**s" 和 "**r**a**t**s" 是相似的 (交换 0 与 2 的位置)； "**ra**ts" 和 "**ar**ts" 也是相似的。
- 但是 "star" **不与** ["tars"，"rats"，"arts"] 中的任意一个相似，因为无法通过交换 star 中的两个不同位置字母得到三者的任意一个。



总之，它们通过相似性形成了两个关联组：**{"tars", "rats", "arts"} **和** {"star"}**。注意，**"tars"** 和 **"arts"** 是在同一组中，即使它们并不相似。形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。


![在这里插入图片描述](https://img-blog.csdnimg.cn/20210131114048630.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Z1eHVlbWluZ3podQ==,size_16,color_FFFFFF,t_70)


给你一个字符串列表 `strs` 。列表中的每个字符串都是 `strs`  中其它所有字符串的一个字母异位词。请问 `strs`  中有多少个 **相似字符串组**？


示例：


输入：strs = ["tars","rats","arts","star"]
输出：2
解释：如题目上文所解释，可以分为 {"tars", "rats", "arts"} 和 {"star"} 两个相似字符串组。



# 解题思路

## 并查集


今天的题目的中文题意比较模糊，我看了很久才明白**相似字符串组**的含义。即相似字符串组中的每个字符串都有另外至少一个字符串和它相似。比如对于 **{"tars", "rats", "arts"}** 这个相似字符串组而言，相似关系是 **"tars" <=> "rats" <=> "arts"**。

两个字符串相似的含义是能够通过交换两个字符的位置，得到另外一个字符串。判断两个字符串相似的时间的复杂度是 O(N)，因为把所有位置遍历一次，统计两个字符串的对应位置有多少不等即可。

**明白了题意之后，做法也就呼之欲出了：把每个字符串当做图中的一个节点，如果两个字符串相似，那么它们之间就有一条边。图中的每个连通区域是一个相似字符串组。问：图中有多少个不连通的区域？**

很显然，图的连通性问题可以用「并查集」去做。然后套「并查集」的模板就可以了。


这也是我之前说的：“在明白题目考察什么之后，剩下的就是套模板”。


和今天题目非常类似的题目是「1579. 保证图可完全遍历」，我前几天的文章已经详细分析过了，两者都是考察图中有多少个连通区域，都是直接使用并查集模板。


# 代码

每个字符串都是一个节点，我们需要分析每两个节点之间是否相似，如果相似就添加一条边，使用并查集，看最终有多少个连通区域。


代码思路：


1. 两重 for 循环，实现对节点之间两两组合，判断两个节点是否相似；
1. 判断相似的方法是：两个字符串的对应位置中只有 0 个或者 2 个不同；
1. 如果两个字符串相似则使用并查集，将此两个节点之间连通上一条边；
1. 统计最终并查集中有多少个不同的连通区域，即为所求。



使用 Python2 写的代码如下。

```python
class Solution(object):
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        N = len(strs)
        dsu = DSU(N)
        for i in range(N):
            for j in range(i + 1, N):
                if self.isSimilar(strs[i], strs[j]):
                    dsu.union(i, j)
        return dsu.regions()
            
    def isSimilar(self, str1, str2):
        count = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count += 1
        return count == 2 or count == 0

class DSU:
    def __init__(self, N):
        self.par_ = range(N + 1)
        self.regions_ = N

    def find(self, x):
        if x != self.par_[x]:
            self.par_[x] = self.find(self.par_[x])
        return self.par_[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        self.par_[px] = py
        self.regions_ -= 1
    
    def regions(self):
        return self.regions_
```

# 刷题心得


今天的题目考察并查集，仍然是可以直接套模板。本周已经连续考察了多个并查集问题，相信大家已经掌握了模板。昨天有群友说，感谢每日一题连续这么多次都是并查集题目，他现在已经能够背下来模板了。这也是大家的算法成长过程。刷题一定要坚持呀！

力扣题目一般是单一考点，即每个题目只考察一个知识点。因此做每个题目时，有一半的工作量是在思考这个题目在考察什么，剩下的一半工作量就是在套模板。把题目抽象成具体考察点的能力需要我们经常练习，也是靠多刷题来获得，当然啦，多看看负雪明烛的解题思路，也会对大家很有帮助的！

OK，这就是本次题解的全部内容了，如果你觉得我的题解对你有帮助的话，求赞、求关注、求转发、求在看。你的认可就是我前进的最大动力！我们明天再见！

# 欢迎加入组织

算法每日一题是个互相帮助、互相监督的力扣打卡网站，其地址是 [https://www.ojeveryday.com/](https://www.ojeveryday.com/)

想加入千人刷题群的朋友，可以复制上面的链接到浏览器，然后在左侧点击“加入组织”，提交力扣个人主页，即可进入刷题群。期待你早日加入。

欢迎关注我的公众号：负雪明烛

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210129111056950.jpg#pic_center)


# 日期

2021 年 1 月 31 日 —— 周末加油！努力！
