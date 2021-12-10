
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/all-paths-from-source-to-target/description/

## 题目描述

Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

Example:

    Input: [[1,2], [3], [3], []] 
    Output: [[0,1,3],[0,2,3]] 
    
    Explanation: The graph looks like this:
    
    0--->1
    |    |
    v    v
    2--->3
    
    There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Note:

 - The number of nodes in the graph will be in the range [2, 15].
 - You can print different paths in any order, but you should keep the order of nodes inside one path.

    
## 题目大意

给出了一个有向无环图，求从起点到终点的所有路径。图的表示方法是，共有n个节点，其数字分别为0...n-1，给出的图graph的每个位置对应的是第i个节点能到达的下一个节点的序号位置。比如题中graph[0] = [1,2]表示图的起点0指向了1,2两个节点。


## 解题方法

### 回溯法

经典的dfs的题目啊，第一遍没做这个题的原因是没看懂题目。。

直接使用dfs的模板公式即可，要注意的是给出的path默认就带着起点0，每次添加的是下个节点n不是当前节点pos。停止的条件是 pos == len(graph) - 1。

代码：

```python
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(graph, res, 0, [0])
        return res
        
    
    def dfs(self, graph, res, pos, path):
        if pos == len(graph) - 1:
            res.append(path)
            return
        else:
            for n in graph[pos]:
                self.dfs(graph, res, n, path + [n])
```

二刷的时候对这个题写法更简单了，因为题目给出的是有向无环图，到达根节点之后可以继续搜索，但是不可能再次到达终点了。

```python
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(graph, 0, len(graph) - 1, res, [0])
        return res

    def dfs(self, graph, start, end, res, path):
        if start == end:
            res.append(path)
        for node in graph[start]:
            self.dfs(graph, node, end, res, path + [node])
```

在Python代码里面可以随便就生成了新的列表，导致回溯过程看不清楚，但是C++版本的回溯法因为只用了一个res和一个path，所以回溯过程看的很清楚。

```cpp
class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<int> path;
        path.push_back(0);
        dfs(graph, 0, graph.size() - 1, path);
        return res;
    }   
private:
    vector<vector<int>> res;
    void dfs(vector<vector<int>>& graph, int start, int end, vector<int> path) {
        if (start == end) {
            res.push_back(path);
        } else {
            for (int node : graph[start]) {
                path.push_back(node);
                dfs(graph, node, end, path);
                path.pop_back();
            }
        }
    }
};
```

## 日期

2018 年 3 月 20 日 ————阳光明媚～
2018 年 12 月 2 日 —— 又到了周日
