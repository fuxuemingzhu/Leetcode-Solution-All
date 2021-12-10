作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/sliding-puzzle/description/

## 题目描述：

On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

Examples 1:

    Input: board = [[1,2,3],[4,0,5]]
    Output: 1
    Explanation: Swap the 0 and the 5 in one move.

Examples 2:

    Input: board = [[1,2,3],[5,4,0]]
    Output: -1
    Explanation: No number of moves will make the board solved.

Examples 3:

    Input: board = [[4,1,2],[5,0,3]]
    Output: 5
    Explanation: 5 is the smallest number of moves that solves the board.
    An example path:
    After move 0: [[4,1,2],[5,0,3]]
    After move 1: [[4,1,2],[0,5,3]]
    After move 2: [[0,1,2],[4,5,3]]
    After move 3: [[1,0,2],[4,5,3]]
    After move 4: [[1,2,0],[4,5,3]]
    After move 5: [[1,2,3],[4,5,0]]
    Input: board = [[3,2,4],[1,5,0]]
    Output: 14

Note:

1. board will be a 2 x 3 array as described above.
1. board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].

## 题目大意

这个就是大家都玩过的滑块游戏，有个0表示空格，每次可以把这个空格和其他的一个相邻的位置进行交换。问最后能不能出现第一排第二排依次是"123450"的结局。如果不能，则返回-1；如果可以，需要返回所需要的最少步数。

## 解题方法

Hard题目真的是一个比一个看起来难，但是只要有充足的经验，能看出这个是考BFS的题目，那么剩下的时间就是套用模板了吧。。

每次移动都相当于得到了一个新的状态，同时记录得到这个状态需要的步数，并把这个状态保存到已经出现过的set里。所以，本题的难点在于使用如果把二维数组和字符串进行转化的问题，代码写的很清楚了，就不详细说了。

需要注意的是，通过二维坐标得到字符串索引的方式是x * cols + y，我觉得应该是常识，可是我第一次没想出来。

Ps，吐槽一句，python的字符画不支持直接指定某个位置的字符，因此这个题里面迫不得已用了几次string和list互转的过程。。

最坏情况下的时间复杂度是O((MN)!)，空间复杂度是O(MN)。M,N代表行列数，这个题分别为2，3.

```python
class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        goal = "123450"
        start = self.board2str(board)
        
        bfs = collections.deque()
        bfs.append((start, 0))
        visited = set()
        visited.add(start)
        
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while bfs:
            path, step = bfs.popleft()
            
            if path == goal:
                return step
            p = path.index("0")
            x, y = p / 3, p % 3
            path = list(path)
            for dir in dirs:
                tx, ty = x + dir[0], y + dir[1]
                if tx < 0 or tx >= 2 or ty < 0 or ty >= 3:
                    continue
                path[tx * 3 + ty], path[x * 3 + y] = path[x * 3 + y], path[tx * 3 + ty]
                pathStr = "".join(path)
                if pathStr not in visited:
                    bfs.append((pathStr, step + 1))
                    visited.add(pathStr)
                path[tx * 3 + ty], path[x * 3 + y] = path[x * 3 + y], path[tx * 3 + ty]
        return -1
    
    def board2str(self, board):
        bstr = ""
        for i in range(2):
            for j in range(3):
                bstr += str(board[i][j])
        return bstr
```

参考资料：

https://www.youtube.com/watch?v=ABSjW0p3wsM

## 日期

2018 年 10 月 1 日 —— 欢度国庆！


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/82917037
