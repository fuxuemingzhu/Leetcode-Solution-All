作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/minimum-cost-to-hire-k-workers/description/

## 题目描述：

There are ``N`` workers.  The ``i-th`` worker has a quality[i] and a minimum wage expectation ``wage[i]``.

Now we want to hire exactly ``K`` workers to form a paid group.  When hiring a group of K workers, we must pay them according to the following rules:

Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
Every worker in the paid group must be paid at least their minimum wage expectation.
Return the least amount of money needed to form a paid group satisfying the above conditions.

 

Example 1:

    Input: quality = [10,20,5], wage = [70,50,30], K = 2
    Output: 105.00000
    Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.

Example 2:

    Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
    Output: 30.66667
    Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers seperately. 
 

Note:

1. 1 <= K <= N <= 10000, where N = quality.length = wage.length
1. 1 <= quality[i] <= 10000
1. 1 <= wage[i] <= 10000
1. Answers within 10^-5 of the correct answer will be considered correct.

## 题目大意

雇工人的题目。每个工人都有自己的质量和一个最小的期望工资。现在要找出K个工人，要求：

1. K个工人的质量和给他开的工资的比例是相同的。
2. 每个工人都要满足他的最小期望工资。

最后求雇佣K个工人，需要支付的最小钱数。

## 解题方法

这个题不是很好理解，经过我的仔细推敲后，觉得可以这么表述：每个工人都有自己期望的价性比，雇佣K个工人的时候要满足每个人的实际价性比不低于他的期望，即需要按照K个工人中的最高期望价性比给这K个人开工资。问需要的最少的工资是多少。注意使用的是价性比，不是性价比。因为性价比是我们买东西的时候希望的，而这些工人是出卖自己的劳动力的，因此他们希望得到更高的价性比。而作为选择工人的这一方，我们希望工人的性价比更高点，但是啊得注意，性价比高的工人会被那些性价比低的工人抬高工资，即他也会要求更高的工资，没有工人愿意看到别人好吃懒做还拿高工资，所以性价比高的工人会索要更高的工资，导致自己性价比和好吃懒做的工人一样。

如果理解了上面的那段话，那么我们需要按照价性比来做排序，然后依次遍历，得到K个工人的工资总和。

使用了一个大根堆，来获取K个工人的最大的价性比，作为K个工人的价性比，使用qsum保存K个工人的质量和。要给他们付的工资就是qsum * 最大性价比。

时间复杂度是O(Nlog(N))，空间复杂度是O(N)。

```python
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        works = sorted([(w / float(q), q) for w, q in zip(wage, quality)])
        que = []
        qsum = 0
        res = float("inf")
        for rate, q in works:
            heapq.heappush(que, -q)
            qsum += q
            if len(que) > K:
                qsum += heapq.heappop(que)
            if len(que) == K:
                res = min(res, qsum * rate)
        return res
```

参考资料：

https://leetcode.com/problems/minimum-cost-to-hire-k-workers/discuss/141768/Detailed-explanation-O(NlogN)

## 日期

2018 年 10 月 5 日 —— 转眼假期要结束了！！
