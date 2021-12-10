- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/contest/weekly-contest-185/problems/minimum-number-of-frogs-croaking/

# 题目描述


给你一个字符串 `croakOfFrogs`，它表示不同青蛙发出的蛙鸣声（字符串 `"croak"` ）的组合。由于同一时间可以有多只青蛙呱呱作响，所以 `croakOfFrogs` 中会混合多个 `“croak”` 。请你返回模拟字符串中所有蛙鸣所需不同青蛙的最少数目。

注意：要想发出蛙鸣 `"croak"`，青蛙必须 依序 输出 `‘c’, ’r’, ’o’, ’a’, ’k’` 这 5 个字母。如果没有输出全部五个字母，那么它就不会发出声音。

如果字符串 `croakOfFrogs` 不是由若干有效的 `"croak"` 字符混合而成，请返回 -1 。

示例 1：

    输入：croakOfFrogs = "croakcroak"
    输出：1 
    解释：一只青蛙 “呱呱” 两次

示例 2：

    输入：croakOfFrogs = "crcoakroak"
    输出：2 
    解释：最少需要两只青蛙，“呱呱” 声用黑体标注
    第一只青蛙 "crcoakroak"
    第二只青蛙 "crcoakroak"

示例 3：

    输入：croakOfFrogs = "croakcrook"
    输出：-1
    解释：给出的字符串不是 "croak" 的有效组合。

示例 4：

    输入：croakOfFrogs = "croakcroa"
    输出：-1
     

提示：

1. `1 <= croakOfFrogs.length <= 10^5`
1. 字符串中的字符只有 'c', 'r', 'o', 'a' 或者 'k'


# 题目大意

按顺序出现的 `"croak"` 即为一次青蛙叫，问给出的字符串中最少有多少个青蛙。

# 解题方法

## 字典

这个题是消消乐问题。

这个题我第一想法是保留各个青蛙的叫声字符串，然后进行查找、匹配、消除。但这个做法会超时，因此不能全部保留青蛙的叫声字符串。

其实我们没有必要保留所有的字符串，只需要知道各个前缀出现的次数就行了。

对叫声字符串进行一遍循环，根据 `croak` 每个字符的前面的字符是什么，对其前面的字符进行-1，当前字符+1。

里面有两个特例：起始的字符`"c"`不需要查找前面的字符，结束的字符`"k"`不需要对当前字符+1。


举例看下匹配的过程：

    输入： "croakcroak"
    匹配的过程：
    c
    Counter({'c': 1})
    r
    Counter({'r': 1, 'c': 0})
    o
    Counter({'o': 1, 'c': 0, 'r': 0})
    a
    Counter({'a': 1, 'c': 0, 'r': 0, 'o': 0})
    k
    Counter({'c': 0, 'r': 0, 'o': 0, 'a': 0})
    c
    Counter({'c': 1, 'r': 0, 'o': 0, 'a': 0})
    r
    Counter({'r': 1, 'c': 0, 'o': 0, 'a': 0})
    o
    Counter({'o': 1, 'c': 0, 'r': 0, 'a': 0})
    a
    Counter({'a': 1, 'c': 0, 'r': 0, 'o': 0})
    k
    Counter({'c': 0, 'r': 0, 'o': 0, 'a': 0})


Python代码如下：

```python
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        count = collections.Counter()
        prev = {"k" :  "a", "a": "o", "o": "r", "r" : "c"}
        res = 0
        for c in croakOfFrogs:
            if c == "c":
                count[c] += 1
            else:
                if count[prev[c]] > 0:
                    if c != "k":
                        count[c] += 1
                    count[prev[c]] -= 1
                else:
                    return -1
            res = max(res, sum(count.values()))
        return res if sum(count.values()) == 0 else -1
```


**欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**

# 日期

2020 年 4 月 19 日 —— 近期比赛太多


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79451733
