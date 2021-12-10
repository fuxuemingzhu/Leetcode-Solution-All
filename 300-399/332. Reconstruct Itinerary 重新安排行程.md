作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/reconstruct-itinerary/description/


## 题目描述

Given a list of airline tickets represented by pairs of departure and arrival airports ``[from, to]``, reconstruct the itinerary in order. All of the tickets belong to a man who departs from ``JFK``. Thus, the itinerary must begin with ``JFK``.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ``["JFK", "LGA"]`` has a smaller lexical order than ``["JFK", "LGB"]``.
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.

Example 1:

    Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Example 2:

    Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
    Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
                 But it is larger in lexical order.


## 题目大意

重新安排行程，使得给出的所有航班都得经过一次。如果出现多条可行的路径，那么优先选择的字典序最小的航班路径。出发点一定是JFK，而且题目保证了最少有一个可行的遍历路径。

## 解题方法

### 后序遍历

感觉是我自己太菜鸡了，看到花花神一般的解法，感觉自己永远不可能想出来的。

这道题的本质是计算一个最"小"的欧拉路径(Eulerian path)。对于一个节点（当然先从JFK开始)，贪心地访问最小的邻居，访问过的边全部删除。当碰到死路的时候就回溯到最近一个还有出路的节点，然后把回溯的路径放到最后去访问，这个过程和后序遍历的一样。1. 如果子节点没有死路（每个节点都只左子树），前序遍历便是欧拉路径。2. 如果子节点1是死路，子节点2完成了遍历，那么子节点2先要被访问。1，2都和后序遍历的顺序正好相反。

其中，如果碰到死路，而没有把所有的边都走过一遍的话，就说明这种走法不满足itinerary，需要沿着树根向上找到最近的一个有其他路可以走的节点N，把新的路走一遍。因为题目保证一定存在一条满足要求的itinerary路径，那么一条这样的死路，一定会相对的在这个节点N上存在另一条路，这条路存在一个回到该节点N的环。先把这个环走过之后再去走这条死路，就可以保证把以N为树根的这个路径上的所有点都走到。

首先肯定是要把路径保存成链表法表示的图的。然后对每个顶点的所有邻接顶点进行排序，这样我们每次都优先选择字典序最小的那个顶点作为下次遍历的节点。我们做了后序遍历即可。最后还要把后序遍历的结果再翻转，才是从根节点出发到每个位置的路径。

![此处输入图片的描述][1]

![此处输入图片的描述][2]

最坏时间复杂度是O(VlogV)，空间复杂度是O(E).

```python
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = collections.defaultdict(list)
        for frm, to in tickets:
            graph[frm].append(to)
        for frm, tos in graph.items():
            tos.sort(reverse=True)
        res = []
        self.dfs(graph, "JFK", res)
        return res[::-1]

    def dfs(self, graph, source, res):
        while graph[source]:
            v = graph[source].pop()
            self.dfs(graph, v, res)
        res.append(source)
```


## 相似题目


## 参考资料

https://www.youtube.com/watch?v=4udFSOWQpdg

## 日期

2018 年 10 月 30 日 —— 啊，十月过完了


  [1]: https://zxi.mytechroad.com/blog/wp-content/uploads/2017/09/332-ep52-2.png
  [2]: https://zxi.mytechroad.com/blog/wp-content/uploads/2017/09/332-ep52-3.png
