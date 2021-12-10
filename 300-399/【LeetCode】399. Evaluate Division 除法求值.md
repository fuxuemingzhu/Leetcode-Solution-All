
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/delete-and-earn/description/

## 题目描述

Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
    
    Given a / b = 2.0, b / c = 3.0. 
    queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
    return [6.0, 0.5, -1.0, 1.0, -1.0 ].

 The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.



According to the example above:

    equations = [ ["a", "b"], ["b", "c"] ],
    values = [2.0, 3.0],
    queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.


## 题目大意

已经给出了某些变量的比值，求新的变量的比值。如果这个变量没有出现过，或者不可到达，那么返回-1.

## 解题方法

这个题其实是一个带权有向图。

题目中给了顶点和顶点之间的关系，其实就是绘制了这个图。然后要求的新的比值其实就是从一个顶点到达另外一个顶点的路径，并且把这条路径上所有的权重相乘。

注意，如果a/b=3，那么从a到b是3，那么从b到a是1/3.

既然是从一个顶点出发到达另外一个顶点，所以应该是dfs解决的问题。

为了防止在DFS中走已经走过了的路，所以需要使用visited保存每次已经访问过的节点。


Python代码如下：

```python
class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        table = collections.defaultdict(dict)
        for (x, y), value in zip(equations, values):
            table[x][y] = value
            table[y][x] = 1.0 / value
        ans = [self.dfs(x, y, table, set()) if x in table and y in table else -1.0 for (x, y) in queries]
        return ans
        
    def dfs(self, x, y, table, visited):
        if x == y:
            return 1.0
        visited.add(x)
        for n in table[x]:
            if n in visited: continue
            visited.add(n)
            d = self.dfs(n, y, table, visited)
            if d > 0:
                return d * table[x][n]
        return -1.0
```


方法二：

并查集。留给二刷。

参考资料：

https://www.youtube.com/watch?v=UwpvInpgFmo
https://zxi.mytechroad.com/blog/graph/leetcode-399-evaluate-division/

## 日期

2018 年 9 月 10 日 —— 教师节快乐~
2019 年 3 月 16 日 —— 周末加油～

  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/51291936
