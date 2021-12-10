- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/longest-happy-string/

# 题目描述

如果字符串中不含有任何 `'aaa'`，`'bbb'` 或 `'ccc'` 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。

给你三个整数 `a`，`b` ，`c`，请你返回 任意一个 满足下列全部条件的字符串 s：

- `s` 是一个尽可能长的快乐字符串。
- `s` 中 最多 有`a 个字母 'a'、b 个字母 'b'、c 个字母 'c'` 。
- `s` 中只含有 `'a'、'b' 、'c'` 三种字母。

如果不存在这样的字符串 s ，请返回一个空字符串 ""。

示例 1：

    输入：a = 1, b = 1, c = 7
    输出："ccaccbcc"
    解释："ccbccacc" 也是一种正确答案。

示例 2：

    输入：a = 2, b = 2, c = 1
    输出："aabbc"

示例 3：
    
    输入：a = 7, b = 1, c = 0
    输出："aabaa"
    解释：这是该测试用例的唯一正确答案。

提示：

1. `0 <= a, b, c <= 100`
2. `a + b + c > 0`


# 题目大意

a 个字母 'a'、b 个字母 'b'、c 个字母 'c'，不准出现连续三个相同的字母。可以够成的最长的字符串是什么。

# 解题方法

## 贪心

做法：在保证没有连续三个字符相等的情况下，不停地从 a, b, c 中**优先使用剩余次数最多**的那个字符添加到结果 res 中。

1. 使用数组表示出 a, b, c的次数和字符的对应关系，防止排序搞混乱了。
2. 判断某个字符 x 能否添加到 res 最后的方法是，res 长度 < 2 或者 res 的最后两个字符至少有一个不等于 x.
3. 只要a, b, c没用完，就一直循环，从数组中优先拿出现次数最多的。如果该字符不能添加，就判断下一个，如果都不能添加则终止。

解释下 `for...break...else`语句：如果 for 循环中没有调用 break，那么使用 else 。 

Python 代码如下。

```python
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        d = [[a, "a"], [b, "b"], [c, "c"]]
        total = a + b + c
        res = ""
        def canAdd(res, x):
            return len(res) < 2 or res[-1] != x or res[-2] != x
        while total > 0:
            d.sort(reverse=True)
            for i, (count, char) in enumerate(d):
                if count == 0: continue
                if canAdd(res, char):
                    res += char
                    d[i][0] -= 1
                    total -= 1
                    break
            else:
                break
        return res
```

 **欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**

# 日期

2020 年 4 月 5 日 —— 好久不打周赛了


  [1]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/04/04/sample_4_1728.png
  [2]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/04/04/sample_2_1728.png
  [3]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/04/04/sample_6_1728.png
