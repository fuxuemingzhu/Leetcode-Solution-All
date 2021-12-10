
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/pyramid-transition-matrix/description/

## 题目描述

We are stacking blocks to form a pyramid. Each block has a color which is a one letter string, like `'Z'`.

For every block of color `C` we place not in the bottom row, we are placing it on top of a left block of color `A` and right block of color `B`. We are allowed to place the block there only if `(A, B, C)` is an allowed triple.

We start with a bottom row of bottom, represented as a single string. We also start with a list of allowed triples allowed. Each allowed triple is represented as a string of length 3.

Return true if we can build the pyramid all the way to the top, otherwise false.

Example 1:

    Input: bottom = "XYZ", allowed = ["XYD", "YZE", "DEA", "FFF"]
    Output: true

    Explanation:    

    We can stack the pyramid like this:
        A
       / \
      D   E
     / \ / \
    X   Y   Z
    
    This works because ('X', 'Y', 'D'), ('Y', 'Z', 'E'), and ('D', 'E', 'A') are allowed triples.

Example 2:

    Input: bottom = "XXYX", allowed = ["XXX", "XXY", "XYX", "XYY", "YXZ"]
    Output: false

    Explanation:
    We can't stack the pyramid to the top.
    Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.

Note:

1. bottom will be a string with length in range [2, 8].
1. allowed will have length in range [0, 200].
1. Letters in all strings will be chosen from the set {'A', 'B', 'C', 'D', 'E', 'F', 'G'}.

## 题目大意

给出了金字塔的底座，并给出了可以依托的砖的组合。看能否构建成一个金字塔。


可以依托的组合意思是在前两个字符的基础上可以累加一个第三个字符。举个栗子，如果对于allowed中的"XYD"，那么就是在X和Y的基础上可以增加一个D字符。


## 解题方法

### 回溯法

刚开始感觉到很难，是因为没有建立好模型，这个其实是一个考察回溯法的题目。

首先，我们来分析一下这个问题的难点在哪里。一般的回溯法题目对于下一个转移状态是很明确告知的，比如常见的地图的4或者8个方向，但是这个题目的回溯转移是需要我们简单设计一下，那就是把两个连续的字符串能够生成的所有第三个字符放到列表里，当做我们下一个前进的方向。如果把这个转移状态设计好了，我们就很容易写出代码了。

我们在每层字符串作为底座的基础上，向上面建立新的一层。所以是个递归过程。建立的方式是通过允许的组合，这个组合是我们可以通过下面的这两块砖来获得上面可以累加什么砖的方式。

所以，用curr表示当前层，用above表示上层。当curr大小为2，above为1，那么金字塔完成。如果curr = above + 1，说明上面这层已经弄好了，下面使用above来作为当前层，继续递归。

如果上面两个都不满足，说明需要继续堆积above，做的方式是在应该继续堆积的位置上，找出能堆积哪些字符，并把这个字符堆积上去，做递归。

我犯了一个错误，是使用的map保存的是键值对，但是对于重复出现的情况就被替换掉了。因此使用list才行，代表了这两块砖上面允许堆积的砖。

代码如下：

```python
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        m = collections.defaultdict(list)
        for triples in allowed:
            m[triples[:2]].append(triples[-1])
        return self.helper(bottom, "", m)
        
    def helper(self, curr, above, m):
        if len(curr) == 2 and len(above) == 1:
            return True
        if len(above) == len(curr) - 1:
            return self.helper(above, "", m)
        pos = len(above)
        base = curr[pos : pos+2]
        if base in m:
            for ch in m[base]:
                if self.helper(curr, above + ch, m):
                    return True
        return False
```

C++代码如下：

```cpp
class Solution {
public:
    bool pyramidTransition(string bottom, vector<string>& allowed) {
        if (bottom.size() == 1) return true;
        for (string& a : allowed) {
            m_[a.substr(0, 2)].push_back(a[2]);
        }
        return helper(bottom, "", m_);
    }
private:
    unordered_map<string, vector<char>> m_;
    bool helper(string pre, string cur, unordered_map<string, vector<char>>& m_) {
        if (pre.size() == 2 && cur.size() == 1) return true;
        if (pre.size() - cur.size() == 1)
            return helper(cur, "", m_);
        int pos = cur.size();
        string next = pre.substr(pos, 2);
        for (char cs : m_[next]) {
            if (helper(pre, cur + cs, m_)) {
                return true;
            }
        }
        return false;
    }
};
```

参考资料：

http://www.cnblogs.com/grandyang/p/8476646.html

## 日期

2018 年 9 月 6 日 —— 作息逐渐规律。
2019 年 1 月 25 日 —— 这学期最后一个工作日
