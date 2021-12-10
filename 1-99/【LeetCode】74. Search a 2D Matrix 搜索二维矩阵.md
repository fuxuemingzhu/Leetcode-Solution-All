
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/search-a-2d-matrix/description/

## 题目描述

Write an efficient algorithm that searches for a value in an ``m x n`` matrix. This matrix has the following properties:

1. Integers in each row are sorted from left to right.
1. The first integer of each row is greater than the last integer of the previous row.

Example 1:

	Input:
	matrix = [
	  [1,   3,  5,  7],
	  [10, 11, 16, 20],
	  [23, 30, 34, 50]
	]
	target = 3
	Output: true

Example 2:

	Input:
	matrix = [
	  [1,   3,  5,  7],
	  [10, 11, 16, 20],
	  [23, 30, 34, 50]
	]
	target = 13
	Output: false

## 题目大意

给出了有规则的二维矩阵，规则是从左向右依次递增，每行的起始元素比上一行的最后一个元素大。进行查找。

## 解题方法

### 左下或者右上开始查找

这个题目是[240. Search a 2D Matrix II](https://blog.csdn.net/fuxuemingzhu/article/details/79459314)的一个特例，所以可以直接使用240题的代码就能通过。方法是从矩阵的左下角或者右上角开始遍历。

这个题在剑指offer的38-40页有详细解释。方法是从右上角向左下角进行遍历，根据比较的大小决定向下还是向左查找。

代码：

```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        row, col = 0, cols - 1
        while True:
            if row < rows and col >= 0:
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] < target:
                    row += 1
                else:
                    col -= 1
            else:
                return False
```

### 顺序查找

我想这个题目要考察的并不是上面这个方法，而是一个更简单的方法，即顺序查找。我们从第一行开始向下面进行查找，如果这行的末尾元素比当前要查找的元素大，那么说明要查找的元素就在这行里。在这行里查找元素很简单啦，就不多少了。

C++代码如下：

```cpp
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.size() == 0 || matrix[0].size() == 0) return false;
        const int M = matrix.size(), N = matrix[0].size();
        for (int i = 0; i < M; ++i) {
            if (target > matrix[i][N - 1])
                continue;
            auto it = find(matrix[i].begin(), matrix[i].end(), target);
            return it != matrix[i].end();
        }
        return false;
    }
};
```

受到上面的解法启发，我们可以直接遍历每一个位置进行查找啊！怎么做？矩阵的顺序遍历只需要一个变量i表示位置即可，matrix[i/N][i%N]即为当前遍历到的元素。

这个做法的C++代码如下：

```cpp
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.size() == 0 || matrix[0].size() == 0) return false;
        const int M = matrix.size(), N = matrix[0].size();
        int i = 0;
        while (i < M * N) {
            if (matrix[i / N][i % N] == target)
                return true;
            ++i;
        }
        return false;
    }
};
```


### 库函数

使用库函数也可以哦，不过库函数都是针对一维数组的查找，所以我们需要把给出的数组变成一维的。在numpy中有reshape函数，幸运的是，leetcode支持Numpy.

python代码如下：

```python
import numpy as np
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        matrix = np.reshape(matrix, [1, -1])
        return target in matrix
```

## 日期

2018 年 3 月 6 日 
2019 年 1 月 7 日 —— 新的一周开始啦啦啊
