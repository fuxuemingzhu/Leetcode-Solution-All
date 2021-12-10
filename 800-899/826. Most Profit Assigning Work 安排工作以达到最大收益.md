作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/most-profit-assigning-work/description/

## 题目描述：

We have jobs: ``difficulty[i]`` is the difficulty of the ``i``th job, and ``profit[i]`` is the profit of the ith job. 

Now we have some workers. ``worker[i]`` is the ability of the ``i``th worker, which means that this worker can only complete a job with difficulty at most ``worker[i]``. 

Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.  If a worker cannot complete any job, his profit is $0.

What is the most profit we can make?

Example 1:

    Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
    Output: 100 
    Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get profit of [20,20,30,30] seperately.

Notes:

1. ``1 <= difficulty.length = profit.length <= 10000``
1. ``1 <= worker.length <= 10000``
1. ``difficulty[i], profit[i], worker[i]``  are in range ``[1, 10^5]``


## 题目大意

有一堆工作，每个工作有对应的难度和收益，现在有几个工人需要干活，一个工人不能干几个活，但是一个活可以被多个工人多次的干。问这批工人能获得的最大收益。


## 解题方法

给的提示是双指针，其实我第一感觉是贪心的。事实上就是贪心。

贪心的策略是给每个工人计算在他的能力范围内，他能获得的最大收益，把这样的工作分配给他。

做的方法是先把困难程度和收益压缩排序，然后对工人排序，再对每个工人，通过从左到右的遍历确定其能获得收益最大值。由于工作和工人都已经排好序了，每次只需要从上次停止的位置继续即可，因此各自只需要遍历一次。

你可能会想到，每个工作的收益和其困难程度可能不是正相关的，可能存在某个工作难度小，但是收益反而很大，这种怎么处理呢？其实这也就是这个算法妙的地方，curMax并不是在每个工人查找其满足条件的工作时初始化的，而是在一开始就初始化了，这样一直保持的是所有的工作难度小于工人能力的工作中，能获得的收益最大值。

也就是说在查找满足条件的工作的时候，curMax有可能不更新，其保存的是目前为止的最大。res加的也就是在满足工人能力情况下的最大收益了。

时间复杂度是O(M+N)，空间复杂度是O(MN)。

```python
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        jobs = sorted([a, b] for a, b in zip(difficulty, profit))
        curMax, i = 0, 0
        res = 0
        for w in sorted(worker):
            while i < len(jobs) and w >= jobs[i][0]:
                curMax = max(curMax, jobs[i][1])
                i += 1
            res += curMax
        return res
```


参考资料：

https://leetcode.com/problems/most-profit-assigning-work/discuss/127031/C++JavaPython-Sort-and-Two-pointer

## 日期

2018 年 10 月 17 日 —— 今又重阳，战地黄花分外香
