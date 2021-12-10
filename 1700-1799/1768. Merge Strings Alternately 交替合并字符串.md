
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 公众号：负雪明烛
- 本文关键词：LeetCode，力扣，算法，算法题，交替合并字符串，Merge Strings Alternately，刷题群

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/merge-strings-alternately/

# 题目描述


给你两个字符串 `word1` 和 `word2` 。请你从 `word1` 开始，通过交替添加字母来合并字符串。如果一个字符串比另一个字符串长，就将多出来的字母追加到合并后字符串的末尾。

返回 合并后的字符串 。

 

示例 1：

	输入：word1 = "abc", word2 = "pqr"
	输出："apbqcr"
	解释：字符串合并情况如下所示：
	word1：  a   b   c
	word2：    p   q   r
	合并后：  a p b q c r

示例 2：

	输入：word1 = "ab", word2 = "pqrs"
	输出："apbqrs"
	解释：注意，word2 比 word1 长，"rs" 需要追加到合并后字符串的末尾。
	word1：  a   b 
	word2：    p   q   r   s
	合并后：  a p b q   r   s

示例 3：

	输入：word1 = "abcd", word2 = "pq"
	输出："apbqcd"
	解释：注意，word1 比 word2 长，"cd" 需要追加到合并后字符串的末尾。
	word1：  a   b   c   d
	word2：    p   q 
	合并后：  a p b q c   d
 

提示：

1. `1 <= word1.length, word2.length <= 100`
1. `word1` 和 `word2` 由小写英文字母组成


# 解题思路


## 合并

交替合并两个字符串，也就是每次分别从 `word1` 和 `word2` 获取一个字符。当一个字符串用完了之后，while 循环停止，然后把另外一个字符串的剩余部分，也补充到结果中。

时间复杂度：$O(M + N)$。

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        cur1 = 0
        cur2 = 0
        res = ""
        while cur1 < len(word1) and cur2 < len(word2):
            res += word1[cur1] + word2[cur2]
            cur1 += 1
            cur2 += 1
        if cur1 != len(word1):
            res += word1[cur1:]
        if cur2 != len(word2):
            res += word2[cur2:]
        return res
```



# 欢迎加入组织

算法每日一题是个互相帮助、互相监督的力扣打卡网站，其地址是 [https://www.ojeveryday.com/](https://www.ojeveryday.com/)

想加入千人刷题群的朋友，可以复制上面的链接到浏览器，然后在左侧点击“加入组织”，提交力扣个人主页，即可进入刷题群。期待你早日加入。

**欢迎关注我的公众号：负雪明烛**

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210129111056950.jpg#pic_center)


# 日期

2021 年 2 月 21 日 —— 好久不打周赛了，发现手已经非常生。
