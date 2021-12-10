作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/video-stitching/

## 题目描述

You are given a series of video clips from a sporting event that lasted ``T`` seconds.  These video clips can be overlapping with each other and have varied lengths.

Each video clip ``clips[i]`` is an interval: it starts at time ``clips[i][0]`` and ends at time ``clips[i][1]``.  We can cut these clips into segments freely: for example, a clip ``[0, 7]`` can be cut into segments ``[0, 1] + [1, 3] + [3, 7]``.

Return the minimum number of clips needed so that we can cut the clips into segments that cover the entire sporting event (``[0, T]``).  If the task is impossible, return -1.

 

Example 1:

    Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
    Output: 3
    Explanation: 
    We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
    Then, we can reconstruct the sporting event as follows:
    We cut [1,9] into segments [1,2] + [2,8] + [8,9].
    Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0, 10].

Example 2:

    Input: clips = [[0,1],[1,2]], T = 5
    Output: -1
    Explanation: 
    We can't cover [0,5] with only [0,1] and [0,2].

Example 3:

    Input: clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], T = 9
    Output: 3
    Explanation: 
    We can take clips [0,4], [4,7], and [6,9].

Example 4:

    Input: clips = [[0,4],[2,8]], T = 5
    Output: 2
    Explanation: 
    Notice you can have extra video after the event ends.
     

Note:

1. ``1 <= clips.length <= 100``
1. ``0 <= clips[i][0], clips[i][1] <= 100``
1. ``0 <= T <= 100``

## 题目大意

给了一堆区间，要求选取最少的区间，这些区间能覆盖[0, T]区间。

## 解题方法

### 贪心

这个题还是很容易想到贪心的。贪心策略是在保证和前面的区间能连接的情况下，选择结尾最靠后的区间，这样的覆盖是最广的。举例来说，如果现在的区间是[0,3]，假设下一个区间要从[1,5]和[2,4]中选择，我们应该选择结尾最靠后的也就是[1,5]。

对于每个相同开头结尾的区间，我只保留结尾最大的那个。这个策略是相同开头的时候，覆盖越大越好。这样，总的区间数目不会超过100个。

然后，我看了Note里的提示，发现时间段的取值范围只有100，所以使用了一个暴力的方法：遍历。即对于区间[a,b]暴力遍历a+1到b中的每个元素，找出是否以该元素开头的区间：如果有，那么找出所有区间最靠后的结尾，则该区间是下一个应该选择的区间。如果对a+1和b之间的所有元素都遍历了，然而找不到存在的区间，那么一定断线了，所以返回-1.

这种贪心策略之下，则选取的区间个数是最少的。

Python代码如下：

```python
class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        count = collections.defaultdict(list)
        for cl in clips:
            if cl[0] in count:
                if cl[1] - cl[0] > count[cl[0]][1] - count[cl[0]][0]:
                    count[cl[0]].pop()
                    count[cl[0]] = cl
            else:
                count[cl[0]] = cl
        if 0 not in count: return -1
        prev = 0
        cur = count[0][1]
        next = cur
        res = 1
        while cur < T:
            hasFind = False
            for c in range(cur, prev, -1):
                if c in count:
                    if count[c][1] > next:
                        next = count[c][1]
                        prev = c
                        hasFind = True
            if not hasFind:
                return -1
            cur = next
            res += 1
        return res
```

## 日期

2019 年 4 月 7 日 —— 周赛bug了3次。。


  [1]: https://assets.leetcode.com/uploads/2019/04/04/sum-of-root-to-leaf-binary-numbers.png
