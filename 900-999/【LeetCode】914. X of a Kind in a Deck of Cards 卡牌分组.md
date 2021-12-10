
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址: https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/description/

## 题目描述

In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.
 

Example 1:

    Input: [1,2,3,4,4,3,2,1]
    Output: true
    Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]

Example 2:

    Input: [1,1,1,2,2,2,3,3]
    Output: false
    Explanation: No possible partition.

Example 3:

    Input: [1]
    Output: false
    Explanation: No possible partition.

Example 4:

    Input: [1,1]
    Output: true
    Explanation: Possible partition [1,1]

Example 5:

    Input: [1,1,2,2,2,2]
    Output: true
    Explanation: Possible partition [1,1],[2,2],[2,2]

Note:

1. 1 <= deck.length <= 10000
1. 0 <= deck[i] < 10000


## 题目大意

判断一堆牌能不能分成很多组，每个组是相同的元素，并且每个组最少两张牌。

## 解题方法

### 遍历

果然是个Easy的题目，很简单。

每个组的元素都是相同的情况下，分组之后每个组有多少个元素呢？

首先，要求每个组的元素都是相同的，因此元素个数最小的那个组限制了每个组的个数。

但不一定是所有元素个数的最小值，因为相同的元素可以分成很多组的，比如这个测试用例，每个组可以都是两个元素即可。

    [1,1,1,1,2,2,2,2,2,2]

所以，可以用一个遍历，从2遍历到`最少次数的数字`中的元素个数。道理是，把最少次数在划分和不划分的情况下，看其他组能不能按照这个个数进行均分。

最坏情况下的时间复杂度是O(N^2)，空间复杂度是O(N)。

Python代码如下：

```python
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        count = collections.Counter(deck)
        X = min(count.values())
        for x in range(2, X + 1):
            if all(v % x == 0 for v in count.values()):
                return True
        return False
```

### 最大公约数
二刷的时候想到了最大公约数解法。

最终分的组的大小是多少，就是每个数字的次数的最大公约数。

比如例子：

	[1,1,2,2,2,2]

最终分成了`[1,1],[2,2],[2,2]`，每个组是2个数字，怎么得来的？看`1`出现了2次，看`2`出现了4次，最终的结果就是2和4的最大公约数2。

公约数能被所有的数字个数整除，所以最大的那个公约数，就是能被所有数字个数整除的最大组大小。

C++代码如下：

```cpp
class Solution {
public:
    bool hasGroupsSizeX(vector<int>& deck) {
        unordered_map<int, int> counter;
        for (int d : deck) {
            counter[d] ++;
        }
        int res = 0;
        for (auto& c : counter) {
            res = gcd(c.second, res);
        }
        return res > 1;
    }
    int gcd(int x, int y) {
        return y == 0 ? x : gcd(y, x % y);
    }
};
```

## 日期

2018 年 9 月 30 日 —— 9月最后一天啦！
2018 年 11 月 24 日 —— 周日开始！一周就过去了～
2020 年 3 月 27 日 —— 开始整合资源
