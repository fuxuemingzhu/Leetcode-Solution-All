
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/reshape-the-matrix/description/


## 题目描述

In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two ``positive`` integers ``r`` and ``c`` representing the ``row`` number and ``column`` number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same ``row-traversing`` order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:

    Input: 
    nums = 
    [[1,2],
     [3,4]]
    r = 1, c = 4
    Output: 
    [[1,2,3,4]]
    Explanation:
    The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.

Example 2:

    Input: 
    nums = 
    [[1,2],
     [3,4]]
    r = 2, c = 4
    Output: 
    [[1,2],
     [3,4]]
    Explanation:
    There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.

Note:

1. The height and width of the given matrix is in range [1, 100].
1. The given r and c are all positive.


## 题目大意

实现Matlab的reshape函数，就是把原来的数组逐行遍历重新改成r行，c列，如果不能实现的话就是返回原来的数组。

## 解题方法

### 变长数组

Python的list是可变的，那么一个简单的想法就是使用可变的List作为新的一行，如果新的一行的元素个数等于题目要求的列数，那么就新建一行。把每行的结果放到返回的列表中即可。

时间复杂度是O(mn)，空间复杂度是O(1).没有额外空间

```python
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        M, N = len(nums), len(nums[0])
        if M * N != r * c:
            return nums
        res = []
        row = []
        for i in range(M):
            for j in range(N):
                row.append(nums[i][j])
                if len(row) == c:
                    res.append(row)
                    row = []
        return res
```

### 求余法

这个做法是由位图法激发出来的，使用一个变量count保存现在已经有了的元素数量，那么直接可以使用``res[count / c][count % c]``确定轮到了的元素的位置。这个方法需要把数组提前构造好。

时间复杂度是O(mn)，空间复杂度是O(1).没有额外空间

```python
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        M, N = len(nums), len(nums[0])
        if M * N != r * c:
            return nums
        res = [[0] * c for _ in range(r)]
        count = 0
        for i in range(M):
            for j in range(N):
                res[count / c][count % c] = nums[i][j]
                count +=1
        return res
```

### 维护行列

上面的方法每次需要通过除法和求余来确定新的位置，事实上是比较耗时的。更快的方法就是维护行和列的变量，在遍历的过程中更新行和列，这样就可以对应放入的位置了。

时间复杂度是O(mn)，空间复杂度是O(1).没有额外空间

```python
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        M, N = len(nums), len(nums[0])
        if M * N != r * c:
            return nums
        res = [[0] * c for _ in range(r)]
        row, col = 0, 0
        for i in range(M):
            for j in range(N):
                if col == c:
                    row += 1
                    col = 0
                res[row][col] = nums[i][j]
                col += 1
        return res
```



## 相似题目


## 参考资料

https://leetcode.com/articles/reshape-the-matrix/

## 日期

2018 年 11 月 1 日 —— 小光棍节


  [1]: http://bookshadow.com/weblog/2016/03/10/leetcode-palindrome-pairs/
