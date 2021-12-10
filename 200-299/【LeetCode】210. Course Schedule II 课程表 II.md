作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/course-schedule-ii/description/

## 题目描述

There are a total of n courses you have to take, labeled from ``0`` to ``n-1``.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: ``[0,1]``

Given the total number of courses and a list of prerequisite **pairs**, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

    Input: 2, [[1,0]] 
    Output: [0,1]
    Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
                 course 0. So the correct course order is [0,1].

Example 2:

    Input: 4, [[1,0],[2,0],[3,1],[3,2]]
    Output: [0,1,2,3] or [0,2,1,3]
    Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
                 courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
                 So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .

Note:

1. The input prerequisites is a graph represented by **a list of edges**, not adjacency matrices. Read more about how a graph is represented.
1. You may assume that there are no duplicate edges in the input prerequisites.


## 题目大意

课程表上有一些课，是必须有修学分的先后顺序的，必须要求在上完某些课的情况下才能上下一门。问是否有方案修完所有的课程？如果有的话请返回其中一个符合要求的路径，否则返回[].

## 解题方法

### 拓扑排序，BFS

这个题是[207. Course Schedule][1]的拓展题目，对拓扑排序提出了更高的要求，即需要打印出拓扑排序的结果，而不只是返回是否是DAG。

看到给的第二个测试用例立马就明白了，就是判断这些课程能否构成有向无环图（DAG）。而任何时候判断DAG的方法要立刻想到拓扑排序。

拓扑排序是对有向无环图（DAG）而言的，对图进行拓扑排序即求其中节点的一个拓扑序列，对于所有的有向边（U, V）（由U指向V），在该序列中节点U都排在节点V之前。

方法是每次选择入度为0的节点，作为序列的下一个节点，然后移除该节点和以从节点出发的所有边。

第一种做法是使用BFS，也是拓扑排序最朴素的思想：每次找到入度为0的节点，把他放到结果里，然后再找第二个入度为0的点等等。

那这个方法比较简单粗暴了：要循环N次，这个循环次数并不是遍历节点的意思，而是我们如果正常取点的话，N次就能把所有的节点都取完了，如果N次操作结束还没判断出来，那么就不是DAG.在这N次中，每次都找一个入度为0的点，并把它的入度变为-1，作为已经取过的点不再使用，同时把从这个点指向的点的入度都-1.

这个过程中，如果找不到入度为0的点，那么说明存在环。如果N次操作，每次都操作成功的去除了一个入度为0的点，那么说明这个图是DAG.

这个做法确实很简洁，只要使用列表Path保存每次入度为0的点，就保存了每次访问的路径。

时间复杂度是O(N ^ 2)，空间复杂度是O(N)。超过了8%的提交。

```python
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)
        for u, v in prerequisites:
            graph[v].append(u)
            indegrees[u] += 1
        path = []
        for i in range(numCourses):
            zeroDegree = False
            for j in range(numCourses):
                if indegrees[j] == 0:
                    zeroDegree = True
                    break
            if not zeroDegree:
                return []
            indegrees[j] -= 1
            path.append(j)
            for node in graph[j]:
                indegrees[node] -= 1
        return path
```

### 拓扑排序，DFS

同样是拓扑排序，但是换了个做法，使用DFS。这个方法是，我们每次找到一个新的点，判断从这个点出发是否有环。

具体做法是使用一个visited数组，当visited[i]值为0，说明还没判断这个点；当visited[i]值为1，说明当前的循环正在判断这个点；当visited[i]值为2，说明已经判断过这个点，含义是从这个点往后的所有路径都没有环，认为这个点是安全的。

那么，我们对每个点出发都做这个判断，检查这个点出发的所有路径上是否有环，如果判断过程中找到了当前的正在判断的路径，说明有环；找到了已经判断正常的点，说明往后都不可能存在环，所以认为当前的节点也是安全的。如果当前点是未知状态，那么先把当前点标记成正在访问状态，然后找后续的节点，直到找到安全的节点为止。最后如果到达了无路可走的状态，说明当前节点是安全的。

findOrder函数中的for循环是怎么回事呢？这个和BFS循环次数不是同一个概念，这里的循环就是看从第i个节点开始能否到达合理结果。这个节点可能没有出度了，那就把它直接放到path里；也可能有出度，那么就把它后面的节点都进行一次遍历，如果满足条件的节点都放到path里，同时把这次遍历的所有节点都标记成了已经遍历；如果一个节点已经被安全的访问过，那么就放过它，继续遍历下个节点。

时间复杂度是O(N)，空间复杂度是O(N)。超过了100%的提交。

```python
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        # 0 = Unknown, 1 = visiting, 2 = visited
        visited = [0] * numCourses
        path = []
        for i in range(numCourses):
            if not self.dfs(graph, visited, i, path):
                return []
        return path
    
    def dfs(self, graph, visited, i, path):
        if visited[i] == 1: return False
        if visited[i] == 2: return True
        visited[i] = 1
        for j in graph[i]:
            if not self.dfs(graph, visited, j, path):
                return False
        visited[i] = 2
        path.append(i)
        return True
```

## 参考资料

https://blog.csdn.net/fuxuemingzhu/article/details/82951771

## 日期

2018 年 10 月 23 日 —— 刮风就是好，天朗气清，惠风和畅了


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/82951771
