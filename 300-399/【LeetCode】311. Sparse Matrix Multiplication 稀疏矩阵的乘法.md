

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode-cn.com/problems/sparse-matrix-multiplication/

## 题目描述

Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

    Input:

    A = [
      [ 1, 0, 0],
      [-1, 0, 3]
    ]

    B = [
      [ 7, 0, 0 ],
      [ 0, 0, 0 ],
      [ 0, 0, 1 ]
    ]
    
    Output:
    
         |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
    AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                      | 0 0 1 |


## 题目大意

给定两个 稀疏矩阵 A 和 B，请你返回 AB。你可以默认 A 的列数等于 B 的行数。

## 解题方法

### 暴力

直接按照矩阵乘法，可以暴力求解。矩阵乘法是三重循环，时间复杂度是O(N^3)。

![此处输入图片的描述][1]

题目给的系数矩阵的特征怎么用呢？可以考虑先遍历一次两个矩阵，记录下A的行和B的列全部为0的索引，当遍历到这些索引时，直接给res中填入0。下面的代码没有这么做，也能通过。


C++代码如下：

```cpp
class Solution {
public:
    vector<vector<int>> multiply(vector<vector<int>>& A, vector<vector<int>>& B) {
        if (A.empty() || A[0].empty() || B.empty() || B[0].empty()) return vector<vector<int>>();
        int M = A.size();
        int N = B[0].size();
        vector<vector<int>> res(M, vector<int>(N, 0));
        for (int row = 0; row < M; ++row) {
            for (int col = 0; col < N; ++col) {
                int cur = 0;
                for (int i = 0; i < A[0].size(); ++i) {
                    cur += A[row][i] * B[i][col];
                }
                res[row][col] = cur;
            }
        }
        return res;
    }
};
```

### 科学计算库numpy

Python有科学计算库numpy可以使用，直接使用库函数求得矩阵的乘法。

```python
import numpy as np
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        a = np.array(A)
        b = np.array(B)
        return np.matmul(a, b)
```

## 日期

2019 年 9 月 24 日 —— 梦见回到了小学，小学已经芳草萋萋破败不堪


  [1]: https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1569299800527&di=0791f14b34f5db98eb9acb10fbb908b1&imgtype=0&src=http://gss0.baidu.com/94o3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/1ad5ad6eddc451da41652b3bb0fd5266d116324a.jpg
