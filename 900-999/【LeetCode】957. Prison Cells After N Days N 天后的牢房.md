
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/prison-cells-after-n-days/description/


## 题目描述


There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

- If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
- Otherwise, it becomes vacant.

(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: ``cells[i] == 1`` if the ``i``-th cell is occupied, else ``cells[i] == 0``.

Given the initial state of the prison, return the state of the prison after ``N`` days (and ``N`` such changes described above.)

 

Example 1:

    Input: cells = [0,1,0,1,1,0,0,1], N = 7
    Output: [0,0,1,1,0,0,0,0]
    Explanation: 
    The following table summarizes the state of the prison on each day:
    Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
    Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
    Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
    Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
    Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
    Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
    Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
    Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:

    Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
    Output: [0,0,1,1,1,1,1,0]
 

Note:

1. cells.length == 8
1. cells[i] is in {0, 1}
1. 1 <= N <= 10^9


## 题目大意

有一个数组，每次操作：如果某个位置i的左边和右边的元素相等，那么当前位置改成1；否则就是0.求N次操作之后的结果是多少。

## 解题方法

### 周期是14

写了一个多小时的题目，后来才发现周期是14.

发现周期的过程就是尝试了一下，不同的数组的循环周期是多少。试了几个之后发现是14，那就是14了。

如果知道是14之后那就好办了，先把N mod 14，然后注意了！如果mod完之后等于0，应该把N设置为14！！最后我是有时间提交通过的，但是这个地方没有想明白，所以比赛结束之后才通过的。

底下的转移方程就很简单了，直接转移。因为最多操作14次，所以很容易就过了。


代码如下：

```python
class Solution(object):
    def prisonAfterNDays(self, oldcells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        cells = copy.deepcopy(oldcells)
        count = 0
        N %= 14
        if N == 0:
            N = 14
        while count < N:
            newCell = [0] * 8
            for i in range(1, 7):
                if cells[i - 1] == cells[i + 1]:
                    newCell[i] = 1
                else:
                    newCell[i] = 0
            cells = newCell
            count += 1
        return cells
```


## 日期

2018 年 12 月 16 日 —— 周赛好难


  [1]: https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-1.png
  [2]: https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-2.png
  [3]: https://zxi.mytechroad.com/blog/wp-content/uploads/2018/12/952-ep232.png
