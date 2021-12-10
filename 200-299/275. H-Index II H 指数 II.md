作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/h-index-ii/description/

## 题目描述：

Given an array of citations ``sorted in ascending order`` (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have ``at least`` h citations each, and the other N − h papers have ``no more than`` h citations each."

Example:

    Input: citations = [0,1,3,5,6]
    Output: 3 
    Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had 
                 received 0, 1, 3, 5, 6 citations respectively. 
                 Since the researcher has 3 papers with at least 3 citations each and the remaining 
                 two with no more than 3 citations each, her h-index is 3.

Note:

If there are several possible values for h, the maximum one is taken as the h-index.

Follow up:

This is a follow up problem to H-Index, where ``citations`` is now guaranteed to be sorted in ascending order.
Could you solve it in logarithmic time complexity?

## 题目大意

计算某个研究人员的影响因子。影响因子的计算方式是有h篇影响力至少为h的论文。影响因子是衡量作者生产力和影响力的方式，判断了他又多少篇影响力很大的论文。和[274. H-Index][1]不同的是，这个题已经排好了序。

## 解题方法

解释一下样例：[0,1,3,5,6]，当h=0时表示至少有0篇影响力为0的论文；当h=1时表示至少有1篇影响力为1的论文；当h=3时表示至少有3篇影响力为3的论文；当h=5时表示至少有5篇影响力为5的论文；当h=6时表示至少有6篇影响力为6的论文.显然符合要求的是只要有3篇影响力为3的论文。

在[274. H-Index][1]中，是先排序再遍历做的，这个题已经排好了序，所以比274更简单，使用二分查找可以快速求解。

我们求的结果就是求影响力x和不小于该影响力的论文个数的最小值，然后再求这个最小值的最大值。

时间复杂度是O(logN)，空间复杂度是O(N)。

```python
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        l, r = 0, N - 1
        H = 0
        while l <= r:
            mid = l + (r - l) / 2
            H = max(H, min(citations[mid], N - mid))
            if citations[mid] < N - mid:
                l = mid + 1
            else:
                r = mid - 1
        return H
```

参考资料：


## 日期

2018 年 10 月 6 日 —— 努力看书


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/82949663
