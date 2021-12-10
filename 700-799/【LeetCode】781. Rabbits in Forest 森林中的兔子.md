
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/rabbits-in-forest/description/

## 题目描述

In a forest, each rabbit has some color. Some subset of rabbits (possibly all of them) tell you how many other rabbits have the same color as them. Those answers are placed in an array.

Return the minimum number of rabbits that could be in the forest.

Examples:

    Input: answers = [1, 1, 2]
    Output: 5
    Explanation:
    The two rabbits that answered "1" could both be the same color, say red.
    The rabbit than answered "2" can't be red or the answers would be inconsistent.
    Say the rabbit that answered "2" was blue.
    Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
    The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.
    
    Input: answers = [10, 10, 10]
    Output: 11
    
    Input: answers = []
    Output: 0

Note:

1. answers will have length at most 1000.
1. Each answers[i] will be an integer in the range [0, 999].

## 题目大意

兔子会报出和自己颜色相同的兔子数量，求最少的兔子数。

## 解题方法

充分理解大神的思路：

> If ``x+1`` rabbits have same color, then we get ``x+1`` rabbits who all answer ``x``. now ``n`` rabbits answer ``x``. 
> If ``n%(x+1)==0``, we need ``n/(x+1)`` groups of ``x+1`` rabbits. 
> If ``n%(x+1)!=0``, we need ``n/(x+1) + 1`` groups of ``x+1`` rabbits.
> the number of groups is math.ceil(n/(x+1)) and it equals to (n+i)/(i+1) , which is more elegant.

翻译一下：

当某个兔子回答x的时候，那么数组中最多允许x+1个兔子同时回答x，那么我们统计数组中所有回答x的兔子的数量n：

若 n%(x+1)==0，说明我们此时只需要 n/(x+1) 组个数为x+1的兔子。

若 n%(x+1)!=0，说明我们此时只需要 n/(x+1) + 1 组个数为x+1的兔子。

那么这两种情况可以通过 ceil(n/(x+1)) 来整合，而这个值也等于 (n + x) / (x + 1).

可以理解为，对每个数字进行记数，如果其出现的次数n能整除（x+1），说明能够成一个颜色，所以x+1个兔子。如果不能整除的话，说明有``n/(x+1) + 1``组兔子。然后一个简化计算的方案。

代码：

```python
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        count = collections.Counter(answers)
        print count
        return sum((count[x] + x) / (x + 1) * (x + 1) for x in count)
```

C++代码如下：

```cpp
class Solution {
public:
    int numRabbits(vector<int>& answers) {
        int res = 0;
        unordered_map<int, int> m;
        for (int a : answers) m[a]++;
        for (auto a : m) {
            res += (a.second + a.first) / (a.first + 1) * (a.first + 1);
        }
        return res;
    }
};
```

## 日期

2018 年 3 月 6 日 
2018 年 12 月 18 日 —— 改革开放40周年
