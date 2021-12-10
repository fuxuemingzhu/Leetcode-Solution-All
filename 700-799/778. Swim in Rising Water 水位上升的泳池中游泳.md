作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/swim-in-rising-water/description/

## 题目描述：

On an N x N ``grid``, each square ``grid[i][j]`` represents the elevation at that point ``(i,j)``.

Now rain starts to fall. At time ``t``, the depth of the water everywhere is ``t``. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most ``t``. You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.

You start at the top left square ``(0, 0)``. What is the least time until you can reach the bottom right square ``(N-1, N-1)``?

Example 1:

    Input: [[0,2],[1,3]]
    Output: 3
    Explanation:
    At time 0, you are in grid location (0, 0).
    You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
    
    You cannot reach point (1, 1) until time 3.
    When the depth of water is 3, we can swim anywhere inside the grid.

Example 2:

    Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
    Output: 16
    Explanation:
     0  1  2  3  4
    24 23 22 21  5
    12 13 14 15 16
    11 17 18 19 20
    10  9  8  7  6
    
    The final route is marked in bold.
    We need to wait until time 16 so that (0, 0) and (4, 4) are connected.

Note:

1. 2 <= N <= 50.
1. grid[i][j] is a permutation of [0, ..., N*N - 1].

## 题目大意

在一个 N x N 的坐标方格 grid 中，每一个方格的值 grid[i][j] 表示在位置 (i,j) 的平台高度。

现在开始下雨了。当时间为 t 时，此时雨水导致水池中任意位置的水位为 t 。你可以从一个平台游向四周相邻的任意一个平台，但是前提是此时水位必须同时淹没这两个平台。假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的。当然，在你游泳的时候你必须待在坐标方格里面。

你从坐标方格的左上平台 (0，0) 出发。最少耗时多久你才能到达坐标方格的右下平台 (N-1, N-1)？

## 解题方法
### 并查集

从左上角通往右下角的路径中，消耗的时间肯定是道路上最高的那个格子的高度。对于这种问题，也是像昨天题目一样，当做连通性问题来解决。

判断是否连通常见的办法是：**并查集**。


昨天的每日一题为「1631. 最小体力消耗路径」，它是求从左上角到右下角的所有路径中的最小高度差绝对值，跟本题非常像。建议大家先阅读昨天的题解：1631. 最小体力消耗路径。

今天题目和昨天题目的不同之处：

- 昨天的题目是把相邻的两个格子之间的高度差的绝对值当作了边的权重，**对边排序**，逐渐添加边，看添加到哪个边的时候，起点和终点能连通；
- 今天的题目中，由于不用求高度差，而是求路径上的格子高度的最大值，因此，可以把抽象成为一个边的权重为 0 的无向图，然后**对顶点排序**，逐个添加上每个顶点，看添加到哪个点的时候，起点和终点能连通。



需要注意题目中的一个条件：`grid[i][j]` 是 `[0, ..., N*N - 1]` 的排列。因此图中没有大小相等的顶点。


整体思路是：


1. 先去除图中的所有顶点，然后按照顶点数值的**从小到大**的顺序，依次遍历并添加每个顶点；
1. 在每次遍历的过程中都要比较这个顶点的数值和其周围的 4 个相邻顶点的数值大小，来判断是否需要添加一条边：如果相邻节点的数值更小，说明该相邻顶点之前**已经**添加到图中，因此现在需要建立一条让两个顶点连通的边；如果相邻节点的数值更大，说明该相邻顶点之前**没有**添加到图中，因此不要建立连通的边。
1. 当添加某一个顶点之后，最左上角的顶点和最右下角的顶点连通了，说明该顶点就是所求。



整个流程就如下面的动画所示（该动画来自力扣官方题解，地址：[https://leetcode-cn.com/problems/swim-in-rising-water/solution/shui-wei-shang-sheng-de-yong-chi-zhong-y-862o/](https://leetcode-cn.com/problems/swim-in-rising-water/solution/shui-wei-shang-sheng-de-yong-chi-zhong-y-862o/)）：


![](https://img-blog.csdnimg.cn/img_convert/3db801dd20cb99441f5c6e3592c8b4d5.gif#align=left&display=inline&height=608&margin=[object Object]&name=&originHeight=608&originWidth=1080&size=0&status=done&style=none&width=1080)

### 二分查找 +  DFS

题意是要求我们，找出一个最小的时间t，在t时刻时所有位置的水面的高度都是t，这时能从左上角的位置到达右下角。

既然指定了开始和结束的位置，可以直接使用DFS或者BFS进行搜索。这个题需要做的就是我们在每个时间t的时候，判断我们能否找到一个有效的路径，如果使用dfs搜索的话，需要判断两个格子的水位相等才行，因为只有海拔相等的情况下，才能保证游过去。因为每个格子自身都有个海拔，所以判断当前高度的方法其实是时刻与自身海拔的最大值。

为了加快搜索，使用了二分查找，题目已经说了所有的数字0～N*N-1之间，每次做二分的时候都要完整的做一次DFS，还好题目规模不大。

时间复杂度是`O(N^2*log(N))`，空间复杂度是`O(N^2)`。

```python
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        left, right = 0, n * n - 1
        while left <= right:
            mid = left + (right - left) / 2
            if self.dfs([[False] * n for _ in range(n)], grid, mid, n, 0, 0):
                right = mid - 1
            else:
                left = mid + 1
        return left
        
    def dfs(self, visited, grid, mid, n, i, j):
        visited[i][j] = True
        if i == n - 1 and j == n - 1:
            return True
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for dir in directions:
            x, y = i + dir[0], j + dir[1]
            if x < 0 or x >= n or y < 0 or y >= n or visited[x][y] or max(mid, grid[i][j]) != max(mid, grid[x][y]):
                continue
            if self.dfs(visited, grid, mid, n, x, y):
                return True
        return False
```

### 优先级队列改进的 BFS

这个思路是，从左上角通往右下角的路径中，瓶颈是哪个呢？肯定是那个必经的道路上有个比较高的。所以，我们只要在做BFS时候，优先走比较矮的路，同时把最高的那个保存下来，就是结果。

```python
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        visited, pq = set((0, 0)), [(grid[0][0], 0, 0)]
        res = 0
        while pq:
            T, i, j = heapq.heappop(pq)
            res = max(res, T)
            directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            if i == j == n - 1:
                break
            for dir in directions:
                x, y = i + dir[0], j + dir[1]
                if x < 0 or x >= n or y < 0 or y >= n or (x, y) in visited:
                    continue
                heapq.heappush(pq, (grid[x][y], x, y))
                visited.add((x, y))
        return res
```

参考资料：

https://leetcode.com/problems/swim-in-rising-water/discuss/113770/Easy-and-Concise-Solution-using-PriorityQueue-PythonC++
https://blog.csdn.net/u014688145/article/details/79254332

## 日期

2018 年 10 月 2 日 —— 小蓝单车莫名其妙收了我1块钱，明明每个月免费骑10次的啊！
2021 年 1 月 31 日 —— 2021已经过了1/12，今天公众号发题晚了，阅读量比较低。


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/82917037
