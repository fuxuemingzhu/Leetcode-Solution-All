作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/cat-and-mouse/description/


## 题目描述

A game on an ``undirected`` graph is played by two players, Mouse and Cat, who alternate turns.

The graph is given as follows: ``graph[a]`` is a list of all nodes ``b`` such that ``ab`` is an edge of the graph.

Mouse starts at node 1 and goes first, Cat starts at node 2 and goes second, and there is a Hole at node 0.

During each player's turn, they **must** travel along one edge of the graph that meets where they are.  For example, if the Mouse is at node ``1``, it ``must`` travel to any node in ``graph[1]``.

Additionally, it is not allowed for the Cat to travel to the Hole (node 0.)

Then, the game can end in 3 ways:

- If ever the Cat occupies the same node as the Mouse, the Cat wins.
- If ever the Mouse reaches the Hole, the Mouse wins.
- If ever a position is repeated (ie. the players are in the same position as a previous turn, and it is the same player's turn to move), the game is a draw.

Given a ``graph``, and assuming both players play optimally, return ``1`` if the game is won by Mouse, ``2`` if the game is won by Cat, and ``0`` if the game is a draw.

 

Example 1:

    Input: [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
    Output: 0
    Explanation:
    4---3---1
    |   |
    2---5
     \ /
      0
 

Note:

1. 3 <= graph.length <= 50
1. It is guaranteed that graph[1] is non-empty.
1. It is guaranteed that graph[2] contains a non-zero element. 

## 题目大意

猫鼠游戏。

有一张无向图，包含最多50个结点。有两个玩家（Mouse和Cat）在图上，Mouse的起始位置是1，Cat的起始位置是2，0处有一个洞，Cat不能移动到0。Mouse和Cat在图上轮流移动，每次必须移动到与当前结点相邻的一个结点。

游戏有三种结束的可能：

1. Cat和Mouse进入同一结点，则Cat胜利
1. Mouse进入0结点，则Mouse胜利
1. Cat和Mouse的位置和回合发生了重复，则平局

问：如果Cat和Mouse都以最优策略行动，最后的结果是什么？

## 解题方法

这个题实在太难了，我只能参考别人的做法了。正确的做法应该是BFS，而且是已知结果倒着求过程的BFS。

设计节点状态是(m,c,turn)，用color[m][c][turn]来记忆该状态的输赢情况．

首先我们将所有已知的确定状态加入一个队列．已知状态包括(0,c,turn)肯定是老鼠赢，(x,x,turn)且x!=0肯定是猫赢。我们尝试用BFS的思路，将这些已知状态向外扩展开去．

扩展的思路是：从队列中取出队首节点状态（m,c,t），找到它的所有邻接的parent的状态（m2,c2,t2）．这里的父子关系是指，(m2,c2,t2)通过t2轮（老鼠或猫）的操作，能得到(m,c,t).我们发现，如果(m,c,t)是老鼠赢而且t2是老鼠轮，那么这个(m2,c2,t2)一定也是老鼠赢．同理，猫赢的状态也类似．于是，我们找到了一种向外扩展的方法．

向外扩展的第二个思路是：对于(m2,c2,t2)，我们再去查询它的所有children（必定是对手轮）是否都已经标注了赢的状态．如果都是赢的状态，那么说明(m2,c2,t2)无路可走，只能标记为输的状态．特别注意的是，第一条规则通过child找parent，和第二条规则通过parent找child的算法细节是不一样的，一定要小心．

这样我们通过BFS不断加入新的探明输赢的节点．直到队列为空，依然没有探明输赢的节点状态，就是平局的意思！

最后输出(1, 2, MOUSE)的颜色。没有被染过色说明是平局。

时间复杂度是O(VE)，空间复杂度是O(V).

```python
class Solution(object):
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        N = len(graph)
        MOUSE, CAT = 1, 2
        # mouse, cat, turn
        color = [[[0] * 3 for i in range(N)] for j in range(N)]
        q = collections.deque()
        for i in range(1, N):
            for t in range(1, 3):
                color[0][i][t] = 1
                q.append((0, i, t))
                color[i][i][t] = 2
                q.append((i, i, t))
        while q:
            curStatus = q.popleft()
            cat, mouse, turn = curStatus
            for preStatus in self.findAllPrevStatus(graph, curStatus):
                preCat, preMouse, preTurn = preStatus
                if color[preCat][preMouse][preTurn] != 0:
                    continue
                if color[cat][mouse][turn] == 3 - turn:
                    color[preCat][preMouse][preTurn] = preTurn
                    q.append(preStatus)
                elif self.allNeighboursWin(color, graph, preStatus):
                    color[preCat][preMouse][preTurn] = 3 - preTurn
                    q.append(preStatus)
        return color[1][2][1]
    
    def findAllPrevStatus(self, graph, curStatus):
        ret = []
        mouse, cat, turn = curStatus
        if turn == 1:
            for preCat in graph[cat]:
                if preCat == 0:
                    continue
                ret.append((mouse, preCat, 2))
        else:
            for preMouse in graph[mouse]:
                ret.append((preMouse, cat, 1))
        return ret
    
    def allNeighboursWin(self, color, graph, status):
        mouse, cat, turn = status
        if turn == 1:
            for nextMouse in graph[mouse]:
                if color[nextMouse][cat][2] != 2:
                    return False
        elif turn == 2:
            for nextCat in graph[cat]:
                if nextCat == 0:
                    continue
                if color[mouse][nextCat][1] != 1:
                    return False
        return True
```

## 参考资料

https://zhanghuimeng.github.io/post/leetcode-913-cat-and-mouse/
https://github.com/wisdompeak/LeetCode/tree/master/BFS/913.Cat-and-Mouse

## 日期

2018 年 10 月 24 日 —— 程序员节被严重炒作了啊
