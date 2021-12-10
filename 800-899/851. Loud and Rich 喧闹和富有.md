# 【LeetCode】851. Loud and Rich 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/loud-and-rich/description/

## 题目描述：

In a group of N people (labelled 0, 1, 2, ..., N-1), each person has different amounts of money, and different levels of quietness.

For convenience, we'll call the person with label x, simply "person x".

We'll say that richer[i] = [x, y] if person x definitely has more money than person y.  Note that richer may only be a subset of valid observations.

Also, we'll say quiet[x] = q if person x has quietness q.

Now, return answer, where answer[x] = y if y is the least quiet person (that is, the person y with the smallest value of quiet[y]), among all people who definitely have equal to or more money than person x.

 

Example 1:

    Input: richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]
    Output: [5,5,2,5,4,5,6,7]
    
    Explanation: 
    
    answer[0] = 5.
    Person 5 has more money than 3, which has more money than 1, which has more money than 0.
    The only person who is quieter (has lower quiet[x]) is person 7, but
    it isn't clear if they have more money than person 0.
    
    answer[7] = 7.
    Among all people that definitely have equal to or more money than person 7
    (which could be persons 3, 4, 5, 6, or 7), the person who is the quietest (has lower quiet[x])
    is person 7.
    
    The other answers can be filled out with similar reasoning.

Note:

1. 1 <= quiet.length = N <= 500
1. 0 <= quiet[i] < N, all quiet[i] are different.
1. 0 <= richer.length <= N * (N-1) / 2
1. 0 <= richer[i][j] < N
1. richer[i][0] != richer[i][1]
1. richer[i]'s are all different.
1. The observations in richer are all logically consistent.



## 题目大意

这个题目理解起来很困难。

题目给出了有钱人之间的对比，在richer中第一个数字的人比第二个数字的人有钱。quiet值代表每个人的安静指数，数字越大代表越吵。

我们要做的是，找出对于每个人，比他有钱的人还比他安静是谁。

真不知道这个题目设定有啥意义。

## 解题方法

因为这个题设计到一连串的比较，这种题一般都是使用dfs解决。这个题先使用dict保存比每个人有钱的人list。

然后对每个人都去遍历比他有钱的人，对于比他有钱的人继续遍历比他更有钱的人……

下面的代码，

res[i]代表比i有钱还比i安静的人的序号。
dfs的含义是找出比i有钱还比i安静的人的序号。

代码如下：

```python
class Solution:
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        m = collections.defaultdict(list)
        for i, j in richer:
            m[j].append(i)
        
        res = [-1] * len(quiet)
        
        def dfs(i):
            if res[i] > 0: return res[i]
            res[i] = i
            for j in m[i]:
                if quiet[res[i]] > quiet[dfs(j)]:
                    res[i] = res[j]
            return res[i]

        for i in range(len(quiet)):
            dfs(i)
        return res
```

参考资料：

https://leetcode.com/problems/loud-and-rich/discuss/137918/C++JavaPython-Concise-DFS

## 日期

2018 年 9 月 8 日 ———— 美好的周末，从刷题开始