
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/set-matrix-zeroes/description/

## 题目描述

Given a ``m x n`` matrix, if an element is 0, set its entire row and column to 0. Do it ``in-place``.

Example 1:

    Input: 
    [
      [1,1,1],
      [1,0,1],
      [1,1,1]
    ]
    
    Output: 
    [
      [1,0,1],
      [0,0,0],
      [1,0,1]
    ]

Example 2:

    Input: 
    [
      [0,1,2,0],
      [3,4,5,2],
      [1,3,1,5]
    ]
    
    Output: 
    [
      [0,0,0,0],
      [0,4,5,0],
      [0,3,1,0]
    ]

Follow up:

1. A straight forward solution using O(mn) space is probably a bad idea.
1. A simple improvement uses O(m + n) space, but still not the best solution.
1. Could you devise a constant space solution?



## 题目大意

有一个二维矩阵，如果某一个位置出现了0，那么这个0所在的行和列全部转化成0. 原地操作。

## 解题方法

### 原地操作

最简单的方法就是用一个新的二维矩阵保存每个位置的结果，最后再放回原地了，题目说了这样不好。

一个简单的优化是，只需要保存每行和每列是否应该置为0，这样用了O(m+n)的空间，但是还有更好的解法。

我想了一个不用额外空间的，暴力的解法。时间上也勉强通过了。。

这个题和[289. Game of Life][1]比较像，289题只用判断8-连通，而这个题需要判断一整行。

我使用的方法是将每个位置的元素的二进制再增加一位，也就是说在末尾补上一个0或者1代表这个是否应该变成0或者不变。如果经过遍历之后，发现最后一位是0，那么把这个位置的数字变成0，如果最后一位是1，那么把这个位置的数字还原成原来的数字（右移一位）。

由于每个数字记录它的状态是在原地进行的，所以我说没有用到额外的空间。但这个题不好的地方在于，第一，没有说出MN的范围，让我很难判断这个解法能否通过；第二，没有说出matrix[m][n]的范围，不能判断左移一位之后，整数是否溢出（Python不存在这个问题）。

时间复杂度是O((M*N) * (M + N))，空间复杂度是O(1).

时间复杂度有``(M + N)``是因为，对于每个位置都去把这个行、列的所有数值进行了遍历来判断是否存在0，其实可以通过把结果保存到这个行列的第一个位置即可，降低了判断的时间复杂度。

代码如下：

```python
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        M, N = len(matrix), len(matrix[0])
        # (old + new)
        if matrix and matrix[0]:
            for m in range(M):
                for n in range(N):
                    matrix[m][n] = (matrix[m][n] << 1) + (1 if matrix[m][n] else 0)
            for m in range(M):
                for n in range(N):
                    if self.getPos(matrix, m, n) == 0:
                        matrix[m][n] = matrix[m][n] >> 1 << 1
            for m in range(M):
                for n in range(N):
                    if matrix[m][n] & 1 == 0:
                        matrix[m][n] = 0
                    else:
                        matrix[m][n] >>= 1
            
        
    def getPos(self, matrix, m, n): 
        # return 0 means this place ==> 0; 1 ==> don't change
        if matrix[m][n] == 0:
            return 0
        M, N = len(matrix), len(matrix[0])
        if any((matrix[m][i] >> 1) == 0 for i in range(N)):
            return 0
        if any((matrix[i][n] >> 1) == 0 for i in range(M)):
            return 0
        return 1
```

这个解法本身是有问题的，如果左移超出INT最大值的时候。比如C++这个方法就过不了。测试用例果然有个INT最大值，这样左移就超出范围了，下面解法是错的。

```cpp
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        if (matrix.size() == 0 || matrix[0].size() == 0) return;
        const int M = matrix.size(), N = matrix[0].size();
        for (int i = 0; i < M; ++i) {
            for (int j = 0; j < N; ++j) {
                if (matrix[i][j] != 0)
                    matrix[i][j] = 1 + (matrix[i][j] << 1);
            }
        }
        for (int r = 0; r < M; ++r) {
            for (int c = 0; c < N; ++c) {
                if (matrix[r][c] == 0) {
                     for (int j = 0; j < N; ++j) {
                        matrix[r][j] >>= 1;
                        matrix[r][j] <<= 1;
                    }
                    for (int i = 0; i < M; ++i) {
                        matrix[i][c] >>= 1;
                        matrix[i][c] <<= 1;
                    }
                }
            }
        }
        for (int i = 0; i < M; ++i) {
            for (int j = 0; j < N; ++j) {
                if ((matrix[i][j] & 1) == 1) {
                    matrix[i][j] >>= 1;
                } else {
                    matrix[i][j] = 0;
                }
            }
        }
    }
};
```

### 新建数组

如果使用新的数组，把老数组拷贝一份，那么就可以在原数组上进行判断，在新数组上进行修改，也就是题目说的O(MN)的空间复杂度。

```cpp
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        if (matrix.size() == 0 || matrix[0].size() == 0) return;
        vector<vector<int>> newM(matrix);
        const int M = matrix.size(), N = matrix[0].size();
        for (int r = 0; r < M; ++r) {
            for (int c = 0; c < N; ++c) {
                if (newM[r][c] == 0) {
                    for (int j = 0; j < N; ++j) {
                        matrix[r][j] = 0;
                    }
                    for (int i = 0; i < M; ++i) {
                        matrix[i][c] = 0;
                    }
                }
            }
        }
    }
};
```

### 队列

使用一个队列保存出现过0的位置，然后就可以再次遍历把所有的位置设置为0了。这里也可以使用其他的数据结构。

```cpp
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        if (matrix.size() == 0 || matrix[0].size() == 0) return;
        const int M = matrix.size(), N = matrix[0].size();
        queue<pair<int, int>> q;
        for (int r = 0; r < M; ++r) {
            for (int c = 0; c < N; ++c) {
                if (matrix[r][c] == 0) {
                    q.push({r, c});
                }
            }
        }
        while (!q.empty()) {
            auto p = q.front(); q.pop();
            for (int j = 0; j < N; ++j) {
                matrix[p.first][j] = 0;
            }
            for (int i = 0; i < M; ++i) {
                matrix[i][p.second] = 0;
            }
        }
    }
};
```

参考资料：


## 日期

2018 年 9 月 26 日 —— 美好的一周又快要过去了。。
2018 年 12 月 17 日 —— 周一要从早起开始

  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/82809923
