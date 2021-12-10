
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/score-after-flipping-matrix/description/

## 题目描述

We have a two dimensional matrix A where each value is 0 or 1.

A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.

After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score.

 

Example 1:

    Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
    Output: 39
    Explanation:
    Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
    0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
 

Note:

- ``1 <= A.length <= 20``
- ``1 <= A[0].length <= 20``
- ``A[i][j] is 0 or 1.``


## 题目大意

题目中给了一个数组A，这个数组中只包含0,1.现在需要整行或者整列的进行toggle操作。目标是进行一波toggle操作之后，把A中的每行数字转化成二进制数，是最终得到的二进制数的和最大。

## 解题方法

题目很烧脑，使用什么样的操作规则才能使得得到的最终数组二进制和最大。

1. 首先，第一列肯定要全部变成1，很显然位数恒定时，1开头的二进制数要比任何0开头的都要大。

1. 其次，我们采取贪心算法，让每一列中1的个数尽可能多。怎么理解这句话呢？

这和我们最终的目标有关，因为我们要求每行数字都转成二进制数之后的``和``，所以，在同一列中，1出现在哪一行对结果一样的。

如果还不明白，看我的分析：

初始状态：

    [0,0,1,1]
    [1,0,1,0]
    [1,1,0,0]

首列置为 1：

    [1,1,0,0]
    [1,0,1,0]
    [1,1,0,0]

每一列 1 的个数大于 0 的个数：

    [1,1,1,1]
    [1,0,0,1]
    [1,1,1,1]

计算结果：15 + 9 + 15 = 39.

其实，最后的计算结果完全可以这么算：

    =     2^3 * 3（第一列有3个1） + 2^2 * 2（第二列有2个1）
        + 2^1 * 2（第三列有2个1） + 2^0 * 3（第四列有3个1）
    = 8*3 + 4*2 + 2*2 + 1*3
    = 24 + 8 + 4 + 3
    = 39

即，我们只关心这一列出现的1的个数，不用关心1出现的位置。

代码如下：

```python
class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        rows, cols = len(A), len(A[0])
        for row in range(rows):
            if A[row][0] == 0:
                A[row] = self.toggle_row(A[row])
        for col in range(1, cols):
            col_array = [A[row][col] for row in range(rows)]
            sum_col_array = sum(col_array)
            if sum_col_array <= rows / 2:
                col_array = self.toggle_col(col_array)
            for row in range(rows):
                A[row][col] = col_array[row]
        bin_row = []
        for row in range(rows):
            bin_row.append(int("".join(map(str, A[row])), 2))
        return sum(bin_row)
                
    def toggle_row(self, row_array):
        return [0 if x == 1 else 1 for x in row_array]
    
    def toggle_col(self, col_array):
        return [0 if x == 1 else 1 for x in col_array]
```

二刷，第一步判断每行的第一个位置是不是0，如果是0那么就把这行全部翻转。第二步，统计每一列有多少个1，计算2的max(count1, count0)次幂。

```python
class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        M, N = len(A), len(A[0])
        for i in range(M):
            if A[i][0] == 0:
                for j in range(N):
                    A[i][j] = 1 - A[i][j]
        res = 0
        for j in range(N):
            count1 = 0
            for i in range(M):
                if A[i][j]:
                    count1 += 1
            res += (1 << N - 1- j) * max(count1, M - count1)
        return res
```

C++代码如下：

```cpp
class Solution {
public:
    int matrixScore(vector<vector<int>> &A) {
        int M = A.size(), N = A[0].size();
        for (int i = 0; i < M; i++)
            if (A[i][0])
                for (int j = 0; j < N; j++)
                    A[i][j] = 1 - A[i][j];
        int res = 0;
        for (int j = 0; j < N; j++) {
            int count1 = 0;
            for (int i = 0; i < M; i++) {
                if (A[i][j]) {
                    count1++;
                }
            }
            res += (1 << (N - 1 - j)) * max(count1, M - count1);
        }
        return res;
    }
};
```

## 日期

2018 年 7 月 19 日 —— 今天主要在忙实验室项目，刷题有点晚了
2018 年 12 月 2 日 —— 又到了周日

