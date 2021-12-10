作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/champagne-tower/description/


## 题目描述

We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup (250ml) of champagne.

Then, some champagne is poured in the first glass at the top.  When the top most glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has it's excess champagne fall on the floor.)

For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.


![此处输入图片的描述][1]


Now after pouring some non-negative integer cups of champagne, return how full the j-th glass in the i-th row is (both i and j are 0 indexed.)


Example 1:

    Input: poured = 1, query_glass = 1, query_row = 1
    Output: 0.0
    Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.

Example 2:

    Input: poured = 2, query_glass = 1, query_row = 1
    Output: 0.5
    Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champange.
 

Note:

- poured will be in the range of [0, 10 ^ 9].
- query_glass and query_row will be in the range of [0, 99].


## 题目大意

往香槟塔最上面一层导入一定体积的香槟酒，求香槟塔每个位置杯子里的香槟体积。

## 解题方法

### 动态规划

这题使用类似动态规划的解法，需要解决的问题是从上一层的酒杯递推求出该层每个位置的酒的体积。

可以做以下思考：首先我们计算每个酒杯如果在没有往下分流的情况下，它会有多少体积的酒。然后分析这一层酒杯的酒如果满了，那么会流到哪里去？显然会均匀的流向下一层的两个相邻的杯子里去。

所以我们使用100 * 100的矩阵模拟每层的杯子，第一层的第一个杯子初始体积是倒入的酒的体积poured，然后向下递推，递推的方式下一层对应序号和下一层对应序号+1的两个杯子均分当前杯子超过1的部分。注意使用的是+=号，也就是下一层杯子的酒的体积是来自当前层流到里面酒体积的累加。

最后返回的时候需要再次判断，我们dp保存的是流经的液体的体积，不是真实的体积，所以和1取个最小值。

这题关键词： 二维数组，保存流经杯子的体积，只流到下一层相邻的两个杯子里，杯子液体体积累加。

本来使用的i遍历到N - 1即最后一层才结束，其实直接递推到题目要求的query_row就行了，后面的那些杯子不用管。

时间复杂度是O(N^2)，空间复杂度是O(100*100).

```python
class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        N = 100
        dp = [[0] * N for _ in range(N)]
        dp[0][0] = poured
        for i in range(query_row):
            for j in range(i + 1):
                if dp[i][j] > 1:
                    dp[i + 1][j    ] += (dp[i][j] - 1) / 2.0
                    dp[i + 1][j + 1] += (dp[i][j] - 1) / 2.0
        return min(1, dp[query_row][query_glass])
```


## 参考资料

https://www.youtube.com/watch?v=OqXzKsEWM44


## 日期

2018 年 10 月 27 日 —— 10月份最后一个周末


  [1]: https://s3-lc-upload.s3.amazonaws.com/uploads/2018/03/09/tower.png
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/83247054
