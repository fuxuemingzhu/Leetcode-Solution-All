
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/spiral-matrix-iii/description/

## 题目描述

On a 2 dimensional grid with R rows and C columns, we start at (r0, c0) facing east.

Here, the north-west corner of the grid is at the first row and column, and the south-east corner of the grid is at the last row and column.

Now, we walk in a clockwise spiral shape to visit every position in this grid. 

Whenever we would move outside the boundary of the grid, we continue our walk outside the grid (but may return to the grid boundary later.) 

Eventually, we reach all R * C spaces of the grid.

Return a list of coordinates representing the positions of the grid in the order they were visited.

 

Example 1:
    
    Input: R = 1, C = 4, r0 = 0, c0 = 0
    Output: [[0,0],[0,1],[0,2],[0,3]]

![此处输入图片的描述][1]
 
Example 2:

    Input: R = 5, C = 6, r0 = 1, c0 = 4
    Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]

 ![此处输入图片的描述][2]

Note:

1. 1 <= R <= 100
1. 1 <= C <= 100
1. 0 <= r0 < R
1. 0 <= c0 < C


## 题目大意

按照顺时针顺序，把一个矩阵的每个位置遍历一遍。遍历时，圈子越来越大，不能走已经走过了的节点。而且，如果走到了矩阵的外边，那么依然可以走。返回的结果是遍历矩阵节点时的顺序。

## 解题方法

这个题目和普通的矩阵遍历的区别就是，它可以走到矩阵的外边。但这也降低了难度。

既然如此，那么我们就完全可以直接按照自己的步骤去走就行，当走到矩阵内部的时候，才去添加到结果之中。

所以，使用了一个生成器，每次就生成下一步走到哪了，不考虑外界条件。然后调用这个生成器，判断是否在矩阵之中并且是否所有的位置都已经遍历了。

代码如下：

```python
class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        def nxt(r, c):
            step = 1
            yield (r, c)
            while True:
                for _ in range(step):
                    c += 1
                    yield (r, c)
                for _ in range(step):
                    r += 1
                    yield (r, c)
                step += 1
                for _ in range(step):
                    c -= 1
                    yield (r, c)
                for _ in range(step):
                    r -= 1
                    yield (r, c)
                step += 1
        ans = []
        for r, c in nxt(r0, c0):
            if 0 <= r < R and 0 <= c < C:
                ans.append([r, c])
            if len(ans) == R * C:
                break
        return ans
```

C++代码如下：

```cpp
class Solution {
public:
    vector<vector<int>> spiralMatrixIII(int R, int C, int r0, int c0) {
        vector<vector<int>> res;
        int dx = 0, dy = 1;
        int step = 1;
        int count = 1;
        res.push_back(vector<int>{r0, c0});
        while (count < R * C) {
            dx = 0, dy = 1;
            for (int s = 0; s < step; s++) {
                r0 += dx;
                c0 += dy;
                if (r0 >= 0 && r0 < R && c0 >= 0 && c0 < C) {
                    res.push_back(vector<int>{r0, c0});
                    count ++;
                    if (count >= R * C) return res;
                }
            }
            dx = 1, dy = 0;
            for (int s = 0; s < step; s++) {
                r0 += dx;
                c0 += dy;
                if (r0 >= 0 && r0 < R && c0 >= 0 && c0 < C) {
                    res.push_back(vector<int>{r0, c0});
                    count ++;
                    if (count >= R * C) return res;
                }
            }
            step ++;
            dx = 0, dy = -1;
            for (int s = 0; s < step; s++) {
                r0 += dx;
                c0 += dy;
                if (r0 >= 0 && r0 < R && c0 >= 0 && c0 < C) {
                    res.push_back(vector<int>{r0, c0});
                    count ++;
                    if (count >= R * C) return res;
                }
            }
            dx = -1, dy = 0;
            for (int s = 0; s < step; s++) {
                r0 += dx;
                c0 += dy;
                if (r0 >= 0 && r0 < R && c0 >= 0 && c0 < C) {
                    res.push_back(vector<int>{r0, c0});
                    count ++;
                    if (count >= R * C) return res;
                }
            }
            step ++;
        }
        return res;
    }
};
```

参考资料：

https://leetcode.com/problems/spiral-matrix-iii/discuss/158995/python-infinite-generator-(yield)

## 日期

2018 年 9 月 4 日 —— 迎接明媚的阳光！
2018 年 12 月 4 日 —— 周二啦！

  [1]: https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/24/example_1.png
  [2]: https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/24/example_2.png
