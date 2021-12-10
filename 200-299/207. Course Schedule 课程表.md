作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/course-schedule/description/

## 题目描述：

There are a total of n courses you have to take, labeled from ``0`` to ``n-1``.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: ``[0,1]``

Given the total number of courses and a list of prerequisite ``pairs``, is it possible for you to finish all courses?

Example 1:

    Input: 2, [[1,0]] 
    Output: true
    Explanation: There are a total of 2 courses to take. 
                 To take course 1 you should have finished course 0. So it is possible.

Example 2:

    Input: 2, [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take. 
                 To take course 1 you should have finished course 0, and to take course 0 you should
                 also have finished course 1. So it is impossible.

Note:

1. The input prerequisites is a graph represented by ``a list of edges``, not adjacency matrices. Read more about how a graph is represented.
1. You may assume that there are no duplicate edges in the input prerequisites.

## 题目大意

课程表上有一些课，是必须有修学分的先后顺序的，必须要求在上完某些课的情况下才能上下一门。问是否有方案修完所有的课程？


## 解题方法

## 方法一：拓扑排序，BFS

看到给的第二个测试用例立马就明白了，就是判断这些课程能否构成有向无环图（DAG）。而任何时候判断DAG的方法要立刻想到拓扑排序。

拓扑排序是对有向无环图（DAG）而言的，对图进行拓扑排序即求其中节点的一个拓扑序列，对于所有的有向边（U, V）（由U指向V），在该序列中节点U都排在节点V之前。

方法是每次选择入度为0的节点，作为序列的下一个节点，然后移除该节点和以从节点出发的所有边。

那这个方法比较简单粗暴了：要循环N次，这个循环次数并不是遍历节点的意思，而是我们如果正常取点的话，N次就能把所有的节点都取完了，如果N次操作结束还没判断出来，那么就不是DAG.在这N次中，每次都找一个入度为0的点，并把它的入度变为-1，作为已经取过的点不再使用，同时把从这个点指向的点的入度都-1.

这个过程中，如果找不到入度为0的点，那么说明存在环。如果N次操作，每次都操作成功的去除了一个入度为0的点，那么说明这个图是DAG.

时间复杂度是O(N ^ 2)，空间复杂度是O(N)。

```python
class Solution(object):
    def canFinish(self, N, prerequisites):
        """
        :type N,: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)
        for u, v in prerequisites:
            graph[v].append(u)
            indegrees[u] += 1
        for i in range(N):
            zeroDegree = False
            for j in range(N):
                if indegrees[j] == 0:
                    zeroDegree = True
                    break
            if not zeroDegree: return False
            indegrees[j] = -1
            for node in graph[j]:
                indegrees[node] -= 1
        return True                
```


### 方法二：拓扑排序，DFS

同样是拓扑排序，但是换了个做法，使用DFS。这个方法是，我们每次找到一个新的点，判断从这个点出发是否有环。

具体做法是使用一个visited数组，当visited[i]值为0，说明还没判断这个点；当visited[i]值为1，说明当前的循环正在判断这个点；当visited[i]值为2，说明已经判断过这个点，含义是从这个点往后的所有路径都没有环，认为这个点是安全的。

那么，我们对每个点出发都做这个判断，检查这个点出发的所有路径上是否有环，如果判断过程中找到了当前的正在判断的路径，说明有环；找到了已经判断正常的点，说明往后都不可能存在环，所以认为当前的节点也是安全的。如果当前点是未知状态，那么先把当前点标记成正在访问状态，然后找后续的节点，直到找到安全的节点为止。最后如果到达了无路可走的状态，说明当前节点是安全的。

findOrder函数中的for循环是怎么回事呢？这个和BFS循环次数不是同一个概念，这里的循环就是看从第i个节点开始能否到达合理结果。这个节点可能没有出度了，那就把它直接放到path里；也可能有出度，那么就把它后面的节点都进行一次遍历，如果满足条件的节点都放到path里，同时把这次遍历的所有节点都标记成了已经遍历；如果一个节点已经被安全的访问过，那么就放过它，继续遍历下个节点。

时间复杂度是O(N ^ 2)，空间复杂度是O(N)。

```python
class Solution(object):
    def canFinish(self, N, prerequisites):
        """
        :type N,: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        # 0 = Unknown, 1 = visiting, 2 = visited
        visited = [0] * N
        for i in range(N):
            if not self.dfs(graph, visited, i):
                return False
        return True
        
    # Can we add node i to visited successfully?
    def dfs(self, graph, visited, i):
        if visited[i] == 1: return False
        if visited[i] == 2: return True
        visited[i] = 1
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
        visited[i] = 2
        return True
```

参考资料：

https://leetcode.com/problems/course-schedule/discuss/58509/18-22-lines-C++-BFSDFS-Solutions
https://www.youtube.com/watch?v=M6SBePBMznU

## 日期

2018 年 10 月 6 日 —— 努力看书


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/82949743
