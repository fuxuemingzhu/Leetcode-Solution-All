# 【LeetCode】378. Kth Smallest Element in a Sorted Matrix 解题报告（Python）

标签： LeetCode

---

题目地址：https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

## 题目描述：

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

    Example:
    
    matrix = [
       [ 1,  5,  9],
       [10, 11, 13],
       [12, 13, 15]
    ],
    k = 8,
    
    return 13.

Note: 

1. You may assume k is always valid, 1 ≤ k ≤ n2.

## 题目大意

找到一个有序二维数组的第k小的数字。这个二维数组，每行依次增加，每列依次增加。

## 解题方法

看到第k个的问题，就想到了用堆去做。竟然没超时！下面的代码也能通过。

```python
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        nums = []
        for line in matrix:
            nums.extend(line)
        heapq.heapify(nums)
        res = 0
        for i in range(k):
            res = heapq.heappop(nums)
        return res
```

根据堆的算法，可以实现改进，不用把每个元素都进堆，只需要把“最可能是最小值”的进堆即可。也就是说我们每次进堆的元素只要包括下一个最小的元素即可。

我们把左上角最小的元素和其索引进堆，然后把堆里的元素进行一个遍历，每次把元素的右边的元素进堆。当是第一列元素的时候，把这个元素下面的元素也进堆。

```python
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        q = [(matrix[0][0], 0, 0)]
        ans = 0
        for _ in range(k):
            ans, i, j = heapq.heappop(q)
            if j == 0 and i + 1 < m:
                heapq.heappush(q, (matrix[i + 1][j], i + 1, j))
            if j + 1 < n:
                heapq.heappush(q, (matrix[i][j + 1], i, j + 1))
        return ans
```

方法二：

二分查找，留给二刷。

http://bookshadow.com/weblog/2016/08/01/leetcode-kth-smallest-element-in-a-sorted-matrix/
http://www.cnblogs.com/grandyang/p/5727892.html

## 日期

2018 年 3 月 15 日 --雾霾消散，春光明媚


  [1]: http://blog.csdn.net/fuxuemingzhu/article/details/79559645