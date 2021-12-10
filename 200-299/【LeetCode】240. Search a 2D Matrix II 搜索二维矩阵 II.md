
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/search-a-2d-matrix/description/

## 题目描述

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

1. Integers in each row are sorted in ascending from left to right.
1. Integers in each column are sorted in ascending from top to bottom.

Example:

Consider the following matrix:

	[
	  [1,   4,  7, 11, 15],
	  [2,   5,  8, 12, 19],
	  [3,   6,  9, 16, 22],
	  [10, 13, 14, 17, 24],
	  [18, 21, 23, 26, 30]
	]

Given target = 5, return true.

Given target = 20, return false.
    
## 题目大意

怪我理解能力太差？谁告诉我和[74. Search a 2D Matrix][1]的区别？

给出了有规则的二维矩阵，规则是从左向右依次递增，从上向下依次递增。进行查找。

## 解题方法

和[74. Search a 2D Matrix][1]完全一样的代码就A了。。我都蒙的。

下面是解释。

这个题在剑指offer的38-40页有详细解释。方法是从右上角向左下角进行遍历，根据比较的大小决定向下还是向左查找。

剑指offer的解释是我们从矩阵的左下角或者右上角开始遍历，这样知道了比较的结果是大还是小，就知道了对应的前进方向。

Python代码：

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

C++代码如下：

```cpp
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.size() == 0 || matrix[0].size() == 0) return false;
        const int M = matrix.size(), N = matrix[0].size();
        int i = M - 1, j = 0;
        while (i >= 0 && j < N) {
            if (matrix[i][j] == target) {
                return true;
            } else if (matrix[i][j] < target) {
                ++j;
            } else {
                --i;
            }
        }
        return false;
    }
};
```

方法二：

暴力解法遍历，这也能过。。我实在看不懂leetcode了。。

```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        return any(target in row for row in matrix)
```

## 日期

2018 年 3 月 6 日 
2019 年 1 月 7 日 —— 新的一周开始啦啦啊

  [1]: http://blog.csdn.net/fuxuemingzhu/article/details/79459200
