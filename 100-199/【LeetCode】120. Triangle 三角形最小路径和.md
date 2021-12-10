# 【LeetCode】120. Triangle 解题报告（Python）

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址https://leetcode.com/problems/triangle/description/

## 题目描述：

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
    
    [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

## 题目大意

找出一个正三角形从顶到下的最短路径。

## 解题方法

很多人肯定和我一样想到的是类似于二叉树的DFS，但是二叉树的每个叶子只会遍历一遍，但是这个三角形中，每个位置相当于被上面的两个节点所共有。所以转而用DP求解。

从顶向下的DP会导致元素越来越多，因此不是很方便，看到大神是从下向上的DP做的，很佩服！

使用minpath[k][i]保存从下向上得到的第k层第i个位置的最短路径。那么有：

```
minpath[k][i] = min( minpath[k+1][i], minpath[k+1][i+1]) + triangle[k][i];
```

然后可以看出minpath[k][i]只被用到了一次，所以可以变成一维DP：

```
For the kth level:
minpath[i] = min( minpath[i], minpath[i+1]) + triangle[k][i];
```

代码里需要注意的是dp的初始化应该是最下面一层，然后从倒数第二层开始遍历；第layer的元素是layer + 1个。

时间复杂度为O(n^2)，空间复杂度O(n)。n为三角形高度。

代码如下：

```python
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = triangle[-1]
        for layer in range(n - 2, -1, -1):
            for i in range(layer + 1):
                dp[i] = min(dp[i], dp[i + 1]) + triangle[layer][i]
        return dp[0]
```

参考资料：

https://leetcode.com/problems/triangle/discuss/38730/DP-Solution-for-Triangle

## 日期

2018 年 9 月 27 日 —— 国庆9天长假就要开始了！
