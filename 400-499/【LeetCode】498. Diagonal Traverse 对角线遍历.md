# 【LeetCode】498. Diagonal Traverse 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/diagonal-traverse/description/

## 题目描述：

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:
    
    Input:
    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
    Output:  [1,2,4,7,5,3,6,8,9]

Explanation:

![此处输入图片的描述][1]

Note:

1. The total number of elements of the given matrix will not exceed 10,000.

## 题目大意

沿着对角线遍历矩阵，返回结果。

## 解题方法

这个题做的时候想看别人怎么解答的，因为考察的就是细心嘛……但还是忍住了，坚持自己写完了。

做法很简单，有两个方向：向右上↗，向左下↙。

然后判断当出界了的时候，下一步应该向哪个方向走就行。因为矩阵的行列对称性，写出来的if语句肯定是对称的。这个可以方便自己写代码以及查错。

代码如下：

```python
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]: return []
        directions = [(-1, 1), (1, -1)]
        count = 0
        res = []
        i, j = 0, 0
        M, N = len(matrix), len(matrix[0])
        while len(res) < M * N:
            if 0 <= i < M and 0 <= j < N:
                res.append(matrix[i][j])
                direct = directions[count % 2]
                i, j = i + direct[0], j + direct[1]
                continue
            elif i < 0 and 0 <= j < N:
                i += 1
            elif 0 <= i < M and j < 0:
                j += 1
            elif i < M and j >= N:
                i += 2
                j -= 1
            elif i >= M and j < N:
                j += 2
                i -= 1
            count += 1
        return res
```


## 日期

2018 年 9 月 8 日 ———— 美好的周末，从刷题开始


  [1]: https://leetcode.com/static/images/problemset/diagonal_traverse.png
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/82390672