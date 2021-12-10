
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/flower-planting-with-no-adjacent/

## 题目描述

You have `N` gardens, labelled `1` to `N`.  In each garden, you want to plant one of 4 types of flowers.

`paths[i] = [x, y]` describes the existence of a bidirectional path from garden `x` to garden `y`.

Also, there is no garden that has more than 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

Return any such a choice as an array answer, where `answer[i]` is the type of flower planted in the `(i+1)-th` garden.  The flower types are denoted `1, 2, 3, or 4`.  It is guaranteed an answer exists.


Example 1:

    Input: N = 3, paths = [[1,2],[2,3],[3,1]]
    Output: [1,2,3]

Example 2:

    Input: N = 4, paths = [[1,2],[3,4]]
    Output: [1,2,1,2]

Example 3:

    Input: N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
    Output: [1,2,3,4]
 
Note:

1. `1 <= N <= 10000`
1. `0 <= paths.size <= 20000`
1. No garden has 4 or more paths coming into or leaving it.
1. It is guaranteed an answer exists.

## 题目大意

每一个顶点都最多只有3条相邻的边，现在要给每个顶点编号1~4，要求相邻的顶点不能是相同的数字。给出其中任意一种方案。

N表示顶点数，paths表示这两个顶点（编号从1开始）之间有边。

## 解题方法

### 图

这个题目背景虽然是花园，但是我相信大家应该都明白了，其实说的是[四色定理][1]。

既然是个图论的题目，那么就按照图的方法来解。先构建无向图，对于每个顶点检查其所有相邻顶点的编号，这个顶点用一个没有用过的编号，依次类推。题目也已经说了，解一定存在。

由于每个顶点最多只有三条边，所以时间复杂度是O(N)。

Python代码如下：

```python
class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        res = [0] * N
        graph = [[] for i in range(N)]
        for path in paths:
            graph[path[0] - 1].append(path[1] - 1)
            graph[path[1] - 1].append(path[0] - 1)
        for i in range(N):
            neighbor_colors = []
            for neighbor in graph[i]:
                neighbor_colors.append(res[neighbor])
            for color in range(1, 5):
                if color in neighbor_colors:
                    continue
                res[i] = color
                break
        return res
```

C++代码如下：


```cpp
class Solution {
public:
    vector<int> gardenNoAdj(int N, vector<vector<int>>& paths) {
        vector<int> res(N, 0);
        vector<vector<int>> graph(N);
        for (auto& path : paths) {
            graph[path[0] - 1].push_back(path[1] - 1);
            graph[path[1] - 1].push_back(path[0] - 1);
        }
        for (int i = 0; i < N; ++i) {
            unordered_set<int> neighbor_colors;
            for (int neighbor : graph[i]) {
                neighbor_colors.insert(res[neighbor]);
            }
            for (int color = 1; color < 5; ++color) {
                if (neighbor_colors.count(color))
                    continue;
                res[i] = color;
                break;
            }
        }
        return res;
    }
};
```

参考资料：
https://leetcode.com/problems/flower-planting-with-no-adjacent/discuss/308003/Python-Clear-solution-without-one-line-code

## 日期

2019 年 6 月 9 日 —— 简单的题没有难度，需要挑战有难度的才行


  [1]: https://baike.baidu.com/item/%E5%9B%9B%E8%89%B2%E5%AE%9A%E7%90%86/805159?fromtitle=%E5%9B%9B%E8%89%B2%E9%97%AE%E9%A2%98&fromid=752628
