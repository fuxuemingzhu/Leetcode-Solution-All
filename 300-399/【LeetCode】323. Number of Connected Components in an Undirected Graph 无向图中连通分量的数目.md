- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode-cn.com/problems/number-of-connected-components-in-an-undirected-graph/

## 题目描述

Given `n` nodes labeled from `0` to `n - 1` and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:

    Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
    
         0          3
         |          |
         1 --- 2    4 
    
    Output: 2

Example 2:

    Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    
         0           4
         |           |
         1 --- 2 --- 3
    
    Output:  1

Note:

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, `[0, 1]` is the same as `[1, 0]` and thus will not appear together in edges.


## 题目大意

给定编号从 0 到 n-1 的 n 个节点和一个无向边列表（每条边都是一对节点），请编写一个函数来计算无向图中连通分量的数目。

## 解题方法

### 并查集

看到求联通分量的题，一般都可以用并查集。比如[1101. The Earliest Moment When Everyone Become Friends][1]。

只要把并查集背下来，这个题目基本直接写上去就好了。

C++代码如下：

```cpp
class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        map_ = vector<int>(n, 0);
        components = n;
        for (int i = 0; i < n; ++i) {
            map_[i] = i;
        }
        for (vector<int>& edge : edges) {
            uni(edge[0], edge[1]);
        }
        return components;
    }
    int find(int a) {
        if (a == map_[a])
            return a;
        return find(map_[a]);
    }
    void uni(int a, int b) {
        int pa = find(a);
        int pb = find(b);
        if (pa == pb)
            return;
        map_[pa] = pb;
        components --;
    }
private:
    vector<int> map_;
    int components;
};
```

## 日期

2019 年 9 月 22 日 —— 熬夜废掉半条命


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/101121394
